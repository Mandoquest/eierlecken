import discord
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views
from funktionen.protectetview import ProtectedView
import os

class StockButtons(ProtectedView):
    def __init__(self, ticker_symbol: str, author_id: int):
        super().__init__(author_id)
        self.ticker_symbol = ticker_symbol

    @discord.ui.button(label="← Back", style=discord.ButtonStyle.red)
    async def back(self, interaction: discord.Interaction, _):
        embed = await choose_Embeds("stockm_p1")
        view = await choose_Views("stockm_p1", author_id=self.author_id)

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[]
        )
        

    @discord.ui.button(label="Buy Stock", style=discord.ButtonStyle.green, emoji="🛒")
    async def buy(self, interaction: discord.Interaction, _):
        embed = await choose_Embeds("buy_Stock", ticker_symbol=self.ticker_symbol)
        view = await choose_Views("buy_Stock", ticker_symbol=self.ticker_symbol, author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label="Sell Stock", style=discord.ButtonStyle.red, emoji="💰")
    async def sell(self, interaction: discord.Interaction, _):
        embed = await choose_Embeds("sell_stock", ticker_symbol=self.ticker_symbol)
        view = await choose_Views("sell_stock", ticker_symbol=self.ticker_symbol, author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)


async def create_stock_buttons(ticker_symbol: str, author_id: int):
    return StockButtons(ticker_symbol, author_id)
