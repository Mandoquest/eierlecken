import discord
from discord.ext import commands
from funktionen.choose_Embeds import choose_Embeds
from datenbanken.cooldowns import (
    check_cooldown,
    load_cooldowns,
    update_cooldown,
    save_cooldowns,
)
from funktionen.inv_interface import get_inventory, add_item
from funktionen.sekunden_in_stunden import sekunden_in_stunden
import random
from funktionen.utils import zahlen_verkleinern


class Cd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("CD.py geladen")

    @commands.command()
    async def cd(self, ctx):
        print(f"{ctx.author} used cd command")
        embed =  await choose_Embeds("cd", user=str(ctx.author.id))
        print("Embed created, sending message")

        await ctx.send(embed=embed)
        print(f"Sent cooldown message to user {ctx.author.id}")

    @commands.command()
    async def reset(self, ctx):
        user_id = str(ctx.author.id)
        load_cooldowns()
        cooldowns = load_cooldowns()
        if ctx.author.guild_permissions.administrator:
            if user_id in cooldowns:
                del cooldowns[user_id]
                save_cooldowns(cooldowns)
                await ctx.send("✅ All cooldowns reseted.")
        else:
            await ctx.send("❌ You need to be an Administrator to use this command.")

    @commands.command()
    async def daily(self, ctx):
        print(f"{ctx.author} used daily command")
        user_id = str(ctx.author.id)
        print("user_id:", user_id)
        rest = check_cooldown(user_id, "daily", 86400)
        print("rest:", rest)
        if rest > 0:
            print("User is on cooldown")
            embed =  await choose_Embeds("cooldown_n_ready", rest=rest)
            await ctx.send(embed=embed)
        else:
            print("User is not on cooldown, giving reward")
            update_cooldown(user_id, "daily")
            print("Cooldown updated, giving reward")
            coins = random.randint(500, 1500)
            print(f"Generated coins: {coins}")
            add_item(user_id, "MandoCoins", coins)
            print(f"Added {coins} MandoCoins to user {user_id}")
            neues_guthaben = get_inventory(user_id, "MandoCoins")
            neues_guthaben = zahlen_verkleinern(neues_guthaben)
            print(f"User {user_id} now has {neues_guthaben} MandoCoins")

            await ctx.send(
                f"🎉 You got {coins}coins. You have {neues_guthaben} coins now"
            )
            print(f"Sent message to user {user_id} about daily reward")


async def setup(bot):
    await bot.add_cog(Cd(bot))
