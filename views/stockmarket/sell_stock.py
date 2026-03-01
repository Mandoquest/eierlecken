import discord
from discord.ui import View, Select, Button
from funktionen.inv_interface import add_item, remove_item, get_inventory
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views

class StockSellView(View):
    def __init__(self, ticker_symbol: str, author_id: int, value: float):
        super().__init__(timeout=60)
        self.ticker = ticker_symbol
        self.ticker_symbol = ticker_symbol  # Store both names for compatibility
        self.author_id = author_id
        # keep both `price` and `value` attributes so other code can refer to either
        self.price: float = float(value)
        self.value: float = float(value)
        self.selected_amount: float | None = None
        self.add_item(StockAmountSelect(self))
        self.add_item(BackButton(self))
        self.add_item(ConfirmButton(self))


class StockAmountSelect(Select):
    def __init__(self, view: StockSellView):
        self.view_ref = view

        options = [
            discord.SelectOption(label="Sell 0.1 Stocks", value="0.1"),
            discord.SelectOption(label="Sell 0.3 Stocks", value="0.3"),
            discord.SelectOption(label="Sell 0.5 Stocks", value="0.5"),
            discord.SelectOption(label="Sell 1 Stock", value="1"),
            discord.SelectOption(label="Sell 2 Stocks", value="2"),
            discord.SelectOption(label="Sell 5 Stocks", value="5"),
            discord.SelectOption(label="Sell 10 Stocks", value="10"),
        ]

        super().__init__(
            placeholder="Choose amount to sell",
            min_values=1,
            max_values=1,
            options=options,
            row=0
        )

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.view_ref.author_id:
            await interaction.response.send_message(
                "❌ This menu is not for you!",
                ephemeral=True
            )
            return

        self.view_ref.selected_amount = float(self.values[0])

        await interaction.response.send_message(
            f"📝 Selected **{self.view_ref.selected_amount} stocks**",
            ephemeral=True
        )


class ConfirmButton(Button):
    def __init__(self, view: StockSellView):
        self.view_ref = view
        super().__init__(
            label="Confirm Sell",
            style=discord.ButtonStyle.green,
            row=1
        )

    async def callback(self, interaction: discord.Interaction):
        print("ConfirmButton clicked")
        if interaction.user.id != self.view_ref.author_id:
            await interaction.response.send_message(
                "❌ This button is not for you!",
                ephemeral=True
            )
            return

        if self.view_ref.selected_amount is None:
            await interaction.response.send_message(
                "⚠️ Please select an amount first!",
                ephemeral=True
            )
            return

        owned = get_inventory(
            interaction.user.id,
            self.view_ref.ticker_symbol
        )

        if self.view_ref.selected_amount > owned:
            await interaction.response.send_message(
                f"❌ You only own **{owned}** stocks!",
                ephemeral=True
            )
            return

        # use the stored price (same as value) to compute earnings
        earnings = self.view_ref.selected_amount * self.view_ref.price

        
        remove_item(
            interaction.user.id,
            self.view_ref.ticker_symbol,
            self.view_ref.selected_amount
        )

        # Add coins
        add_item(
            interaction.user.id,
            "MandoCoins",
            earnings
        )

        await interaction.response.send_message(
            f"💰 You sold **{self.view_ref.selected_amount} "
            f"{self.view_ref.ticker_symbol}** stocks\n"
            f"💵 Earned **{earnings} MandoCoins**",
            ephemeral=True
        )

        # disable only the amount selector and confirm button so the user can't resell
        # keep the back button enabled so they can still navigate away
        for child in self.view_ref.children:
            # dropdown or confirm button should be disabled
            if isinstance(child, Select) or (isinstance(child, Button) and child.label == "Confirm Sell"):
                child.disabled = True
        # we don't stop the view here; leaving it running lets the back-button remain active
        await interaction.message.edit(view=self.view_ref)


class BackButton(Button):
    def __init__(self, view: StockSellView):
        self.view_ref = view
        super().__init__(
            label="Back",
            style=discord.ButtonStyle.red,
            row=1
        )

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.view_ref.author_id:
            await interaction.response.send_message(
                "❌ This button is not for you!",
                ephemeral=True
            )
            return


        # navigate back to the individual stock page where the user came from
        view = await choose_Views(
            "stockmarket_main",
            author_id=self.view_ref.author_id,
        )
        embed = await choose_Embeds(
            "stockmarket_main",
            author_id=self.view_ref.author_id,
        )
        await interaction.response.edit_message(embed=embed, view=view)
