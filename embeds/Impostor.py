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


def Impostor_end(players, **kwargs) -> discord.Embed:
    """Embed shown after all players confirmed and roles/words were sent.

    - Accepts `players` as a list of member objects or mention strings.
    - Does NOT reveal the impostor or the secret word (they were DM'd).
    """
    if isinstance(players, list):
        # accept discord.Member or mention strings
        try:
            players_list = [p.mention if hasattr(p, "mention") else str(p) for p in players]
        except Exception:
            players_list = [str(p) for p in players]
        players_str = "\n".join(players_list)
    else:
        players_str = str(players)

    embed = discord.Embed(
        title="🕵️ Impostor — Spiel gestartet",
        colour=0x00ff00,
        description=(
            "Alle Spieler haben bestätigt und die Rollen/Wörter wurden per DM verschickt.\n"
            "Das Impostor bleibt geheim — viel Spaß beim Spielen!"
        )
    )

    embed.add_field(name="👥 Spieler", value=players_str or "Keine Spieler", inline=False)
    embed.add_field(name="📬 Check DMs", value="Jeder Spieler wurde per DM informiert. Das Spiel läuft nun!", inline=False)
    embed.set_footer(text="Am Ende des Spiels könnt ihr den Impostor aufdecken bzw. abstimmen.")
    return embed