import discord


def aktueller_Job(user):
    Job = user.get_job(user)
    Job = Job["name"]
    embed = discord.Embed(
        title="💼 Dein aktueller Job",
        description=f"**{user.display_name}**, dein aktueller Job ist:",
        color=discord.Color.green(),
    )

    embed.add_field(name="Job", value=f"🛠️ {Job}", inline=False)
    embed.set_footer(text="Nutze !work, um mit deinem Job Geld zu verdienen.")
    embed.set_thumbnail(url=user.display_avatar.url)
    return embed
