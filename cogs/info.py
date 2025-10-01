import discord
from discord.ext import commands

from funktionen.choose_Embeds import choose_Embeds


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["Help", "HELP", "info", "Info", "INFO"])
    async def help_command(self, ctx, *, arg=None):
        embed = await choose_Embeds("help_erstellen", user=str(ctx.author.id), arg=arg)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))
