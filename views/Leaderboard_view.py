import discord
from funktionen.choose_Embeds import choose_Embeds


class LeaderboardView(discord.ui.View):
    def __init__(self, user: str, top: str):
        super().__init__(timeout=None)
        self.user = user
        self.top = top

        # Button wechseln: Top 10 <-> Top 20
        if top == "10":
            self.add_item(LeaderboardTop20Button(user))
        elif top == "20":
            self.add_item(LeaderboardTop10Button(user))


class LeaderboardTop20Button(discord.ui.Button):
    def __init__(self, user: str):
        super().__init__(label="Top 20", style=discord.ButtonStyle.primary, emoji="🏆")
        self.user = user

    async def callback(self, interaction: discord.Interaction):
        if str(interaction.user.id) != self.user:
            await interaction.response.send_message(
                "This is not your button!", ephemeral=True
            )
            return

        embed = await choose_Embeds("leaderboard", top="20", user=self.user)
        await interaction.response.edit_message(
            embed=embed, view=create_leaderboard_buttons(top="20", user=self.user)
        )


class LeaderboardTop10Button(discord.ui.Button):
    def __init__(self, user: str):
        super().__init__(label="Top 10", style=discord.ButtonStyle.primary, emoji="🏆")
        self.user = user

    async def callback(self, interaction: discord.Interaction):
        if str(interaction.user.id) != self.user:
            await interaction.response.send_message(
                "This is not your button!", ephemeral=True
            )
            return

        embed = await choose_Embeds("leaderboard", top="10", user=self.user)
        await interaction.response.edit_message(
            embed=embed, view=create_leaderboard_buttons(top="10", user=self.user)
        )


def create_leaderboard_buttons(top: str, user: str) -> LeaderboardView:
    return LeaderboardView(user=user, top=top)
