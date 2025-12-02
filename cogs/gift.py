import discord
from discord.ext import commands
from funktionen.inv_interface import remove_item, add_item, get_inventory


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
        balance = get_inventory(sender.id, "MandoCoins")
        if balance < amount:
            await ctx.send(f"Insufficient funds. Your current balance: {balance}")
            return
        remove_item(sender.id, "MandoCoins", amount)
        add_item(receiver.id, "MandoCoins", amount)

        balance_receiver = get_inventory(receiver.id, "MandoCoins")
        await ctx.send(
            f"{sender.mention} has successfully gifted {amount} to {receiver.mention}.\n"
            f"His/Her new balance: {balance_receiver}"
        )


async def setup(bot):
    await bot.add_cog(gift(bot))
