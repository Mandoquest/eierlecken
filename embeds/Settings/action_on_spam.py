import discord 

action_on_spam_embed = discord.Embed(
    title="⚠️ Choose Action on Spam",
    description="Select what should happen when a user triggers the antispam system.",
    color=discord.Color.red()
).add_field(
    name="🔔 1. Warning Only",
    value="Send a **private warning** to the user.\n_Suitable for relaxed or new communities._",
    inline=False
).add_field(
    name="⏳ 2. Timeout",
    value="Warn the user once, then apply a **timeout** (e.g. 60 seconds) on next offense.\n_Recommended for active servers._",
    inline=False
).add_field(
    name="🔨 3. Kick or Ban",
    value="Apply a **kick or ban** after repeated offenses.\n_Use only on highly restricted servers._",
    inline=False
).set_footer(
    text="You can also set how many warnings are allowed before action is taken."
)