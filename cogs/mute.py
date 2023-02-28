import nextcord
from nextcord.ext import commands
from asyncio import sleep

class TimeoutCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: nextcord.Member, duration: int, *, reason=None):
        """
        Timeouts a member in the server for a specified duration (in seconds).

        Example usage:
        !timeout @member#1234 60 Spamming the chat
        """
        timeout_role = nextcord.utils.get(ctx.guild.roles, name="Timeout")
        if not timeout_role:
            # Create the Timeout role if it doesn't exist
            timeout_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(timeout_role, read_messages=True, send_messages=False)
        await member.add_roles(timeout_role, reason=reason)
        await ctx.send(f"{member} has been timed out for {duration} seconds. Reason: {reason}")

        # Wait for the duration and then remove the timeout role from the member
        await sleep(duration)
        await member.remove_roles(timeout_role, reason="Timeout period ended.")
        await ctx.send(f"{member}'s timeout has ended.")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the member and duration for the timeout.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Could not find the member or the duration was not a number. Please try again.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to timeout members.")
        else:
            await ctx.send("An error occurred while trying to timeout the member. Please try again later.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: nextcord.Member):
        """
        Removes the timeout role from a timed out member.

        Example usage:
        !untimeout @member#1234
        """
        timeout_role = nextcord.utils.get(ctx.guild.roles, name="Muted")
        if not timeout_role:
            await ctx.send("No members are currently timed out.")
        elif timeout_role in member.roles:
            await member.remove_roles(timeout_role, reason="Timeout manually lifted by moderator.")
            await ctx.send(f"{member}'s timeout has been lifted.")
        else:
            await ctx.send(f"{member} is not currently timed out.")

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the member to untimeout.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Could not find the member. Please try again.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to untimeout members.")
        else:
            await ctx.send("An error occurred while trying to untimeout the member. Please try again later.")

def setup(bot):
    bot.add_cog(TimeoutCog(bot))
