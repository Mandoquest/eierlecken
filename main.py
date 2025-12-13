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

    CHANNEL_ID = 1265535516863107079
    try:
        channel = await client.fetch_channel(CHANNEL_ID)
    except Exception as e:
        print("Fehler beim Fetchen des Channels:", e)
        return

    embed = await choose_Embeds("stockmarket")
    view = await choose_Views("stockmarket")
    await channel.send(embed=embed, view=view)

    @client.event
    async def on_command_error(ctx, error):
        try:
            cmd_name = ctx.command.name if ctx.command else None
            print(f"Command error in {cmd_name}: {error}")
        except Exception as e:
            print("Fehler in on_command_error handler:", e)


@client.command()
async def ping(ctx):
    print(ctx.author.id)
    view = await choose_Views("view_stockmarket")
    await ctx.send(view=view)


@client.command()
async def Test(ctx):
    print("Test command activated")
    embed = await choose_Embeds("Test")
    print("Embed chosen")
    view = await choose_Views("Test")
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
