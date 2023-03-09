import nextcord
from nextcord.ext import commands

class DeleteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete', aliases=['del'])
    async def delete_message(self, ctx, amount: int):
        """
        Deletes the specified number of messages on the current channel.
        Usage: !delete <amount>
        """
        channel = ctx.channel
        messages = await channel.history(limit=amount + 1).flatten()
        for message in messages:
            await message.delete()

def setup(bot):
    bot.add_cog(DeleteCog(bot))
