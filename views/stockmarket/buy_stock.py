import discord
from discord.ui import View, Select, Button
from funktionen.inv_interface import add_item, remove_item, get_inventory
from funktionen.choose_Views import choose_Views
from funktionen.choose_Embeds import choose_Embeds


class StockBuyView(View):
    def __init__(self, ticker_symbol: str, author_id: int, value: int):
        super().__init__(timeout=60)
        self.ticker = ticker_symbol
        self.author_id = author_id
        self.price = value
        self.amount: float | None = None

        self.add_item(AmountSelect(self))
        self.add_item(ConfirmBuy(self))
        self.add_item(BackButton(self))


class AmountSelect(Select):
    def __init__(self, view: StockBuyView):
        self.view_ref = view
        super().__init__(
            placeholder="Select amount",
            options=[
                discord.SelectOption(label="0.1", value="0.1"),
                discord.SelectOption(label="0.5", value="0.5"),
                discord.SelectOption(label="1", value="1"),
                discord.SelectOption(label="5", value="5"),
            ],
        )

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.view_ref.author_id:
            return await interaction.response.send_message("❌ Not for you", ephemeral=True)
        self.view_ref.amount = float(self.values[0])
        await interaction.response.send_message(
            f"Selected {self.view_ref.amount}", ephemeral=True
        )


class ConfirmBuy(Button):
    def __init__(self, view: StockBuyView):
        self.view_ref = view
        super().__init__(label="Buy", style=discord.ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        if self.view_ref.amount is None:
            return await interaction.response.send_message("Select amount first", ephemeral=True)

        cost = self.view_ref.amount * self.view_ref.price
        coins = get_inventory(interaction.user.id, "MandoCoins")

        if cost > coins:
            return await interaction.response.send_message("❌ Not enough coins", ephemeral=True)

        remove_item(interaction.user.id, "MandoCoins", cost)
        add_item(interaction.user.id, self.view_ref.ticker, self.view_ref.amount, category="stock")

        await interaction.response.send_message(
            f"✅ Bought {self.view_ref.amount} {self.view_ref.ticker}",
            ephemeral=True
        )


class BackButton(Button):
    def __init__(self, view):
        super().__init__(label="Back", style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.Interaction):
        embed = await choose_Embeds("stockmarket")
        view = await choose_Views("stock_page_1")
        await interaction.response.edit_message(embed=embed, view=view)
