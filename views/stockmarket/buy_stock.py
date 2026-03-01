import discord
from discord.ui import View, Select, Button
from funktionen.inv_interface import add_item, remove_item, get_inventory
from funktionen.choose_Views import choose_Views
from funktionen.choose_Embeds import choose_Embeds
from funktionen.protectetview import ProtectedView


class StockBuyView(ProtectedView):
    def __init__(self, ticker_symbol: str, author_id: int, value: float = 0.0):
        super().__init__(author_id, timeout=60)
        self.ticker = ticker_symbol
        self.author_id = author_id
        self.price: float = float(value)
        self.amount: float | None = None

        self.add_item(AmountSelect(self))
        self.add_item(BackButton(self))
        self.add_item(ConfirmBuy(self))


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
        print("ConfirmBuy button clicked")
        if self.view_ref.amount is None:
            print("No amount selected")
            return await interaction.response.send_message("Select amount first", ephemeral=True)

        if self.view_ref.price <= 0:
            print("Price unavailable or zero")
            return await interaction.response.send_message("❌ Stock price unavailable — try again later", ephemeral=True)

        cost = self.view_ref.amount * self.view_ref.price
        print(f"Calculated cost: {cost} MandoCoins for {self.view_ref.amount} {self.view_ref.ticker} at price {self.view_ref.price} MandoCoins each")

        coins = get_inventory(interaction.user.id, "MandoCoins")
        print(f"User has {coins} MandoCoins")

        if cost > coins:
            print("Not enough coins")
            return await interaction.response.send_message("❌ Not enough coins", ephemeral=True)

        print("Proceeding with purchase")
        remove_item(interaction.user.id, "MandoCoins", cost)
        print(f"Removed {cost} MandoCoins from user inventory")
        add_item(interaction.user.id, self.view_ref.ticker, self.view_ref.amount, category="stock")
        print(f"Added {self.view_ref.amount} {self.view_ref.ticker} to user inventory")

        # Disable buy/select controls so user cannot accidentally repurchase,
        # but keep the Back button enabled so navigation still works.
        for child in self.view_ref.children:
            # disable dropdown and the buy button only
            if isinstance(child, Select) or (isinstance(child, Button) and child.label == "Buy"):
                child.disabled = True

        # apply the updated view state to the original message
        try:
            await interaction.message.edit(view=self.view_ref)
        except Exception as e:
            print("Failed to edit message after purchase:", e)

        await interaction.response.send_message(
            f"✅ Bought {self.view_ref.amount} {self.view_ref.ticker}",
            ephemeral=True,
        )

        print("--------------------------------Purchase completed----------------------------------------------------------------")

class BackButton(Button):
    def __init__(self, view: StockBuyView):
        self.view_ref = view
        super().__init__(label="← Back", style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.Interaction):
        print("Back button clicked")
        view = await choose_Views("stockmarket_main", author_id=self.view_ref.author_id)
        print("View for stockmarket_main created")
        embed = await choose_Embeds("stockmarket_main")
        print("Embed for stockmarket_main created")
        await interaction.response.edit_message(embed=embed, view=view)
        print("Message edited to stockmarket_main")