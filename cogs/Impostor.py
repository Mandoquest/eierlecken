import discord
from discord.ext import commands

from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


class Impostor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def impostor(self, ctx, *players: discord.Member):
        players = list(players)
        if ctx.author not in players:
            players.insert(0, ctx.author)  # Add author at the start
        if len(players) < 2:
            await ctx.send("Please mention at least two players to play Impostor.")
        else:
            player_mentions = [p.mention for p in players]
            embed = await choose_Embeds(
                "impostor_game",
                author=ctx.author.display_name,
                author_id=ctx.author.id,
                players=player_mentions,
            )
            view = choose_Views(
                "Impostor",
                author_id=ctx.author.id,
                author_name=ctx.author.display_name,
                players=players,
            )
            await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Impostor(bot))
