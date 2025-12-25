import discord
import yfinance as yf
import asyncio


async def create_stock_embed(ticker_symbol: str) -> discord.Embed:
    loop = asyncio.get_running_loop()
    ticker_symbol = ticker_symbol.strip().upper()

    def fetch_info():
        ticker = yf.Ticker(ticker_symbol)
        try:
            # Fast info + full info as fallback
            fast = ticker.fast_info or {}
            full = ticker.info or {}
            return fast, full
        except Exception:
            return {}, {}

    try:
        fast_info, full_info = await asyncio.wait_for(
            loop.run_in_executor(None, fetch_info), timeout=3.0
        )
    except asyncio.TimeoutError:
        embed = discord.Embed(
            title=f"{ticker_symbol}",
            description="Error: Timeout while fetching data.",
            color=discord.Color.dark_gray(),
        )
        embed.add_field(
            name="Notice", value="Yahoo Finance did not respond.", inline=False
        )
        embed.set_footer(text="Please try again later.")
        return embed
    except Exception as e:
        embed = discord.Embed(
            title=f"{ticker_symbol}",
            description="Error fetching data.",
            color=discord.Color.dark_gray(),
        )
        embed.add_field(name="Error", value=str(e), inline=False)
        embed.set_footer(text="Error fetching from Yahoo Finance.")
        return embed

    if not fast_info and not full_info:
        embed = discord.Embed(
            title=f"{ticker_symbol}",
            description="Ticker not found or no data available.",
            color=discord.Color.dark_gray(),
        )
        embed.add_field(
            name="Notice", value="Check the ticker symbol (e.g., AAPL).", inline=False
        )
        embed.set_footer(text="Data source: Yahoo Finance")
        return embed

    # Get values, fallback from full info if missing
    name = fast_info.get("shortName") or full_info.get("shortName") or ticker_symbol
    current_price = fast_info.get("last_price") or full_info.get("currentPrice", "N/A")
    change_percent = fast_info.get("change_percent") or full_info.get("regularMarketChangePercent")
    market_cap = fast_info.get("market_cap") or full_info.get("marketCap", "N/A")
    volume = fast_info.get("volume") or full_info.get("volume", "N/A")
    year_high = fast_info.get("year_high") or full_info.get("fiftyTwoWeekHigh", "N/A")
    year_low = fast_info.get("year_low") or full_info.get("fiftyTwoWeekLow", "N/A")
    prev_close = fast_info.get("previous_close") or full_info.get("previousClose", "N/A")
    open_price = fast_info.get("open") or full_info.get("open", "N/A")

    # Format numbers for better readability
    if isinstance(current_price, (int, float)):
        current_price = f"${current_price:,.2f}"
    if isinstance(open_price, (int, float)):
        open_price = f"${open_price:,.2f}"
    if isinstance(prev_close, (int, float)):
        prev_close = f"${prev_close:,.2f}"
    if isinstance(market_cap, (int, float)):
        if market_cap >= 1_000_000_000:
            market_cap = f"${market_cap / 1_000_000_000:.2f}B"
        elif market_cap >= 1_000_000:
            market_cap = f"${market_cap / 1_000_000:.2f}M"
        else:
            market_cap = f"${market_cap}"
    if isinstance(volume, (int, float)):
        volume = f"{volume:,}"

    # Embed color based on daily change
    if change_percent is None:
        color = discord.Color.dark_gray()
    elif change_percent >= 0:
        color = discord.Color.green()
    else:
        color = discord.Color.red()

    embed = discord.Embed(
        title=f"{name} ({ticker_symbol})",
        description="Stock Information (Yahoo Finance)",
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

    embed.add_field(name="Price", value=f"{current_price}", inline=True)
    embed.add_field(
        name="Daily Change",
        value=(f"{change_percent:.2f}%" if isinstance(change_percent, (int, float)) else "N/A"),
        inline=True,
    )
    embed.add_field(name="Market Cap", value=f"{market_cap}", inline=False)
    embed.add_field(
        name="52-Week High / Low", value=f"{year_high} / {year_low}", inline=False
    )
    embed.add_field(name="Volume", value=f"{volume}", inline=True)
    embed.add_field(name="Open Price", value=f"{open_price}", inline=True)
    embed.add_field(name="Previous Close", value=f"{prev_close}", inline=True)

    embed.set_footer(text="Data from Yahoo Finance (fast_info + info)")
    return embed
