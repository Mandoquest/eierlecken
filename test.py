print("\033[32mDies ist rot\033[0m")
import discord


class MyView(discord.ui.View):
    @discord.ui.button(label="A button", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        button.disabled = True
