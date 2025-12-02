import discord
from discord.ext import commands
from datenbanken.inv import get_inventory


class DarfIchHierNichtsSagen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test_command(self, ctx):
        player_id = ctx.author.id
        inventory = get_inventory(player_id)
        await ctx.send(f"Inventory for player {player_id}: {inventory}")
