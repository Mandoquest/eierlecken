import discord
from discord.ext import commands
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leaderboard")
    async def show_leaderboard(self, ctx, top: int = 10):
        """Zeigt das Leaderboard an. Top kann 10 oder 20 sein."""
        top_str = str(top)
        try:
            embed = await choose_Embeds(
                "leaderboard", top=top_str, user=str(ctx.author.id), bot=self.bot
            )
            view = choose_Views("leaderboard", top=top_str, user=str(ctx.author.id))
            await ctx.send(embed=embed, view=view)
        except Exception as e:
            await ctx.send(f"Fehler beim Laden des Leaderboards: {e}")


async def setup(bot):
    await bot.add_cog(Leaderboard(bot))
