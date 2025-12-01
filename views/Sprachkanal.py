import discord
from discord.ui import View, Button
from datenbanken.Sprachkanäle import get_channel, set_channel
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


def Sprachkanal_Buttons(**kwargs):
    guild: discord.Guild = kwargs.get("Guild")
    channel_id = get_channel(guild.id)

    if channel_id is None:

        class SprachkanalView(View):
            def __init__(self):
                super().__init__(timeout=None)

            @discord.ui.button(
                label="Create Voice Channel",
                style=discord.ButtonStyle.success,
                emoji="➕",
            )
            async def create_vc(self, interaction: discord.Interaction, button: Button):
                guild = interaction.guild
                vc = await guild.create_voice_channel(name=f"Create Voice Channel")
                set_channel(guild.id, vc.id)
                embed = await choose_Embeds("Sprachkanal", Guild=guild)
                view = choose_Views("Sprachkanal", Guild=guild)
                await interaction.response.edit_message(embed=embed, view=view)

        return SprachkanalView()
    elif channel_id is not None:

        class SprachkanalView(View):
            def __init__(self):
                super().__init__(timeout=None)

            @discord.ui.button(
                label="Delete Voice Channel",
                style=discord.ButtonStyle.danger,
                emoji="🗑️",
            )
            async def delete_vc(self, interaction: discord.Interaction, button: Button):
                guild_obj = interaction.guild
                channel = guild_obj.get_channel(channel_id)
                await channel.delete()
                set_channel(guild_obj.id, None)
                embed = await choose_Embeds("Sprachkanal", Guild=guild_obj)
                view = choose_Views("Sprachkanal", Guild=guild_obj)
                await interaction.response.edit_message(embed=embed, view=view)

        return SprachkanalView()
