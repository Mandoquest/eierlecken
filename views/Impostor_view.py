import discord

from funktionen.choose_Embeds import choose_Embeds
from funktionen.choose_Views import choose_Views
from funktionen.choose_impostor import choose_impostor

class ImpostorStart(discord.ui.View):
    def __init__(self, author_id, author_name, players):
        super().__init__(timeout=None)
        self.author_id = author_id
        self.author_name = author_name
        self.players = list(players)  # List of discord.Member
        self.confirmed = set()        # Set of user IDs

    @discord.ui.button(label="confirm", style=discord.ButtonStyle.green, emoji="✅")
    async def start_game(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user

        if user.id not in [p.id for p in self.players] and user.id != self.author_id:
            await interaction.response.send_message("You are not a player in this game.", ephemeral=True)
            return
        if user.id in self.confirmed:
            await interaction.response.send_message("You have already confirmed your participation.", ephemeral=True)
            return

        self.confirmed.add(user.id)
        player_mentions = [p.mention for p in self.players]
        confirmed_mentions = [p.mention for p in self.players if p.id in self.confirmed]

        embed = await choose_Embeds(
            "edit_impostor",
            players=player_mentions,
            confirmed=confirmed_mentions,
            author=self.author_name
        )
        await interaction.response.edit_message(embed=embed, view=self)

        print(f"Confirmed: {self.confirmed} / Players: {self.players}")
        if len(self.confirmed) == len(self.players):
            await choose_impostor(self.players)
            embed = await choose_Embeds("Impostor_end",players=self.players)
            await interaction.followup.send("All players confirmed! Check your DMs.")


