import discord
from discord.ext import commands
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


class StockMarket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("StockMarket.py geladen")

    @commands.command(name="stock", aliases=["Stock", "stocks", "Stocks"])
    async def stock(self, ctx):
        print(f"{ctx.author} used stock command")
        embed =  await choose_Embeds("stockmarket_main")
        print("Embed created, creating view")
        view = await choose_Views("stockmarket_main", author_id=ctx.author.id)
        print("View created, sending message")
        await ctx.send(embed=embed, view=view)
        print(f"Sent stock market message to user {ctx.author.id}")


async def setup(bot):
    await bot.add_cog(StockMarket(bot))
