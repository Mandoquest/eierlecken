import discord
from discord.ext import commands

from funktionen.choose_Embeds import choose_Embeds
from datenbanken.cooldowns import check_cooldown, update_cooldown
from funktionen.inv_interface import get_inventory, remove_item


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
            print("User is on cooldown")
            embed =  await choose_Embeds(
                "cooldown_n_ready", rest=rest
            )
            await ctx.send(embed=embed)
            return
        print("User can buy scratch card, updating cooldown and removing coins")
        update_cooldown(str(ctx.author.id), "rubbellos")
        print("Cooldown updated, removing coins")
        remove_item(ctx.author.id, "MandoCoins", 5000)
        print("Coins removed, creating embed")

        embed =  await choose_Embeds("scratchcard_erstellen", user=ctx.author.id)
        print("Embed created, sending message")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Scratchcard(bot))
