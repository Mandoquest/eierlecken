import discord
import os
from funktionen.inv_interface import get_inventory


async def leaderboard_erstellen(top, user, bot=None):
    """Erstellt ein Leaderboard basierend auf den MandoCoins in der Spieler‑Inventur.

    *top* kann "10" oder "20" sein. Der *user*-Parameter wird nur für die
    Button-View-Validierung weitergegeben.
    """

    top = str(top)

    # alle Spielerdateien durchgehen, Guthaben auslesen
    balances: list[tuple[str, int]] = []
    player_folder = os.path.join("player_data")
    if os.path.isdir(player_folder):
        for fname in os.listdir(player_folder):
            if not fname.endswith(".json"):
                continue
            uid = fname[:-5]
            amt = get_inventory(uid, "MandoCoins")
            # get_inventory kann ein dict zurückgeben, deswegen absichern
            if isinstance(amt, dict):
                amt = amt.get("amount", 0)
            try:
                amt = int(amt)
            except Exception:
                amt = 0
            balances.append((uid, amt))

    # nach Guthaben absteigend sortieren und gleiche Werte als gleichrangig behandeln
    balances.sort(key=lambda x: (-x[1], x[0]))
    ranked: list[tuple[int, str, int]] = []
    last_amount = None
    rank = 0
    for idx, (uid, amt) in enumerate(balances, start=1):
        if amt != last_amount:
            rank = idx
            last_amount = amt
        ranked.append((rank, uid, amt))

    async def build_embed(title, color):
        description = "Here are the users with the highest MandoCoins balances."
        if top == "20":
            description = "Here are the top 20 users with the highest MandoCoins balances."
        embed = discord.Embed(title=title, description=description, color=color)
        limit = int(top) if top in ("10", "20") else 0
        for platz, uid, amt in ranked[:limit]:
            username = await fetch_username(uid, bot)
            mention = f"<@{uid}>"          # zeigt @-Erwähnung an
            embed.add_field(
                name=f"{platz}. {mention} ({username})",
                value=f"Score: {amt}",
                inline=False,
            )
        return embed

    # optional footer with die eigene Position
    async def add_user_footer(embed):
        try:
            # ranked list contains tuples (rank, uid, amt)
            entry = next((r, a) for r, u, a in ranked if u == user)
            embed.set_footer(text=f"Dein Rang: {entry[0]} mit {entry[1]} MandoCoins")
        except StopIteration:
            # user not in ranking (maybe gibts kein Guthaben)
            pass
        return embed

    if top == "10":
        emb = await build_embed("🏆 Leaderboard - Top 10", 0xFFD700)
        return await add_user_footer(emb)
    elif top == "20":
        emb = await build_embed("🏆 Leaderboard - Top 20", 0xC0C0C0)
        return await add_user_footer(emb)
    else:
        return discord.Embed(
            title="Leaderboard",
            description="Ungültige Top-Auswahl.",
            color=0xFF0000,
        )


async def fetch_username(user_id, bot):
    """Versucht zuerst, im Cache zu finden, ansonsten über API abzurufen."""
    try:
        if bot is not None:
            user = bot.get_user(int(user_id))
            if user is None:
                user = await bot.fetch_user(int(user_id))
            return user.name
        else:
            return f"User {user_id}"
    except Exception:
        return f"User {user_id}"
