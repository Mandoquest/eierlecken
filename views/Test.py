import discord 

class TestView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Klicke mich!", style=discord.ButtonStyle.primary, custom_id="test_button")
    async def test_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Du hast den Test-Button geklickt!", ephemeral=True)