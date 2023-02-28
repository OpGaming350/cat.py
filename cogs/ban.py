import nextcord
from nextcord.ext import commands

class BanUnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        """
        Bans a member from the server.

        Example usage:
        !ban @member#1234 Offensive language
        """
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned. Reason: {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the member to ban.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Could not find the member. Please try again.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to ban members.")
        else:
            await ctx.send("An error occurred while trying to ban the member. Please try again later.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: nextcord.User, *, reason=None):
        """
        Unbans a member from the server.

        Example usage:
        !unban @member#1234 Ban was a mistake
        """
        await ctx.guild.unban(member, reason=reason)
        await ctx.send(f"{member} has been unbanned. Reason: {reason}")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the member to unban.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Could not find the member. Please try again.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to unban members.")
        else:
            await ctx.send("An error occurred while trying to unban the member. Please try again later.")

def setup(bot):
    bot.add_cog(BanUnbanCog(bot))
