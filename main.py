import nextcord
from nextcord.ext import commands
import os 
import json

# Opens Config Files
with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']
ALLOWED_USERS = config['allowed_users']

intents = nextcord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=config['prefix'],intents=intents)
bot.remove_command("help")

# Text that shows on console when ready
@bot.event
async def on_ready():
    print(f"   ____      _                 ")
    print(f"  / ___|__ _| |_   _ __  _   _ ")
    print(f" | |   / _` | __| | '_ \| | | |")
    print(f" | |__| (_| | |_ _| |_) | |_| |")
    print(f"  \____\__,_|\__(_) .__/ \__, |") 
    print(f"                  |_|    |___/ ")
    print(f"\033[92m > BOT ONLINE")
    await bot.change_presence(activity=nextcord.Game(name="Cat.py Coming Soon..."))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You are not allowed to use this command.")
    else:
        print(error)

for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")

def is_allowed(ctx):
    return ctx.author.id in ALLOWED_USERS

@bot.command()
@commands.check(is_allowed)
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded Cogs")

@bot.command()
@commands.check(is_allowed)
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded Cogs")

@bot.command()
@commands.check(is_allowed)
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send("Reloaded Cogs")

bot.run(TOKEN)

# ©Code written by OpCat The King#6878 and edited and bugfixing by Ghast#0001