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
    embed = discord.Embed(
        title="Pong!",
        description="Der Bot ist online und bereit.",
        color=0x00ff00
    )
    embed.set_image(url="https://i.imgur.com/4M34hi2.png")
    await ctx.send(embed=embed)

# Funktion, um Stock-Embed zu erstellen
async def create_stock_embed(ticker_symbol: str):
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period="3mo")

    if data.empty:
        embed = discord.Embed(
            title=f"Aktie {ticker_symbol} nicht gefunden",
            description="Bitte überprüfe das Ticker-Symbol.",
            color=discord.Color.red()
        )
        return embed, None

    # Plot erstellen
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data['Close'], label='Schlusskurs', color='green', linewidth=2)
    plt.fill_between(data.index, data['Close'], color='green', alpha=0.1)
    for i in range(1, len(data)):
        if data['Close'].iloc[i] < data['Close'].iloc[i-1]:
            plt.plot(data.index[i-1:i+1], data['Close'].iloc[i-1:i+1], color='red', linewidth=2)
    plt.title(f"{ticker_symbol} - Letzte 3 Monate")
    plt.xlabel("Datum")
    plt.ylabel("Preis (USD)")
    plt.grid(True)

    filename = f"chart_{ticker_symbol}_{int(datetime.utcnow().timestamp())}.png"
    plt.savefig(filename)
    plt.close()

    embed = discord.Embed(
        title=f"{ticker_symbol} Aktieninfo",
        description=f"Aktueller Kurs: ${data['Close'].iloc[-1]:.2f}",
        color=discord.Color.blue(),
        timestamp=datetime.utcnow()
    )

    return embedname

# Stock-Befehl
@bot.command()
async def stock(ctx, ticker: str):
    embedname = await create_stock_embed(ticker)
    
    if filename:
        file = discord.File(filename, filename=filename)
        embed.set_image(url=f"attachment://{filename}")
    else:
        file = None  # Aktie nicht gefunden

    # Button erstellen
    button = Button(label="Bild löschen", style=discord.ButtonStyle.red)

    async def button_callback(interaction):
        new_embed = embed.copy()
        new_embed.set_image(url=None)
        # Attachments entfernen, damit das Bild verschwindet
        await interaction.response.edit_message(embed=new_embed, view=None, attachments=[])
    
    button.callback = button_callback
    view = View()
    view.add_item(button)

    await ctx.send(embed=embed=file, view=view)

    # Datei nach dem Senden löschen, um Speicher zu sparen
    if filename and os.path.exists(filename):
        os.remove(filename)

# Token laden und Bot starten
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
