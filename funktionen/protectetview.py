import discord

class ProtectedView(discord.ui.View):
    def __init__(self, author_id: int, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        self.author_id = author_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Prüfen ob der klickende User der Author ist
        if interaction.user.id != self.author_id:
            # Ephemere Fehlermeldung
            await interaction.response.send_message(
                "❌ Du kannst diese Buttons nicht benutzen.",
                ephemeral=True
            )
            return False

        return True
