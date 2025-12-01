import discord
import os
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views

client = commands.Bot(
    command_prefix="!", intents=discord.Intents.all(), help_command=None
)


async def load():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    COGS_DIR = os.path.join(BASE_DIR, "cogs")

    for filename in os.listdir(COGS_DIR):
        if filename.endswith(".py"):
            ext = f"cogs.{filename[:-3]}"
            try:
                await client.load_extension(ext)
            except Exception as e:
                print(f"Fehler beim Laden von {filename}: {e}")

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Game(name="mit deinen Daten"))
        print("\033[32mBot ist Fertig\033[0m")


@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description="`whoever reads this is stupid` <a:typing:1410736488915669124>",
    )
    await ctx.send(embed=embed)


@client.command()
async def Test(ctx):
    print("Test command activated")
    embed = await choose_Embeds("Test")
    print("Embed chosen")
    view = choose_Views("Test")
    print("Embed and View chosen")
    await ctx.send(embed=embed, view=view)
    print("Message sent")


@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You are not in a voice channel!")
        return
    channel = ctx.author.voice.channel
    await ctx.send(f"Verbinde mit **{channel.name}**...")
    await channel.connect()
    await ctx.send(f"connected with **{channel.name}** ✅")


load_dotenv()
token = os.getenv("DISCORD_TOKEN")


async def main():
    async with client:
        await load()
        await client.start(token)


asyncio.run(main())
