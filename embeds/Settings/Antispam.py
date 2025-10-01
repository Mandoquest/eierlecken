import discord

Antispam_embed = discord.Embed(
    title="🛡️ Antispam Settings",
    description="Adjust the behavior of the antispam system for this server.",
    color=discord.Color.blue()
).add_field(
    name="📨 Message Limit",
    value="**5 messages** allowed within **10 seconds**.",
    inline=False
).add_field(
    name="⚠️ Action on Spam",
    value="User receives a **warning** on first offense, then a **60-second timeout**.",
    inline=False
).add_field(
    name="🚫 Ignored Roles",
    value="`@Admin`, `@Moderator`",
    inline=False
).add_field(
    name="📍 Ignored Channels",
    value="#off-topic, #bot-commands",
    inline=False
).set_footer(
    text="Use the buttons or /antispam edit to modify these settings."
)