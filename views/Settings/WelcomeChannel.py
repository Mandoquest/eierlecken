import discord

from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views
from funktionen.check_admin import AuthorView
from datenbanken.welcome_channel_datenbank import set_welcome_channel

class ChannelSelect(discord.ui.ChannelSelect):
    def __init__(self, author_id: int):
        self.author_id = author_id
        super().__init__(
            placeholder="Kanal für Willkommensnachrichten wählen",
            min_values=1,
            max_values=1,
            channel_types=[discord.ChannelType.text],
        )

    async def callback(self, interaction: discord.Interaction):
        selected_channel = self.values[0]
        guild_id = interaction.guild.id
        channel_id = selected_channel.id
        set_welcome_channel(guild_id, channel_id)
        embed= await choose_Embeds("Welcome_channel", guild=interaction.guild)
        view= choose_Views("Welcome_channel", author_id=self.author_id)
        await interaction.response.edit_message(view=view, embed=embed)


class WelcomeChannel_View(AuthorView):
    def __init__(self, author_id: int):
        super().__init__(timeout=None, author_id = author_id)
        
        self.add_item(ChannelSelect(author_id)) 

    @discord.ui.button(label="Back", style=discord.ButtonStyle.primary, emoji="◀️", row=1)
    async def back_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = await choose_Embeds("Main", guild=interaction.guild)
        view = choose_Views("Main", author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)
    @discord.ui.button(label="delete", style=discord.ButtonStyle.danger, emoji="❌", row=1)
    async def delete_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        set_welcome_channel(interaction.guild.id, None)  
            
        embed= await choose_Embeds("Welcome_channel", guild=interaction.guild)
        view= choose_Views("Welcome_channel", author_id=self.author_id)
        await interaction.response.edit_message(view=view, embed=embed)