import discord
from discord.ui import View
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


async def create_stock_buttons(ticker_symbol: str, author_id: int) -> View:
    class Stockbuttons(View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)

        @discord.ui.button(
            label="back ",
            style=discord.ButtonStyle.red,
            emoji="⬅️",
            custom_id="back_to_stockmarket",
        )
        async def back_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stockmarket")
            view = await choose_Views("Stockmarket_page1")
            await interaction.response.edit_message(embed=embed, view=view)

        @discord.ui.button(
            label="buy stock",
            style=discord.ButtonStyle.green,
            emoji="🛒",
            custom_id="buy_stock",
        )
        async def buy_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol=ticker_symbol)
            view = await choose_Views("stock", ticker_symbol=ticker_symbol , author_id=author_id)
            await interaction.response.edit_message(embed=embed, view=view)

        @discord.ui.button(
            label="sell stock",
            style=discord.ButtonStyle.red,
            emoji="💰",
            custom_id="sell_stock",
        )
        async def sell_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds(
                "sell_stock",
                ticker_symbol=ticker_symbol,
            )
            view = await choose_Views("sell_stock", ticker_symbol=ticker_symbol)
            await interaction.response.edit_message(embed=embed, view=view)

    return Stockbuttons
