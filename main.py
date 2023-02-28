import nextcord
from nextcord.ext import commands
import os 

intents = nextcord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='//', intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
  print(f"   ____      _                 ")
  print(f"  / ___|__ _| |_   _ __  _   _ ")
  print(f" | |   / _` | __| | '_ \| | | |")
  print(f" | |__| (_| | |_ _| |_) | |_| |")
  print(f"  \____\__,_|\__(_) .__/ \__, |") 
  print(f"                  |_|    |___/ ")
  print(f"\033[92m > BOT ONLINE")

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="Cat.py"))

for fn in os.listdir('./cogs'):
  if fn.endswith('.py'):
    bot.load_extension(f"cogs.{fn[:-3]}")

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f"cogs.{extension}")
  await ctx.send("Loaded Cogs")

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f"cogs.{extension}")
  await ctx.send("Unloaded Cogs")
  
@bot.command()
async def reload(ctx, extension):
  bot.reload_extension(f"cogs.{extension}")
  await ctx.send("Reloaded Cogs")
  
bot.run("MTA2NDkzMzQ5MDM3OTk4MDg4Mg.Gg7Vf3.5Xy1k7Bwauz8W-uWyBfMsmShc2WZtIME06zj9w")