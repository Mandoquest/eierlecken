import discord

def buy_stock_embed(ticker_symbol: str):
    embed = discord.Embed(
        title=f"📈 Buy {ticker_symbol}",
        description=f"Select the amount of **{ticker_symbol}** stock you want to buy.",
        color=discord.Color.green()
    )
    
    embed.add_field(
        name="Instructions", 
        value="Use the dropdown to select amount and click **Buy** to confirm.",
        inline=False
    )
    
    embed.set_footer(text="Investment Bot")
    embed.set_thumbnail(url="https://i.imgur.com/3J9oM7H.png")  
    embed.timestamp = discord.utils.utcnow()
    
    return embed
