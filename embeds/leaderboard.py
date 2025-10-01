import discord
from datenbanken.datenbanken_test import _konten


async def leaderboard_erstellen(top, user, bot=None):
    top = str(top)

    if top == "10":
        embed = discord.Embed(
            title="🏆 Leaderboard - Top 10",
            description="Here are the top 10 users with the highest scores:",
            color=0xFFD700,
        )
        for platz, uid, guthaben in leaderboard(seite=1, pro_seite=10):
            username = await fetch_username(uid, bot)
            embed.add_field(
                name=f"{platz}. {username}",
                value=f"Score: {guthaben}",
                inline=False,
            )
        return embed
    elif top == "20":
        embed = discord.Embed(
            title="🏆 Leaderboard - Top 20",
            description="Here are the top 20 users with the highest scores:",
            color=0xC0C0C0,
        )
        for platz, uid, guthaben in leaderboard(seite=1, pro_seite=20):
            username = await fetch_username(uid, bot)
            embed.add_field(
                name=f"{platz}. {username}",
                value=f"Score: {guthaben}",
                inline=False,
            )
        return embed
    else:
        embed = discord.Embed(
            title="Leaderboard",
            description="Ungültige Top-Auswahl.",
            color=0xFF0000,
        )
        return embed


async def fetch_username(user_id, bot):
    try:
        user = await bot.fetch_user(int(user_id))
        return user.name
    except Exception:
        return f"User {user_id}"


def leaderboard(seite=1, pro_seite=10):
    sortierte_konten = sorted(_konten.items(), key=lambda x: (-x[1], x[0]))

    rangliste = []
    rang = 1
    letzter_score = None

    for i, (uid, guthaben) in enumerate(sortierte_konten, start=1):
        if guthaben != letzter_score:
            rang = i
            letzter_score = guthaben
        rangliste.append((rang, uid, guthaben))

    # Bereich für die gewünschte Seite berechnen
    start = (seite - 1) * pro_seite
    ende = start + pro_seite

    return rangliste[start:ende]
