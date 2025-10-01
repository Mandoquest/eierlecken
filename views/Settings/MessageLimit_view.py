import discord 


from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views
from funktionen.check_admin import AuthorView
from funktionen.antispam_bank import set_message_limit


class MessageLimitButtons(discord.ui.View):
    def __init__(self, author_id):
        super().__init__(timeout=None)
        self.author_id = author_id

    @discord.ui.button(label="Back", style=discord.ButtonStyle.primary, emoji="◀️")
    async def first_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = await choose_Embeds("Main", guild=interaction.guild)
        view = choose_Views("Main", author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label="Light", style=discord.ButtonStyle.primary, emoji="🔹")
    async def second_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        set_message_limit(interaction.guild.id, "leicht")
        await interaction.response.send_message("Message limit set to Light: **10 messages every 15 seconds**.", ephemeral=True)

    @discord.ui.button(label='Medium (Recommended)', style=discord.ButtonStyle.primary, emoji="🔸")
    async def third_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        set_message_limit(interaction.guild.id, "mittel")
        await interaction.response.send_message("Message limit set to Medium: 5 messages every 10 seconds.", ephemeral=True)

    @discord.ui.button(label="Strict", style=discord.ButtonStyle.primary, emoji="🔴")
    async def fourth_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        set_message_limit(interaction.guild.id, "stark")
        await interaction.response.send_message("Message limit set to Light: **3 messages every 5 seconds**.", ephemeral=True)

    @discord.ui.button(label="disable", style=discord.ButtonStyle.danger, emoji="❌")
    async def fifth_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        set_message_limit(interaction.guild.id, "aus")
        await interaction.response.send_message("Message limit disabled.", ephemeral=True)