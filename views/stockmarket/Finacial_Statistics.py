import discord 
from funktionen.protectetview import ProtectedView
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views

class FinancialStatisticsView(ProtectedView):
    def __init__(self, author_id):
        super().__init__(author_id, timeout=None)

    @discord.ui.button(label="back", style=discord.ButtonStyle.red, emoji="📊")
    async def portfolio_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed =  await choose_Embeds("stockmarket_main")
        view = await choose_Views("stockmarket_main", author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)

