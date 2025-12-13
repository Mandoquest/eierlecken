import discord
import yfinance as yf
import asyncio
from typing import Optional


async def create_stock_embed(ticker_symbol: str) -> discord.Embed:
    loop = asyncio.get_running_loop()
    ticker_symbol = ticker_symbol.strip().upper()

    def fetch_info():
        ticker = yf.Ticker(ticker_symbol)

        try:
            return ticker.fast_info or {}
        except Exception:
            return {}

    try:

        info = await asyncio.wait_for(
            loop.run_in_executor(None, fetch_info), timeout=3.0
        )
    except asyncio.TimeoutError:
        embed = discord.Embed(
            title=f"{ticker_symbol}",
            description="Fehler: Zeitüberschreitung beim Abrufen der Daten.",
            color=discord.Color.dark_gray(),
        )
        embed.add_field(
            name="Hinweis", value="Yahoo Finance reagierte nicht.", inline=False
        )
        embed.set_footer(text="Versuche es später erneut.")
        return embed
    except Exception as e:
        embed = discord.Embed(
            title=f"{ticker_symbol}",
            description="Fehler beim Abrufen der Daten.",
            color=discord.Color.dark_gray(),
        )
        embed.add_field(name="Fehler", value=str(e), inline=False)
        embed.set_footer(text="Fehler beim Abruf von Yahoo Finance.")
        return embed

    if not info:
        embed = discord.Embed(
            title=f"{ticker_symbol}",
            description="Ticker nicht gefunden oder keine Daten verfügbar.",
            color=discord.Color.dark_gray(),
        )
        embed.add_field(
            name="Hinweis", value="Prüfe das Tickersymbol (z.B. AAPL).", inline=False
        )
        embed.set_footer(text="Datenquelle: Yahoo Finance")
        return embed

    name = info.get("shortName") or ticker_symbol
    current_price = info.get("last_price", "N/A")
    change_percent = info.get("change_percent")
    market_cap = info.get("market_cap", "N/A")
    volume = info.get("volume", "N/A")
    year_high = info.get("year_high", "N/A")
    year_low = info.get("year_low", "N/A")
    prev_close = info.get("previous_close", "N/A")
    open_price = info.get("open", "N/A")

    if change_percent is None:
        color = discord.Color.dark_gray()
    elif change_percent >= 0:
        color = discord.Color.green()
    else:
        color = discord.Color.red()

    embed = discord.Embed(
        title=f"{name} ({ticker_symbol})",
        description="Aktieninformationen (Yahoo Finance)",
        color=color,
    )

    if ticker_symbol.isalpha():

        domain_map = {
            "AAPL": "apple.com",
            "MSFT": "microsoft.com",
            "AMZN": "amazon.com",
            "GOOGL": "abc.xyz",
            "NVDA": "nvidia.com",
            "META": "meta.com",
            "TSLA": "tesla.com",
            "JPM": "jpmorganchase.com",
        }
        domain = domain_map.get(ticker_symbol, f"{ticker_symbol.lower()}.com")
        embed.set_thumbnail(url=f"https://logo.clearbit.com/{domain}")

    embed.add_field(name="Kurs", value=f"${current_price}", inline=True)
    embed.add_field(
        name="Tagesveränderung",
        value=(
            f"{change_percent:.2f}%"
            if isinstance(change_percent, (int, float))
            else "N/A"
        ),
        inline=True,
    )
    embed.add_field(name="Marktkapitalisierung", value=f"{market_cap}", inline=False)
    embed.add_field(
        name="52-Wochen Hoch / Tief", value=f"{year_high} / {year_low}", inline=False
    )
    embed.add_field(name="Volumen", value=f"{volume}", inline=True)
    embed.add_field(name="Eröffnungskurs", value=f"${open_price}", inline=True)
    embed.add_field(name="Vorheriger Schlusskurs", value=f"${prev_close}", inline=True)

    embed.set_footer(text="Daten von Yahoo Finance (fast_info)")
    return embed
