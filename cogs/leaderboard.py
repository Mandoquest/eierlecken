import discord
from discord.ext import commands
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leaderboard")
    async def show_leaderboard(self, ctx, top: int = 10):
        """Zeigt das Leaderboard an.

        *top* kann 10 oder 20 sein. Andere Werte werden abgelehnt.
        Das Ranking basiert auf dem MandoCoins‑Guthaben in der Inventurdatenbank.
        """
        if top not in (10, 20):
            await ctx.send("Bitte 10 oder 20 als oberste Anzahl angeben.", ephemeral=True)
            return

        top_str = str(top)
        try:
            embed =  await choose_Embeds(
                "leaderboard", top=top_str, user=str(ctx.author.id), bot=self.bot
            )
            view = await choose_Views(
                "leaderboard", top=top_str, user=str(ctx.author.id)
            )
            # Keine Benachrichtigungen für mentions im Embed
            allowed = discord.AllowedMentions(users=False, roles=False, everyone=False)
            await ctx.send(embed=embed, view=view, allowed_mentions=allowed)
        except Exception as e:
            await ctx.send(f"Fehler beim Laden des Leaderboards: {e}")


async def setup(bot):
    await bot.add_cog(Leaderboard(bot))
