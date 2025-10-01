import discord
from discord.ext import commands
from datenbanken.datenbanken_test import gib_guthaben, ändere_guthaben


class gift(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gift", aliases=["Gift", "GIFT", "g"])
    async def gift(self, ctx, member: discord.Member, amount: int):
        sender = ctx.author
        receiver = member
        if amount <= 0:
            await ctx.send("Please provide an amount greater than 0.")
            return
        if sender == receiver:
            await ctx.send("You cannot gift to yourself.")
            return
        balance = gib_guthaben(sender.id)
        if balance < amount:
            await ctx.send(f"Insufficient funds. Your current balance: {balance}")
            return
        ändere_guthaben(sender.id, -amount)
        ändere_guthaben(receiver.id, amount)

        await ctx.send(
            f"{sender.mention} has successfully gifted {amount} to {receiver.mention}.\n"
            f"Your new balance: {gib_guthaben(sender.id)}"
        )


async def setup(bot):
    await bot.add_cog(gift(bot))
