import discord
from discord.ui import View
from funktionen.choose_Views import choose_Views
from funktionen.choose_Embeds import choose_Embeds
from funktionen.protectetview import ProtectedView
import os

# ---------------------- STOCKMARKET PAGE 1 ----------------------
class stockm_p1(ProtectedView):
    def __init__(self, author_id: int):
        super().__init__(author_id)

    @discord.ui.button(label="← Back", style=discord.ButtonStyle.red)
    async def back(self, interaction: discord.Interaction, _):
        view = await choose_Views("stockmarket_main", author_id=self.author_id)
        embed = await choose_Embeds("stockmarket_main")
        
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label="APPLE (AAPL)", style=discord.ButtonStyle.blurple)
    async def aapl(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="AAPL")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="AAPL",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)
                
    @discord.ui.button(label="Tesla (TSLA)", style=discord.ButtonStyle.blurple)
    async def tsla(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="TSLA")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="TSLA",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="Microsoft (MSFT)", style=discord.ButtonStyle.blurple)
    async def msft(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="MSFT")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="MSFT",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="Next →", style=discord.ButtonStyle.green)
    async def next_page(self, interaction: discord.Interaction, _):
        embed = await choose_Embeds("stockm_p2", author_id=self.author_id)
        view = await choose_Views("stockm_p2", author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)

# ---------------------- STOCKMARKET PAGE 2 ----------------------
class stockm_p2(ProtectedView):
    def __init__(self, author_id: int):
        super().__init__(author_id)

    @discord.ui.button(label="← Back", style=discord.ButtonStyle.red)
    async def back(self, interaction: discord.Interaction, _):
        view = await choose_Views("stockm_p1", author_id=self.author_id)
        embed = await choose_Embeds("stockm_p1")
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label="Amazon (AMZN)", style=discord.ButtonStyle.blurple)
    async def amzn(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="AMZN")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="AMZN",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="Google (GOOGL)", style=discord.ButtonStyle.blurple)
    async def goog(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="AMZN")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="AMZN",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="Netflix (NFLX)", style=discord.ButtonStyle.blurple)
    async def nflx(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="NFLX")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="NFLX",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="→ Next", style=discord.ButtonStyle.green)
    async def next_page(self, interaction: discord.Interaction, _):
        embed = await choose_Embeds("stockm_p3", author_id=self.author_id)
        view = await choose_Views("stockm_p3", author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)

# ---------------------- STOCKMARKET PAGE 3 ----------------------
class stockm_p3(ProtectedView):
    def __init__(self, author_id: int):
        super().__init__(author_id)

    @discord.ui.button(label="← Back", style=discord.ButtonStyle.red)
    async def back(self, interaction: discord.Interaction, _):
        view = await choose_Views("stockm_p2", author_id=self.author_id)
        embed = await choose_Embeds("stockm_p2")
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label="McDonald's (MCD)", style=discord.ButtonStyle.blurple)
    async def mcd(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="MCD")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="MCD",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="Ubisoft (UBSFY)", style=discord.ButtonStyle.blurple)
    async def ubsfy(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="UBSFY")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="UBSFY",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="Coca-Cola (KO)", style=discord.ButtonStyle.blurple)
    async def ko(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="KO")
        file = discord.File(filename)

        view = await choose_Views(
            "stock",
            ticker_symbol="KO",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)

    @discord.ui.button(label="→ Next", style=discord.ButtonStyle.green)
    async def next_page(self, interaction: discord.Interaction, _):
        embed = await choose_Embeds("stockm_p4", author_id=self.author_id)
        view = await choose_Views("stockm_p4", author_id=self.author_id)
        await interaction.response.edit_message(embed=embed, view=view)

# ---------------------- STOCKMARKET PAGE 4 ----------------------
class stockm_p4(ProtectedView):
    def __init__(self, author_id: int):
        super().__init__(author_id)

    @discord.ui.button(label="← Back", style=discord.ButtonStyle.red)
    async def back(self, interaction: discord.Interaction, _):
        view = await choose_Views("stockm_p3", author_id=self.author_id)
        embed = await choose_Embeds("stockm_p3")
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label="NVIDIA (NVDA)", style=discord.ButtonStyle.blurple)
    async def nvda(self, interaction: discord.Interaction, _):
        embed, filename = await choose_Embeds("stock", ticker_symbol="NVDA")
        file = discord.File(filename)
        

        view = await choose_Views(
            "stock",
            ticker_symbol="NVDA",
            author_id=self.author_id
        )

        await interaction.response.edit_message(
            embed=embed,
            view=view,
            attachments=[file]
        )

        os.remove(filename)
