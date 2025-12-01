import discord
from discord.ext import commands

from funktionen.choose_Embeds import choose_Embeds
from datenbanken.datenbanken_test import ändere_guthaben, gib_guthaben
from datenbanken.cooldowns import check_cooldown, update_cooldown
from funktionen.inv_interface import add_item, get_inventory, remove_item


class Scratchcard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("scratchcard.py geladen")

    @commands.command()
    async def scratchcard(self, ctx):
        print("Command received")
        guthaben = get_inventory(ctx.author.id, "MandoCoins")
        print("Guthaben:", guthaben)
        if guthaben < 5000:
            await ctx.send("You need at least 5000 coins to buy a scratch card.")
            return

        rest = check_cooldown(str(ctx.author.id), "rubbellos", 36000)
        print("Cooldown:", rest)
        if rest > 0:
            embed = await choose_Embeds(
                "cooldown_n_ready", user_id=str(ctx.author.id), rest=rest
            )
            await ctx.send(embed=embed)
            return

        update_cooldown(str(ctx.author.id), "rubbellos")
        remove_item(ctx.author.id, "MandoCoins", 5000)

        embed = await choose_Embeds("scratchcard_erstellen", user=ctx.author.id)

        await ctx.send("test")


async def setup(bot):
    await bot.add_cog(Scratchcard(bot))
