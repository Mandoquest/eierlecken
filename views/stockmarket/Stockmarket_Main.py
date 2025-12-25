import discord
from discord.ui import View, Button
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


class Stockmarket_Main(View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)

    @discord.ui.button(
        label="Stockmarket",
        style=discord.ButtonStyle.blurple,
        emoji="🔍",
        custom_id="Market Overview",
    )
    async def stockmarket_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        embed = await choose_Embeds("stockm_p1")
        view = await choose_Views("stockm_p1")
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(
        label="Your Portfolio",
        style=discord.ButtonStyle.blurple,
        emoji="💼",
        custom_id="Your Portfolio",
    )
    async def your_stocks_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        embed = await choose_Embeds("your_portfolio", author_id=interaction.user.id)
        # view = await choose_Views("your_portfolio", author_id=interaction.user.id)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(
        label="Financial Statistics",
        style=discord.ButtonStyle.blurple,
        emoji="📊",
        custom_id="Finacial Statistics",
    )
    async def Fincancial_statistics_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        embed = await choose_Embeds(
            "Fincancial_statistics", author_id=interaction.user.id
        )
        view = await choose_Views(
            "Fincancial_statistics", author_id=interaction.user.id
        )
        await interaction.response.edit_message(embed=embed, view=view)
