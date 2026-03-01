import discord 
import yfinance as yf

def get_current_stock_price(ticker_symbol: str) -> float:
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

liste = [
    "AAPL", 
    "TSLA", 
    "MSFT", 
    "AMZN", 
    "GOOGL", 
    "NFLX", 
    "MCD", 
    "UBSFY", 
    "KO"
]



def get_weekly_change(ticker: str) -> float | None:
    """
    Berechnet die prozentuale Kursänderung der letzten 7 Tage
    basierend auf Schlusskursen (YFinance).
    """

    try:
        stock = yf.Ticker(ticker)

        # letzte 7 Tage (Trading Days werden automatisch gefiltert)
        hist = stock.history(period="7d")

        if hist.empty or len(hist) < 2:
            return None

        start_price = hist["Close"].iloc[0]
        end_price = hist["Close"].iloc[-1]

        if start_price == 0:
            return None

        change_percent = ((end_price - start_price) / start_price) * 100
        return round(change_percent, 2)

    except Exception as e:
        print(f"Error fetching weekly change for {ticker}: {e}")
        return None









def create_financial_statistics_embed() -> discord.Embed:
    """Create a visually improved embed with financial statistics for all stocks"""

    embed = discord.Embed(
        title="📈 Financial Statistics",
        description="Current **stock prices** of the watched stocks:",
        color=discord.Color.blurple(),
        timestamp=discord.utils.utcnow()
    )

    for ticker in sorted(liste):
        price = get_current_stock_price(ticker)

        if price is not None:
            value = f"💲 **{price:,.2f} USD**"
        else:
            value = "⚠️ *Price not available*"

        embed.add_field(
            name=f"🏷️ {ticker}",
            value=value,
            inline=True
        )

    embed.set_footer(text="Data source: YFinance | Aktualisiert: {:%Y-%m-%d %H:%M:%S}".format(discord.utils.utcnow()))

    return embed



def create_weekly_ranking_embed() -> discord.Embed:
    """Create an embed showing a ranking based on last week's performance"""

    embed = discord.Embed(
        title="🏆 Wochen-Rangliste",
        description="Performance der Aktien **in den letzten 7 Tagen**",
        color=discord.Color.gold(),
        timestamp=discord.utils.utcnow()
    )

    ranking = []

    for ticker in liste:
        change = get_weekly_change(ticker)
        if change is not None:
            ranking.append((ticker, change))

    # Nach Performance sortieren (beste zuerst)
    ranking.sort(key=lambda x: x[1], reverse=True)

    medals = ["🥇", "🥈", "🥉"]

    for index, (ticker, change) in enumerate(ranking[:10]):  # Top 10
        emoji = medals[index] if index < 3 else "📊"
        sign = "📈" if change >= 0 else "📉"

        embed.add_field(
            name=f"{emoji} {index + 1}. {ticker}",
            value=f"{sign} **{change:+.2f}%**",
            inline=False
        )

    embed.set_footer(text="Time period: last 7 days")

    return embed