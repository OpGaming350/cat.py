import nextcord
from nextcord.ext import commands

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx):
        """
        Shows the status of the bot.
        """
        embed = nextcord.Embed(title="Bot Status", color=0x00ff00)
        embed.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms")
        embed.add_field(name="Guilds", value=f"{len(self.bot.guilds)}")
        embed.add_field(name="Users", value=f"{len(self.bot.users)}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(StatusCog(bot))
