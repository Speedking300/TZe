import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # besser als im Klartext

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Selfbot gestartet als {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Online 24/7"))

@bot.command()
async def setstatus(ctx, *, text):
    await bot.change_presence(activity=discord.Game(name=text))
    await ctx.send(f"✅ Status geändert zu: **{text}**")

bot.run(TOKEN)
