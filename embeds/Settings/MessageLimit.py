import discord 

MessageLimit_embed = discord.Embed(
    title="📨 Choose Message Limit",
    description="Select how strict the antispam system should be for message frequency.",
    color=discord.Color.orange()
).add_field(
    name="🔹 Light",
    value="Allow **10 messages** every **15 seconds**\n_Suitable for relaxed chats._",
    inline=False
).add_field(
    name="🔸 Medium (Recommended)",
    value="Allow **5 messages** every **10 seconds**\n_Balanced for most communities._",
    inline=False
).add_field(
    name="🔴 Strict",
    value="Allow **3 messages** every **5 seconds**\n_For high-traffic or rule-sensitive channels._",
    inline=False
).set_footer(
    text="Use the Buttons below to apply a setting."
)