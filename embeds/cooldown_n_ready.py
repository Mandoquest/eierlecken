import discord 
import time

async def create_embed(rest):
    timestamp = int(time.time()) + rest
    discord_timestamp = f"<t:{timestamp}:R>"
    embed = discord.Embed(title="Cooldown", description=f"You are on cooldown until {discord_timestamp}")
    return embed