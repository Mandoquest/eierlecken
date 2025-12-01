import discord
from discord.ui import View, Button


class Test(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Test Button", style=discord.ButtonStyle.primary)
    async def test_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "Du hast den Test Button gedrückt!", ephemeral=True
        )
