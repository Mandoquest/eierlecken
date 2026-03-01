import discord 
from funktionen.protectetview import ProtectedView
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views

class YourPortfolio(ProtectedView):
    def __init__(self, author_id):
        super().__init__(timeout=None)
        self.author_id = author_id

    @discord.ui.button(label="back", style=discord.ButtonStyle.red, emoji="📊")
    async def portfolio_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed =  await choose_Embeds("stockmarket_main")
        view = choose_Views("stockmarket_main")
        await interaction.response.edit_message(embed=embed, view=view)