import discord
from discord.ui import View
from funktionen.inv_interface import get_inventory, add_item


async def buy_stock_view(
    ticker_symbol: str,
) -> View:
    class BuyStockView(View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)

            options = [
                discord.SelectOption(
                    label="buy 0.1 Stocks", description="Beschreibung 1"
                ),
                discord.SelectOption(
                    label="Buy 0.3 Stocks", description="Beschreibung 2"
                ),
                discord.SelectOption(
                    label="Buy 0.3 Stocks", description="Beschreibung 3"
                ),
                discord.SelectOption(
                    label="Buy 0.5 Stocks", description="Beschreibung 4"
                ),
                discord.SelectOption(
                    label="Buy 1 Stocks", description="Beschreibung 5"
                ),
                discord.SelectOption(
                    label="Buy 2 Stocks", description="Beschreibung 6"
                ),
                discord.SelectOption(
                    label="Buy 5 Stocks", description="Beschreibung 7"
                ),
                discord.SelectOption(
                    label="Buy 10 Stocks", description="Beschreibung 8"
                ),
            ]
            super().__init__(
                placeholder="choose amount to buy",
                min_values=1,
                max_values=1,
                options=options,
            )

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != self.author_id:
                await interaction.response.send_message(
                    "Its not your Button!", ephemeral=True
                )
                return

            selected_value = self.values[0]
            add_item(interaction.user.id, f"stock_{ticker_symbol}", selected_value)
            await interaction.response.send_message(
                f"You have bought {selected_value} Stocks of {ticker_symbol}!",
                ephemeral=True,
            )
