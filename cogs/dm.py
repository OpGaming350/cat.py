import nextcord
from nextcord.ext import commands

class DmCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dm(self, ctx, user: nextcord.User, *, message: str):
        """Sends a direct message to a user."""
        try:
            await user.send(message)
            await ctx.send(f"Message sent to {user.name}.")
        except nextcord.HTTPException:
            await ctx.send(f"Failed to send a message to {user.name}.")

def setup(bot):
    bot.add_cog(DmCog(bot))
