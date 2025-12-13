import os
import yfinance as yf
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def create_stock_embed(ticker_symbol: str) -> discord.Embed:
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    name = info.get("shortName", ticker_symbol)
    current_price = info.get("currentPrice") or "N/A"
    change_percent = info.get("regularMarketChangePercent")
    change_percent_str = (
        f"{change_percent:.2f}%" if change_percent is not None else "N/A"
    )
    market_cap = info.get("marketCap")
    market_cap_str = f"${market_cap:,}" if market_cap else "N/A"
    volume = info.get("volume")
    volume_str = f"{volume:,}" if volume else "N/A"
    fifty_two_week_high = info.get("fiftyTwoWeekHigh") or "N/A"
    fifty_two_week_low = info.get("fiftyTwoWeekLow") or "N/A"
    dividend_yield = info.get("dividendYield")
    dividend_yield_str = f"{dividend_yield:.2f}%" if dividend_yield else "Keine"
    sector = info.get("sector", "N/A")
    open_price = info.get("open") or "N/A"
    prev_close = info.get("previousClose") or "N/A"
    pe_ratio = info.get("trailingPE") or "N/A"
    eps = info.get("trailingEps") or "N/A"
    logo_url = info.get("logo_url")

    color = (
        discord.Color.green()
        if change_percent and change_percent >= 0
        else discord.Color.red()
    )

    embed = discord.Embed(
        title=f"{name} ({ticker_symbol.upper()})",
        description="Aktieninformationen von Yahoo Finance",
        color=color,
    )

    if logo_url:
        embed.set_thumbnail(url=logo_url)

    embed.add_field(name="Kurs", value=f"${current_price}", inline=True)
    embed.add_field(name="Tagesveränderung", value=change_percent_str, inline=True)
    embed.add_field(name="Marktkapitalisierung", value=market_cap_str, inline=False)
    embed.add_field(
        name="52-Wochen Hoch / Tief",
        value=f"{fifty_two_week_high} / {fifty_two_week_low}",
        inline=False,
    )
    embed.add_field(name="Volumen", value=volume_str, inline=True)
    embed.add_field(name="Eröffnungskurs", value=f"${open_price}", inline=True)
    embed.add_field(name="Vorheriger Schlusskurs", value=f"${prev_close}", inline=True)
    embed.add_field(name="Dividendenrendite", value=dividend_yield_str, inline=True)
    embed.add_field(name="Sektor", value=sector, inline=True)
    embed.add_field(name="KGV", value=f"{pe_ratio}", inline=True)
    embed.add_field(name="EPS", value=f"{eps}", inline=True)

    embed.set_footer(text="Daten von Yahoo Finance")
    return embed


@bot.command()
async def stock(ctx, ticker_symbol: str):
    """Sendet ein schönes Aktien-Embed für den angegebenen Ticker"""
    try:
        embed = create_stock_embed(ticker_symbol)
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Fehler beim Abrufen der Aktie '{ticker_symbol}': {e}")


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
