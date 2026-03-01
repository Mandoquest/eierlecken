import discord
import asyncio
import yfinance as yf
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views
from funktionen.protectetview import ProtectedView
import os


def fetch_stock_price(ticker_symbol: str) -> float:
    try:
        ticker = yf.Ticker(ticker_symbol)
        price = ticker.info.get("regularMarketPrice")
        if price is None:
            raise ValueError("Price not found in ticker info")
        return float(price)
    except Exception as e:
        print(f"Error fetching stock price for {ticker_symbol}: {e}")
        return 0.0
class StockButtons(ProtectedView):
    def __init__(self, ticker_symbol: str, author_id: int):
        super().__init__(author_id)
        self.ticker_symbol = ticker_symbol

    @discord.ui.button(label="← Back", style=discord.ButtonStyle.red)
    async def back(self, interaction: discord.Interaction, _):
        embed = await choose_Embeds("stockm_p1")
        view = await choose_Views("stockm_p1", author_id=self.author_id)#
        
        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[]
        )
        

    @discord.ui.button(label="Buy Stock", style=discord.ButtonStyle.green, emoji="🛒")
    async def buy(self, interaction: discord.Interaction, _):

        price = fetch_stock_price(self.ticker_symbol)
        embed = await choose_Embeds("buy_Stock", ticker_symbol=self.ticker_symbol, price=price)
        view = await choose_Views("buy_Stock", ticker_symbol=self.ticker_symbol, author_id=self.author_id, value=price)
        await interaction.response.edit_message(embed=embed, view=view, attachments=[])

    @discord.ui.button(label="Sell Stock", style=discord.ButtonStyle.red, emoji="💰")
    async def sell(self, interaction: discord.Interaction, _):
        print("Sell button clicked")
        price = fetch_stock_price(self.ticker_symbol)
        embed = await choose_Embeds("sell_stock", ticker_symbol=self.ticker_symbol, price=price)
        print("Embed created for sell stock")
        # include the current price so the selling view can calculate earnings
        view = await choose_Views(
            "sell_stock",
            ticker_symbol=self.ticker_symbol,
            author_id=self.author_id,
            value=price,
        )
        print("View created for sell stock")
        await interaction.response.edit_message(embed=embed, view=view, attachments=[])
        print("------------------------------------Done------------------------------------")

async def create_stock_buttons(ticker_symbol: str, author_id: int):
    return StockButtons(ticker_symbol, author_id)
