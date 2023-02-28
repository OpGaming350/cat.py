import nextcord
from nextcord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        """
        Kicks a member from the server.

        Example usage:
        !kick @member#1234 Kicking for breaking rules
        """
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked from the server. Reason: {reason}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the member to kick.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Could not find the member. Please try again.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to kick members.")
        else:
            await ctx.send("An error occurred while trying to kick the member. Please try again later.")

def setup(bot):
    bot.add_cog(KickCog(bot))
