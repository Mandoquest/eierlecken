import discord
from datenbanken.cooldowns import check_cooldown
import time


async def erstelle_cd_embed(user):
    print("cd embed erstellen angefangen")

    # Cooldowns abfragen (Rückgabe: Restzeit in Sekunden)
    rest_daily = check_cooldown(user, "daily", 86400)
    rest_rubbellos = check_cooldown(user, "rubbellos", 36000)

    # Unix-Timestamps für Discord <t:...> berechnen
    cooldown_daily_ende = int(time.time() + rest_daily)
    cooldown_rubbellos_ende = int(time.time() + rest_rubbellos)

    # Embed erstellen
    embed = discord.Embed(title="⏳ Cooldowns")

    # Rubbellos
    if rest_rubbellos > 0:
        embed.add_field(
            name="",
            value=f"`!scratchcard`<a:typing:1410736488915669124> <t:{cooldown_rubbellos_ende}:R>",
            inline=False,
        )
    else:
        embed.add_field(name="", value="`!scratchcard` ✅", inline=False)

    # Daily
    if rest_daily > 0:
        embed.add_field(
            name="",
            value=f"`!daily` <a:typing:1410736488915669124> <t:{cooldown_daily_ende}:R>",
            inline=False,
        )
    else:
        embed.add_field(name="", value="`!daily` ✅", inline=False)

    return embed


def erstelle_cd_n_ready(user_id, rest):
    cooldown_ende = int(time.time() + rest)

    embed = discord.Embed(
        title="⏳ Cooldown aktiv",
        description=(f"the command is on cooldown. Please wait <t:{cooldown_ende}:R>."),
        color=discord.Color.red(),
    )
    return embed
