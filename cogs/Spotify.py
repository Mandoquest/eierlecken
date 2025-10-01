import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio
from funktionen.spotify_to_youtube import spotify_to_youtube
from funktionen.choose_Embeds import choose_Embeds

# ---- Verbesserte YTDL Optionen ----
ytdl_format_options = {
    "format": "bestaudio/best",
    "quiet": True,
    "extract_flat": "in_playlist",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "opus",
            "preferredquality": "192",
        }
    ],
}

# ---- Verbesserte FFmpeg Optionen mit Puffer ----
ffmpeg_options = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn -bufsize 64k",
}


ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}  # Warteschlangen pro Server
        self.preloaded = {}  # Vorbereitete Songdaten

    async def ensure_voice(self, ctx):
        if ctx.author.voice is None:
            embed = await choose_Embeds("not_dc")
            await ctx.send(embed=embed)
            return None
        channel = ctx.author.voice.channel
        voice_client = ctx.guild.voice_client
        if voice_client is None:
            voice_client = await channel.connect()
        elif voice_client.channel != channel:
            await voice_client.move_to(channel)
        return voice_client

    async def preload_song(self, url):
        loop = asyncio.get_running_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=False)
        )
        if "entries" in data:
            data = data["entries"][0]
        return data["url"], data["title"]

    async def play_next(self, ctx, guild_id):
        if self.queues[guild_id]:
            url = self.queues[guild_id].pop(0)

            if guild_id in self.preloaded and self.preloaded[guild_id].get(url):
                url2, title = self.preloaded[guild_id].pop(url)
            else:
                url2, title = await self.preload_song(url)

            source = discord.FFmpegPCMAudio(url2, **ffmpeg_options)

            def after_playing(error):
                fut = asyncio.run_coroutine_threadsafe(
                    self.play_next(ctx, guild_id), self.bot.loop
                )
                try:
                    fut.result()
                except Exception as e:
                    print(f"Fehler nach Songende: {e}")

            ctx.guild.voice_client.play(source, after=after_playing)
            embed = await choose_Embeds("Main")
            await ctx.send(f"Spiele jetzt: **{title}**")

            # Nächsten Song vorbereiten
            if self.queues[guild_id]:
                next_url = self.queues[guild_id][0]
                if guild_id not in self.preloaded:
                    self.preloaded[guild_id] = {}
                if next_url not in self.preloaded[guild_id]:
                    self.preloaded[guild_id][next_url] = await self.preload_song(
                        next_url
                    )
        else:
            if ctx.guild.voice_client:
                await ctx.guild.voice_client.disconnect()
            await ctx.send("Die Warteschlange ist leer.")

    @commands.command(name="play")
    async def play(self, ctx, *, url):
        voice_client = await self.ensure_voice(ctx)
        if voice_client is None:
            return
        if "https://open.spotify.com/" in url:
            youtube_url = await spotify_to_youtube(url)
            if youtube_url is None:
                await ctx.send(
                    "Kein passendes YouTube-Video für diesen Spotify-Link gefunden."
                )
                return
            url = youtube_url

        if not ("youtube.com/watch" in url or "youtu.be/" in url):
            await ctx.send("Nur YouTube-Links werden unterstützt.")
            return

        guild_id = ctx.guild.id
        if guild_id not in self.queues:
            self.queues[guild_id] = []

        self.queues[guild_id].append(url)

        if guild_id not in self.preloaded:
            self.preloaded[guild_id] = {}
        if url not in self.preloaded[guild_id]:
            self.preloaded[guild_id][url] = await self.preload_song(url)

        if not voice_client.is_playing():
            await self.play_next(ctx, guild_id)
        else:
            await ctx.send("Lied zur Warteschlange hinzugefügt.")

    @commands.command(name="skip")
    async def skip(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.stop()
            await ctx.send("Song wurde übersprungen.")
        else:
            await ctx.send("Es läuft gerade nichts.")

    @commands.command(name="pause")
    async def pause(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.pause()
            await ctx.send("Musik pausiert.")
        else:
            await ctx.send("Es läuft gerade nichts.")

    @commands.command(name="resume")
    async def resume(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_paused():
            voice_client.resume()
            await ctx.send("Musik fortgesetzt.")
        else:
            await ctx.send("Die Musik ist nicht pausiert.")

    @commands.command(name="stop")
    async def stop(self, ctx):
        voice_client = ctx.guild.voice_client
        guild_id = ctx.guild.id
        if voice_client:
            self.queues[guild_id] = []
            if guild_id in self.preloaded:
                self.preloaded[guild_id] = {}
            await voice_client.disconnect()
            await ctx.send("Musik gestoppt und Warteschlange geleert.")
        else:
            await ctx.send("Ich bin in keinem Voice-Channel.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
