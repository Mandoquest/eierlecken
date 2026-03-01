import discord
from discord.ext import commands
import aiohttp
import uuid
from datenbanken.aktive_Spiele import aktive_spiele
from views.blackjack_view import BlackjackView
from embeds.blackjack_embed import erstelle_start_embed
from funktionen.utils import zahlen_verkleinern
from funktionen.inv_interface import get_inventory, remove_item


class BlackJack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Blackjack.py geladen")

    @commands.command(name="blackjack", aliases=["Blackjack", "gamble", "Gamble"])
    async def blackjack(self, ctx, einsatz="100"):
        user_id = ctx.author.id
        if einsatz == "all":
            einsatz = get_inventory(user_id, "MandoCoins")
        else:
            einsatz = int(einsatz)
        if einsatz <= 0:
            await ctx.send("❌ The bet must be greater than 0.")
            return
        if user_id in [spiel["user_id"] for spiel in aktive_spiele.values()]:
            await ctx.send("❌ You already have an active game.")
            return
        if get_inventory(user_id, "MandoCoins") < einsatz:
            await ctx.send("❌ You don't have enough coins.")
            return

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
                ) as resp:
                    deck_id = (await resp.json())["deck_id"]
                async with session.get(
                    f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=3"
                ) as resp:
                    cards = (await resp.json())["cards"]
                    player_cards = [cards[0]]
                    dealer_cards = [cards[1]]
        except Exception as e:
            await ctx.send(f"❌ Error starting game: {str(e)}")
            return

        remove_item(user_id, "MandoCoins", einsatz)

        spiel_id = str(uuid.uuid4())[:8]
        view = BlackjackView(
            user_id, deck_id, player_cards, dealer_cards, einsatz, spiel_id
        )

        aktive_spiele[spiel_id] = {
            "user_id": user_id,
            "view": view,
            "aktion_laeuft": False,
        }

        embed = await erstelle_start_embed(
            ctx.author, spiel_id, einsatz, player_cards
        )
        await ctx.send(embed=embed, view=view)

    @commands.command(name="balance", aliases=["bal", "Bal", "Balance", "b", "B"])
    async def balance(self, ctx):
        print (f"Checking balance for user {ctx.author.id}")
        stand = get_inventory(ctx.author.id, "MandoCoins")
        print(f"Raw balance: {stand}")
        Konto = zahlen_verkleinern(stand)
        print(f"Formatted balance: {Konto}")
        await ctx.send(f"💰 Your Balance: **{Konto} MandoCoins**")


async def setup(bot):
    await bot.add_cog(BlackJack(bot))
