import discord
from discord.ext import commands
from discord.ui import Button, View
import os
from dotenv import load_dotenv
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Bot Setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")

# Ein einfacher Ping-Befehl
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Token laden und Bot starten
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
