import discord
from discord.ui import View
from funktionen.choose_Views import choose_Views
from funktionen.choose_Embeds import choose_Embeds


class stockm_p1(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="← Back", style=discord.ButtonStyle.red)
    async def back(self, interaction: discord.Interaction, _):
        view = await choose_Views("Stockmarket_main")
        embed = await choose_Embeds("Stockmarket_main")
        await interaction.response.edit_message(view=view)
    
    
    @discord.ui.button(label="Apple (AAPL)", style=discord.ButtonStyle.blurple)
    async def aapl(self, interaction: discord.Interactions):
        embed = await choose_Embeds("stock", ticker_symbol="AAPL")
        view = await choose_Views(
            "stock",
            ticker_symbol="AAPL",
            author_id=interaction.user.id,
        )
        await interaction.response.edit_message(embed=embed, view=view)
    
    @discord.ui.button(label="Tesla (TSLA)", style=discord.ButtonStyle.blurple)
    async def tsla(self, interaction: discord.Interactions):
        embed = await choose_Embeds("stock", ticker_symbol="TSLA")
        view = await choose_Views(
            "stock",
            ticker_symbol="TSLA",
            author_id=interaction.user.id,
        )
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label="Microsoft (MSFT)", style=discord.ButtonStyle.blurple)
    async def msft(self, interaction: discord.Interactions):
        embed = await choose_Embeds("stock", ticker_symbol="MSFT")
        view = await choose_Views(
            "stock",
            ticker_symbol="MSFT",
            author_id=interaction.user.id,
        )
        await interaction.response.edit_message(embed=embed, view=view)
    
    
    @discord.ui.button(label="Next →", style=discord.ButtonStyle.green)
    async def next_page(self, interaction: discord.Interaction, _):
        view = await choose_Views("stock_page_2")
        await interaction.response.edit_message(view=view)
