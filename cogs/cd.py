import discord
from discord.ext import commands
from funktionen.choose_Embeds import choose_Embeds
from datenbanken.cooldowns import (
    check_cooldown,
    load_cooldowns,
    update_cooldown,
    save_cooldowns,
)
from embeds.cd import erstelle_cd_embed
from datenbanken.datenbanken_test import ändere_guthaben, gib_guthaben
from funktionen.sekunden_in_stunden import sekunden_in_stunden
import random


class Cd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cd(self, ctx):
        embed = await choose_Embeds("cd", user=str(ctx.author.id))

        await ctx.send(embed=embed)

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
        user_id = str(ctx.author.id)
        rest = check_cooldown(user_id, "daily", 86400)
        print(rest)
        if rest > 0:
            embed = await choose_Embeds("cooldown_n_ready", user_id=user_id, rest=rest)
            Zeit = sekunden_in_stunden(rest)
            await ctx.send(embed=embed)
        else:
            update_cooldown(user_id, "daily")
            coins = random.randint(500, 1500)
            ändere_guthaben(user_id, coins)
            neues_guthaben = gib_guthaben(user_id)
            await ctx.send(
                f"🎉 You got {coins}coins. You have {neues_guthaben} coins now"
            )


async def setup(bot):
    await bot.add_cog(Cd(bot))
