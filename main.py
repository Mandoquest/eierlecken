import discord
import os
from discord.ext import commands
import asyncio
import sys
from dotenv import load_dotenv
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views
from funktionen.error_handler import report_exception

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
                await report_exception(client, e, context=f"load extension {filename}", admin_channel_id=ERROR_CHANNEL_ID if 'ERROR_CHANNEL_ID' in globals() else None, admin_user_id=ADMIN_USER_ID if 'ADMIN_USER_ID' in globals() else None)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="mit deinen Daten"))
    print("\033[32mBot ist Fertig\033[0m")

    CHANNEL_ID = 1265535516863107079
    try:
        channel = await client.fetch_channel(CHANNEL_ID)
    except Exception as e:
        await report_exception(client, e, context="on_ready fetch channel", admin_channel_id=ERROR_CHANNEL_ID if 'ERROR_CHANNEL_ID' in globals() else None, admin_user_id=ADMIN_USER_ID if 'ADMIN_USER_ID' in globals() else None)
        return

    embed = await choose_Embeds("stockmarket_main")
    view = await choose_Views("stockmarket_main")
    await channel.send(embed=embed, view=view)


@client.command()
async def clear_all(ctx):
    await ctx.send("Starte das Löschen aller Nachrichten... Dies kann einige Minuten dauern.", delete_after=5)

    async for message in ctx.channel.history(limit=None, oldest_first=False):
        try:
            await message.delete()
            await asyncio.sleep(0.1)  
        except discord.Forbidden:
            await ctx.send("Ich habe nicht genügend Berechtigungen zum Löschen von Nachrichten.")
            break
        except discord.HTTPException:
            continue  

    await ctx.send("Alle Nachrichten wurden gelöscht.", delete_after=5)  




@client.command()
async def ping(ctx):
    print(ctx.author.id)
    view = await choose_Views("buy_Stock", ticker_symbol="NVDA", author_id=ctx.author.id)
    embed = await choose_Embeds("Test") 
    await ctx.send(embed=embed, view=view)

@client.command()
async def line(ctx):
    print("--------------------------------------------------------------------------------")
    await ctx.send("Done")


@client.command()
async def test(ctx):
    embed, filename = await choose_Embeds("stock", ticker_symbol="NVDA")
    file = discord.File(filename)
    view = await choose_Views(
        "stock",
        ticker_symbol="NVDA",
        author_id=ctx.author.id
    )
    await ctx.send(embed=embed, view=view, file=file)



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

# Optional: set an admin user id or an admin channel id via environment variables
ERROR_CHANNEL_ID = int(os.getenv("ERROR_CHANNEL_ID")) if os.getenv("ERROR_CHANNEL_ID") else None
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID")) if os.getenv("ADMIN_USER_ID") else None


async def main():
    async with client:
        # Set asyncio loop exception handler to report uncaught exceptions
        loop = asyncio.get_running_loop()

        def _loop_exc(loop, context):
            exc = context.get('exception') or Exception(context.get('message'))
            asyncio.create_task(report_exception(client, exc, context=str(context), admin_channel_id=ERROR_CHANNEL_ID, admin_user_id=ADMIN_USER_ID))

        loop.set_exception_handler(_loop_exc)

        await load()
        await client.start(token)


@client.event
async def on_command_error(ctx, error):
    try:
        cmd_name = ctx.command.name if ctx.command else None
        await report_exception(client, error, context=f"command {cmd_name} by {ctx.author.id}", admin_channel_id=ERROR_CHANNEL_ID, admin_user_id=ADMIN_USER_ID)
    except Exception as e:
        print("Fehler in on_command_error handler:", e)


asyncio.run(main())


##################################
##          Sellbutton          ##
##         Back Button          ##
##################################