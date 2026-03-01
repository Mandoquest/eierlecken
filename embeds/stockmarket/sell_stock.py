import discord 

def sell_stock_embed(ticker_symbol: str, price: float | None = None):
    embed = discord.Embed(
        title=f"💰 Sell {ticker_symbol}",
        description=f"Select the amount of **{ticker_symbol}** stock you want to sell.",
        color=discord.Color.red()
    )
    if price is not None:
        embed.add_field(name="Price", value=f"${price:.2f}", inline=True)
    embed.add_field(
        name="Instructions",
        value="Use the dropdown to select amount and click **Confirm Sell** to confirm.",
        inline=False
    )
    embed.set_footer(text="Investment Bot")
    embed.set_thumbnail(url="https://i.imgur.com/3J9oM7H.png")
    embed.timestamp = discord.utils.utcnow()
    
    return embed