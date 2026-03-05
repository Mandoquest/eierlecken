from enum import member

import discord
import os
import json
from discord.ext import commands
from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views
from datenbanken.Sprachkanäle import get_channel
import asyncio


class Sprachkanal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "datenbanken/temp_channels.json"
        self.temp_channels = self.load_channels()


    @commands.Cog.listener()
    async def on_ready(self):
        print("Sprachkanal.py geladen")

    def load_channels(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return {}

    def save_channels(self):
        with open(self.file, "w") as f:
            json.dump(self.temp_channels, f, indent=4)

    @commands.command(name="Voicechannel", aliases=["vc", "voicechannel"])
    async def sprachkanal(self, ctx):
        
        print(f"User {ctx.author} ({ctx.author.id}) used the Voicechannel command in guild {ctx.guild} ({ctx.guild.id})")
        if ctx.author.guild_permissions.administrator:
            print("User has administrator permissions, sending embed and view")
            embed =  await choose_Embeds("Sprachkanal", Guild=ctx.guild)
            print("Embed created, creating view")
            view = await choose_Views("Sprachkanal", Guild=ctx.guild)
            await ctx.send(embed=embed, view=view)
        else:
            message = await ctx.send(
                "you dont have the permission, the message will be deleted in 5 seconds"
            )
            await asyncio.sleep(5)
            await message.delete()
            await ctx.message.delete()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print("--------------------------------------------------------------------------------")
        print(f"Voice state update detected for user {member} ({member.id}) in guild {member.guild} ({member.guild.id})")
        guild = member.guild
        trigger_channel_id = get_channel(guild.id)

        # ──────────────── JOIN / MOVE IN TRIGGER ────────────────
        print(f"Trigger channel ID: {trigger_channel_id}")
        if after.channel and after.channel.id == trigger_channel_id:
            # Verhindert doppeltes Erstellen
            for channel_id, owner_id in self.temp_channels.items():
                if owner_id == member.id:
                    channel = guild.get_channel(int(channel_id))
                    if channel:
                        await member.move_to(channel)
                    return

            category = after.channel.category

            try:
                created_channel = await guild.create_voice_channel(
                    name=f"{member.name}'s Room",
                    category=category,
                    reason="Join-to-Create Voice Channel"
                )

                # Owner speichern
                self.temp_channels[str(created_channel.id)] = member.id
                self.save_channels()

                # Rechte setzen
                await created_channel.set_permissions(
                    member,
                    manage_channels=True,
                    mute_members=True,
                    move_members=True,
                    connect=True
                )

                await member.move_to(created_channel)

            except Exception as e:
                print(f"[Voice-System] Fehler beim Erstellen: {e}")

        # ──────────────── LEAVE / MOVE OUT ────────────────
        print(f"Checking if user left a temp channel...")
        if before.channel:
            channel = before.channel
            channel_id = str(channel.id)

            if channel_id not in self.temp_channels:
                return

            try:
                # Channel leer → löschen
                if len(channel.members) == 0:
                    await channel.delete(reason="Temp Voice leer")
                    del self.temp_channels[channel_id]
                    self.save_channels()
                    return

                # Owner weg → neuen Owner bestimmen
                owner_id = self.temp_channels[channel_id]
                if member.id == owner_id:
                    new_owner = channel.members[0]
                    self.temp_channels[channel_id] = new_owner.id
                    self.save_channels()

                    await channel.set_permissions(
                        new_owner,
                        manage_channels=True,
                        mute_members=True,
                        move_members=True
                    )

            except Exception as e:
                print(f"[Voice-System] Fehler beim Löschen/Owner-Wechsel: {e}")

    @commands.command(name="rename")
    async def rename(self, ctx, *, new_name: str):
        if ctx.author.voice is None:
            return await ctx.send("You are not in a voice channel.")

        channel = ctx.author.voice.channel

        if str(channel.id) not in self.temp_channels:
            return await ctx.send("You can only rename temporary voice channels.")

        if self.temp_channels[str(channel.id)] != ctx.author.id:
            return await ctx.send("You do not own this voice channel.")

        await channel.edit(name=new_name)
        embed = discord.Embed(
            title="✅ Voice Channel Renamed",
            description=f"Your voice channel has been successfully renamed to:\n**{new_name}**",
            color=discord.Color.green(),
        )
        embed.set_footer(text="Action completed successfully")
        await ctx.send(embed=embed)

    @commands.command(name="userlimit", aliases=["limit", "Limit", "Userlimit"])
    async def userlimit(self, ctx, *, limit: int):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel.", ephemeral=True)
        channel = ctx.author.voice.channel
        if str(channel.id) not in self.temp_channels:
            return await ctx.send(
                "You can only set the user limit for temporary voice channels.",
                empheral=True,
            )
        if self.temp_channels[str(channel.id)] != ctx.author.id:
            return await ctx.send("You do not own this voice channel.", empheral=True)
        await channel.edit(user_limit=limit)
        await ctx.send(f"User limit set to {limit}.", ephemeral=True)

    @commands.command(name="kick", aliases=["Kick", "KICK"])
    async def kick(self, ctx, member: discord.Member):
        if ctx.author.voice is None:
            return await ctx.send("You are not in a voice channel.", ephemeral=True)
        channel = ctx.author.voice.channel
        if str(channel.id) not in self.temp_channels:
            return await ctx.send(
                "You can only kick members from temporary voice channels.",
                ephemeral=True,
            )
        if self.temp_channels[str(channel.id)] != ctx.author.id:
            return await ctx.send("You do not own this voice channel.", ephemeral=True)
        if member not in channel.members:
            return await ctx.send(
                f"{member.name} is not in your voice channel.", ephemeral=True
            )
        await member.move_to(None)
        await ctx.send(
            f"{member.name} has been kicked from the voice channel.", ephemeral=True
        )

    @commands.command(name="promote", aliases=["Promote"])
    async def promote(self, ctx, member: discord.Member):
        if ctx.author.voice is None:
            return await ctx.send("You are not in a voice channel.", ephemeral=True)
        channel = ctx.author.voice.channel
        if str(channel.id) not in self.temp_channels:
            return await ctx.send(
                "You can only promote members in temporary voice channels.",
                ephemeral=True,
            )
        if self.temp_channels[str(channel.id)] != ctx.author.id:
            return await ctx.send("You do not own this voice channel.", ephemeral=True)
        if member not in channel.members:
            return await ctx.send(
                f"{member.name} is not in your voice channel.", ephemeral=True
            )
        self.temp_channels[str(channel.id)] = member.id
        self.save_channels()
        await ctx.send(
            f"{member.name} has been promoted to channel owner.", ephemeral=True
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Sprachkanal(bot))
