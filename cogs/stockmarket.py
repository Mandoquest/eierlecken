import discord
from discord.ext import commands
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


class StockMarket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stock", aliases=["Stock", "stocks", "Stocks"])
    async def stock(self, ctx):
        embed = await choose_Embeds("stockmarket")
        view = await choose_Views("stockmarket")
        await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(StockMarket(bot))
