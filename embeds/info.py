import discord
from discord.ext import commands


def help_erstellen(user, arg=None):
    if arg is None:
        embed = discord.Embed(
            title="ℹ️ Bot Help",
            description="Welcome to the Info section! Here you can find useful information about the bot's features and commands.",
            color=discord.Color.blue(),
        )
        embed.add_field(
            name="💰 Economy Commands",
            value=(
                "`!daily` - Claim your daily reward.\n"
                "`!scratchcard` - Buy a scratch card for a chance to win coins (costs 5000 coins).\n"
                "`!balance` - Check your current coin balance.\n"
                "`!cd` - Check your command cooldowns.\n"
            ),
            inline=False,
        )

        embed.add_field(
            name="🎮 Game Commands",
            value=(
                "`!blackjack` - Start a game of blackjack.\n"
                "`!impostor` - Start an impostor game in your server. Tag a user to invite them.\n"
            ),
            inline=False,
        )
        embed.add_field(
            name="ℹ️ Info Commands",
            value=(
                "`!info` - Displays this information message.\n"
                "`!Info <command>` - Provides detailed information about a specific command.\n"
            ),
            inline=False,
        )
        embed.add_field(
            name="🔧 Voice Channel Commands",
            value=(
                "`rename` - Rename your temporary voice channel.\n"
                "`userlimit` - Set the user limit for your temporary voice channel.\n"
                "`kick` - Kick a member from your temporary voice channel.\n"
                "`promote` - Promote a member to owner of your temporary voice channel.\n"
            ),
            inline=False,
        )
        embed.set_footer(text="Use commands wisely! ⚡")
        return embed
    elif arg.lower() == "daily":
        embed = discord.Embed(
            title="🗓️ Daily Command",
            description=(
                "The `!daily` command allows you to claim a daily reward of coins. You can use this command once every 24 hours.\n\n"
                "**How to Use:**\n"
                "`!daily` - Claim your daily reward.\n\n"
                "**Cooldown:**\n"
                "This command has a 24-hour cooldown. You will be notified if you try to use it before the cooldown period is over."
            ),
            color=discord.Color.green(),
        )
        return embed
    elif arg.lower() == "scratchcard":
        embed = discord.Embed(
            title="🎟️ scratchcard info",
            description=(
                "**possible Items:**\n"
                "<:diamond:1414017424398745731> 25,000 coins (00.1% chance)\n"
                "❌ Rivet (20% chance)\n"
                "<:coin:1414017451875893249> 575 coins (38% chance)\n"
                "<:banknote:1414021458166026290> 800 coins (25% chance)\n"
                "<:coinstack:1414017436289601637> 1,000 coins (10.9% chance)\n\n"
                "**costs:** 5000 coins per scratchcard\n"
                "**How does it work:**\n"
                "Buy a scratchcard (!scratchcard) and try your luck!\n"
                "Good luck!"
            ),
            color=discord.Color.blue(),
        )
        return embed
    elif arg.lower() == "blackjack":
        embed = discord.Embed(
            title="🎰 Welcome to Blackjack",
            description=(
                "Try your luck and outsmart the dealer!\n\n"
                "### 💵 Bet & Win\n"
                "• Use your virtual balance to place a bet\n"
                "• Win up to **2x your stake** — or hit a **Blackjack** for 2.5x!\n\n"
                "### 🃏 Game Rules\n"
                "• Number cards = face value\n"
                "• Face cards = 10\n"
                "• Ace = 1 or 11\n"
                "• Closest to 21 without going over **wins**\n\n"
                "### 🎮 Actions\n"
                "`/blackjack start [amount]` – Place your bet and play\n"
                "`Hit` – Draw a card\n"
                "`Stand` – Hold and end your turn\n\n"
                "🔗 [Full Rules](https://bicyclecards.com/how-to-play/blackjack)"
            ),
            color=discord.Color.gold(),
        )
    elif arg.lower() == "impostor":
        embed = discord.Embed(
            title="🕵️‍♂️ Impostor Command",
            description=(
                "The `!impostor` command allows you to start an impostor game in your server. You can invite other users to join the game.\n\n"
                "**How to Use:**\n"
                "`!impostor @user` - Start an impostor game and invite the tagged user.\n\n"
                "**You need at least 3 player**\n"
                "When enough players have joined, the game will begin and you'll receive a DM with your role."
            ),
            color=discord.Color.purple(),
        )

    embed.set_footer(text="Use your balance wisely – fortune favors the bold."),
    return embed
