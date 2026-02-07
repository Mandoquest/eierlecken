import discord

def create_embed():

    embed = discord.Embed(
        title="Test",
        description="👉 [Website besuchen](https://example.com)"
    )

    embed.set_author(
        name="Meine Website",
        url="https://example.com"
    )
    embed.add_field(
        name="Links",
        value="[Website](https://example.com)",
        inline=False
    )
    return embed