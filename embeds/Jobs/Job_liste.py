from discord import Embed, Colour
from datenbanken.job_list import jobs
from datenbanken.jobs import get_job
import discord


def jobs_embed(user):
    print("jobs_embed loaded")
    embed = discord.Embed(
        title="🎮 Verfügbare Jobs im Bot",
        description="Wähle einen Job aus und starte dein Abenteuer! Je schwieriger der Job, desto anspruchsvoller das Minispiel.",
        colour=Colour.blurple(),
    )

    for job in jobs:
        embed.add_field(
            name=f"{job['name']}",
            value=f"🎯 Minispiel: {job['spiel']}",
            inline=False,
        )

        embed.set_footer(text="Viel Erfolg bei deinem neuen Job!")
        return embed
