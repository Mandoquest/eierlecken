import discord
import asyncio
import yfinance as yf


async def create_buy_stock_embed(ticker_symbol: str) -> discord.Embed:
    loop = asyncio.get_running_loop()

    def fetch_info():
        ticker = yf.Ticker(ticker_symbol)
        return ticker.info

    info = await loop.run_in_executor(None, fetch_info)

    current_price = info.get("currentPrice") or "N/A"
    embed = discord.Embed(
        title="Buy Stock",
        description="Use the buttons below to buy stocks.",
        color=discord.Color.green(),
    )
    embed.add_field(
        name="Stock",
        value=f"You are about to buy shares of {ticker_symbol}.",
        inline=False,
    )
    embed.add_field(name="current_price", value=f"${current_price}", inline=True)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1170/1170576.png")
