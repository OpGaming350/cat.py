from nextcord.ext import commands
import nextcord

embed = nextcord.Embed(
    title="CAT.PY", 
    url="https://media.discordapp.net/attachments/1064059871160446986/1076501456175247391/images_2.png",
    description="""It's is a discord bot written in python! Click On Dropdown Box To Check All Commands""",
    )
embed.set_thumbnail(url="https://media.discordapp.net/attachments/1064059871160446986/1076501456175247391/images_2.png")
embed.set_footer(text="Made By OpCat#6878 | EPICTRON DEVELOPMENT")
embed.color = 0xffcc33
embed2 = nextcord.Embed()
embed2.set_thumbnail(url="https://media.discordapp.net/attachments/1064059871160446986/1076501456175247391/images_2.png")
embed2.set_footer(text="Made By OpCat#6878 | EPICTRON DEVELOPMENT")
embed2.color = 0xffcc33
@commands.command()
async def help(ctx: commands.Context) -> None:
    menu = Menu()
    global embed
    await ctx.reply(view=Dropdown(), embed=embed)
class Menu(nextcord.ui.Select):
    def __init__(self):
        options = (
            nextcord.SelectOption(label="ADMIN", description="Shows The List Of Admin Commands"),
            nextcord.SelectOption(label="OWNER", description="Shows The Owner Commands"),
            nextcord.SelectOption(label="Soon", description="Soon")
        )
        super().__init__(placeholder="CLICK TO VIEW", options=options, min_values=1, max_values=1)
        
    async def callback(self, interaction: nextcord.Interaction):
        global embed  # Make embed a global variable
        value = interaction.data['values'][0]
        embed2.clear_fields()
        if value == 'ADMIN':
            embed2.title = 'ADMIN COMMANDS'
            embed2.description = '> Commands That Is Used By Admins'
            embed2.add_field(name="`//ban`", value="Bans members", inline=True)
            embed2.add_field(name="`//unban`", value="Unbans members", inline=False)
            embed2.add_field(name="`//mute`", value="Mutes members", inline=False)
            embed2.add_field(name="`//unmute`", value="Unmutes members", inline=False)
            embed2.add_field(name="`//lock`", value="Locks channel or servers", inline=False)
            embed2.add_field(name="`//unlock`", value="Unlocks channel or servers", inline=False)
            embed2.color = 0x3774aa
            
        elif value == 'OWNER':
            embed2.title = 'OWNER'
            embed2.description = 'You selected Option 2'
        elif value == 'Soon':
            embed2.title = 'Comming soon'
            embed2.description = 'You selected Option 3'
        await interaction.response.edit_message(embed=embed2, view=Dropdown())

class Dropdown(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Menu())

def setup(bot):
    bot.add_command(help)
