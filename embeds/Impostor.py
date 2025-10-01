import discord

def impostor_game(players, author=None, **kwargs) -> discord.Embed:
    if isinstance(players, list):
        players_str = "\n".join(players)
    else:
        players_str = str(players)
    embed = discord.Embed(
        title="🕵️ Impostor Game – Lobby",
        colour=0xff0000,
        description=(
            "Welcome to the **Impostor Game**!\n"
            "All players must confirm before the game can begin.\n"
        )
    )
    if author:
        embed.set_author(name=f"Game started by {author}")

    embed.add_field(
        name="👥 Players",
        value=players_str,
        inline=False
    )

    embed.add_field(
        name="✅ Confirmed",
        value="No players confirmed yet.",
        inline=True
    )

    embed.add_field(
        name="❌ Not Confirmed",
        value=players_str,
        inline=True
    )

    embed.add_field(
        name="📖 How to Play",
        value=(
            "- One player will secretly be the **Impostor**.\n"
            "- All others receive the same secret word via DM.\n"
            "- The Impostor does **not** get the word.\n"
            "- Each player must describe the word *without saying it*.\n"
            "- At the end, vote who you think the Impostor is.\n"
            "- The Impostor can then try to guess the word."
        ),
        inline=False
    )

    embed.set_footer(text="Click the ✅ Confirm button to join the game.")
    return embed




def edit_impostor(players, confirmed=None, author=None, **kwargs) -> discord.Embed:

    if confirmed is None:
        confirmed = []

    if isinstance(players, list):
        players_str = "\n".join(players)
    else:
        players_str = str(players)

    if isinstance(confirmed, (set, list)):
        confirmed_str = "\n".join(confirmed) if confirmed else "No players confirmed yet."
    else:
        confirmed_str = str(confirmed)

    # Not confirmed = players not in confirmed
    not_confirmed = [p for p in players if p not in confirmed]
    not_confirmed_str = "\n".join(not_confirmed) if not_confirmed else "All players confirmed!"

    embed = discord.Embed(
        title="🕵️ Impostor Game – Lobby",
        colour=0xff0000,
        description=(
            "Welcome to the **Impostor Game**!\n"
            "All players must confirm before the game can begin.\n"
        )
    )
    if author:
        embed.set_author(name=f"Game started by {author}")

    embed.add_field(
        name="👥 Players",
        value=players_str,
        inline=False
    )

    embed.add_field(
        name="✅ Confirmed",
        value=confirmed_str,
        inline=True
    )
    
    embed.add_field(
        name="❌ Not Confirmed",
        value=not_confirmed_str,
        inline=True
    )

    embed.add_field(
        name="📖 How to Play",
        value=(
            "- One player will secretly be the **Impostor**.\n"
            "- All others receive the same secret word via DM.\n"
            "- The Impostor does **not** get the word.\n"
            "- Each player must describe the word *without saying it*.\n"
            "- At the end, vote who you think the Impostor is.\n"
            "- The Impostor can then try to guess the word."
        ),
        inline=False
    )

    embed.set_footer(text="Click the ✅ Confirm button to join the game.")
    return embed