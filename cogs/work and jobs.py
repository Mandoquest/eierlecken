import discord
from discord.ext import commands
from datenbanken.jobs import get_job
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views


class Work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="work", aliases=["Work"])
    async def Work(self, ctx):
        user_id = ctx.user.id
        job = get_job(user_id)
        if job is None:
            await ctx.send("You dont have a Job! use !jobs to get one")
        elif job is not None:
            await ctx.send(f"your job is {job}")

    @commands.command(name="Jobs", aliases=["Job", "jobs", "job"])
    async def Job(self, ctx):
        user = ctx.user.id
        print("embed creation startet")
        try:
            Job = get_job(user.id)
            if Job is None:
                embed = await choose_Embeds("Job_liste", user=user)
                view = choose_Views("Job_liste")
                print("Embed created:", embed)
                await ctx.send(embed=embed, view=view)

            elif Job is not None:
                embed = await choose_Embeds("aktueller_Job", user=user)
                print("Embed created:", embed)
                view = choose_Views("aktueller_Job", user=user)
                await ctx.send(embed=embed)
        except Exception as e:
            print("Error sending jobs embed:", e)
            await ctx.send(f"Error: {e}")


async def setup(bot):
    await bot.add_cog(Work(bot))
