import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def aktie(ctx, symbol: str):

    file = discord.File("chart.png", filename="chart.png")
    
    embed = discord.Embed(title=f"{symbol} Aktienkurs")
    embed.set_image(url="attachment://chart.png")  # Lokale Datei im Embed
    await ctx.send(file=file, embed=embed)



load_dotenv()
token = os.getenv("DISCORD_TOKEN")





bot.run(token)