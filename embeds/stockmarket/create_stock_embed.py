import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yfinance as yf
import discord
from datetime import datetime

def create_stock_embed_sync(ticker_symbol: str):
    # Aktie abrufen
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period="3mo")

    # Fehlerbehandlung
    if data.empty:
        embed = discord.Embed(
            title=f"Aktie {ticker_symbol} nicht gefunden",
            description="Bitte überprüfe das Ticker-Symbol.",
            color=discord.Color.red()
        )
        return embed, None

    # Plot vorbereiten
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor("white")  # Hintergrund weiß

    # Linien zwischen Schlusskursen einzeichnen mit leichter Transparenz
    for i in range(1, len(data)):
        color = 'green' if data['Close'].iloc[i] >= data['Close'].iloc[i-1] else 'red'
        ax.plot(
            data.index[i-1:i+1], 
            data['Close'].iloc[i-1:i+1], 
            color=color, 
            linewidth=2, 
            alpha=0.8,   # leichte Transparenz für moderneren Look
            zorder=3
        )

    # Achsen sichtbar und durchgehend
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('black')
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_color('black')
    ax.spines['left'].set_linewidth(1.5)

    # Ticks
    ax.tick_params(axis='y', which='both', direction='in', length=5, color='black')
    ax.tick_params(axis='x', rotation=20, color='black')

    # Titel und X-Achse begrenzen
    ax.set_title(f"{ticker_symbol} - Letzte 3 Monate", fontsize=16, weight='bold')
    ax.set_xlim(data.index[0], data.index[-1])

    # Plot speichern
    filename = f"chart_{ticker_symbol}.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.close(fig)

    # Discord Embed erstellen
    embed = discord.Embed(
        title=f"{ticker_symbol} Aktieninfo",
        description=f"Aktueller Kurs: ${data['Close'].iloc[-1]:.2f}",
        color=discord.Color.blue(),
        timestamp=datetime.utcnow()
    )
    embed.set_image(url=f"attachment://{filename}")
    

    return embed, filename
