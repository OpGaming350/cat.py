import nextcord
from nextcord.ext import commands

class LockdownCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: nextcord.TextChannel = None):
        """
        Locks down the specified channel or the entire server if no channel is specified.

        Example usage:
        !lockdown #general
        !lockdown
        """
        if not channel:
            # If no channel is specified, lock down the entire server
            overwrites = {
                ctx.guild.default_role: nextcord.PermissionOverwrite(send_messages=False)
            }
            for channel in ctx.guild.text_channels:
                await channel.edit(overwrites=overwrites)
            await ctx.send("The server has been locked down.")
        else:
            overwrites = channel.overwrites_for(ctx.guild.default_role)
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"{channel.mention} has been locked down.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: nextcord.TextChannel = None):
        """
        Unlocks the specified channel or the entire server if no channel is specified.

        Example usage:
        !unlock #general
        !unlock
        """
        if not channel:
            # If no channel is specified, unlock the entire server
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(ctx.guild.default_role, overwrite=None)
            await ctx.send("The server has been unlocked.")
        else:
            overwrites = channel.overwrites_for(ctx.guild.default_role)
            overwrites.send_messages = None
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"{channel.mention} has been unlocked.")

    @lockdown.error
    @unlock.error
    async def lockdown_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Could not find the specified channel. Please try again.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to manage channels.")
        else:
            await ctx.send("An error occurred while trying to lock down or unlock the channel/server. Please try again later.")

def setup(bot):
    bot.add_cog(LockdownCog(bot))
