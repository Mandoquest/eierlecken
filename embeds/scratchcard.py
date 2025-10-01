import discord
import random
from datenbanken.datenbanken_test import ändere_guthaben


def scratchcard_erstellen(user: int):
    gewinnstufen = [
        ("<:diamond:1414017424398745731>", 25000, 0.1),
        ("<:blank:1414045339320582254>❌<:blank:1414045339320582254>", 0, 20),
        (
            "<:blank:1414045339320582254><:coin:1414017451875893249><:blank:1414045339320582254>",
            2800,
            38,
        ),
        (
            "<:blank:1414045339320582254><:banknote:1414021458166026290><:blank:1414045339320582254>",
            3300,
            25,
        ),
        (
            "<:blank:1414045339320582254><:coinstack:1414017436289601637><:blank:1414045339320582254>",
            3500,
            10.9,
        ),
    ]

    rnd = random.uniform(0, 100)
    kumulativ = 0
    symbol, gewinn = None, 0

    for s, coins, chance in gewinnstufen:
        kumulativ += chance
        if rnd <= kumulativ:
            symbol, gewinn = s, coins
            break

    alle_symbole = [
        "<:blank:1414045339320582254>❌<:blank:1414045339320582254>",
        "<:blank:1414045339320582254><:coin:1414017451875893249><:blank:1414045339320582254>",
        "<:blank:1414045339320582254><:banknote:1414021458166026290><:blank:1414045339320582254>",
        "<:blank:1414045339320582254><:coinstack:1414017436289601637><:blank:1414045339320582254>",
    ]
    grid = []
    for _ in range(9):
        grid.append(random.choice(alle_symbole))
    grid[random.randint(0, 8)] = symbol
    grid = [f"||{e}||" for e in grid]
    reihen = [grid[i : i + 3] for i in range(0, 9, 3)]
    matrix = "\n".join(" ".join(r) for r in reihen)
    if gewinn > 0:
        ändere_guthaben(user, gewinn)
        print(f"User {user} won {gewinn} coins")
    embed = discord.Embed(
        title="🎟️ scratchcard",
        description="good luck! \n\n" + matrix,
        color=discord.Color.gold(),
    )
    embed.set_footer(text="!info scratchcard to see values")
    return embed


def info_scratchpad():
    embed = discord.Embed(
        title="🎟️ scratchcard info",
        description=(
            "**possible Items:**\n"
            "<:diamond:1414017424398745731> 25,000 coins (00.1% chance)\n"
            "❌ Rivet (20% chance)\n"
            "<:coin:1414017451875893249> 575 coins (38% chance)\n"
            "<:banknote:1414021458166026290> 800 coins (25% chance)\n"
            "<:coinstack:1414017436289601637> 1,000 coins (10.9% chance)\n\n"
            "**costs:** 5000 coins per scratchcard\n"
            "**How does it work:**\n"
            "Buy a scratchcard (!scratchcard) and try your luck!\n"
            "Good luck!"
        ),
        color=discord.Color.blue(),
    )
    return embed
