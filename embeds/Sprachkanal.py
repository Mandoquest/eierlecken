import discord
from datenbanken.Sprachkanäle import get_channel


async def Sprachkanal(**kwargs):

    guild = kwargs.get("Guild")
    print(f"Guild ID for Voice Channel Embed: {guild}")

    if guild is None:
        raise ValueError("Guild ID is required for the voice channel embed.")

    channel_id = get_channel(guild.id)
    print(f"Channel ID for Voice Channel Embed: {channel_id}")

    embed = discord.Embed(
        title="🎤 Voice Channel Information",
        description=(
            "Manage and view details about your personal voice channel here.\n"
            "Use the buttons below to create or customize your channel."
        ),
        color=discord.Color.blue(),
    )
    print(channel_id)
    if channel_id is None:
        embed.add_field(
            name="🔇 Current Voice Channel",
            value=(
                "There is currently **no voice channel**.\n"
                "👉 Click **Create** below to generate a new one."
            ),
            inline=False,
        )
    elif channel_id is not None:
        embed.add_field(
            name="🔊 Current Voice Channel",
            value=f"The active voice channel is:\n➡️ <#{channel_id}>",
            inline=False,
        )
    embed.set_footer(text="Voice Channel System • powered by MandoBot 🤖")
    embed.timestamp = discord.utils.utcnow()

    return embed
