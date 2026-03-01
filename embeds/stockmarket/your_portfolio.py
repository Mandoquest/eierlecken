import discord 
import yfinance as yf
from funktionen.inv_interface import get_inventory


def get_current_stock_price(ticker_symbol: str):
    """Fetch current stock price from yfinance"""
    try:
        stock = yf.Ticker(ticker_symbol)
        data = stock.history(period="1d")
        
        if data.empty:
            return None
        
        return float(data['Close'].iloc[-1])
    except Exception as e:
        print(f"Error fetching price for {ticker_symbol}: {e}")
        return None


def create_your_portfolio_embed(author_id: int):
    stocks = get_inventory(author_id, category="stock")

    embed = discord.Embed(
        title="📈 Your Portfolio",
        description="Here you can see your current stock holdings.",
        color=discord.Color.blue()
    )

    # Normalize inventory
    if isinstance(stocks, dict):
        stocks_list = [{"item": k, **v} for k, v in stocks.items()]
    elif isinstance(stocks, list):
        stocks_list = stocks
    else:
        stocks_list = []

    if not stocks_list:
        embed.add_field(
            name="🪙 No Stocks",
            value="You don't currently own any stocks.",
            inline=False
        )
        return embed

    total_value = 0.0

    for stock in stocks_list:
        ticker = stock.get("item", "Unknown")
        amount = stock.get("amount", 0)

        price = get_current_stock_price(ticker)

        if price is not None:
            value = price * amount
            total_value += value

            field_value = (
                f"📦 **Amount:** {amount}\n"
                f"💵 **Price:** ${price:,.2f}\n"
                f"💰 **Value:** ${value:,.2f}"
            )
        else:
            field_value = (
                f"📦 **Amount:** {amount}\n"
                f"⚠️ Price unavailable"
            )

        embed.add_field(
            name=f"🏷️ {ticker}",
            value=field_value,
            inline=False
        )

    embed.add_field(
        name="📊 Total Portfolio Value",
        value=f"💎 **${total_value:,.2f}**",
        inline=False
    )

    embed.set_footer(text=f"User ID {author_id}")
    embed.timestamp = discord.utils.utcnow()

    return embed