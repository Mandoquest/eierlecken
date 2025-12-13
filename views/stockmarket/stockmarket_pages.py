import discord
from discord.ui import View, Button
from funktionen.inv_interface import add_item
from funktionen.choose_Views import choose_Views
from funktionen.choose_Embeds import choose_Embeds


async def Stockmarket_page1():
    print("Stockmarket_page1 view initialized")

    class Stockmarket_page1(View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)

        @discord.ui.button(
            label="back",
            style=discord.ButtonStyle.red,
            emoji="⬅️",
            custom_id="back",
        )
        async def back_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stockmarket")
            view = await choose_Views("stockmarket")
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(
            label="Apple (AAPL)",
            style=discord.ButtonStyle.blurple,
            emoji="🍎",
            custom_id="stock_aapl",
        )
        async def aapl_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            print("AAPL button callback triggered")
            embed = await choose_Embeds("stock", ticker_symbol="AAPL")

            view = await choose_Views("stock", ticker_symbol="AAPL")
            print("AAPL button pressed")
            await interaction.response.edit_message(embed=embed, view=view)

        @discord.ui.button(
            label="Microsoft (MSFT)",
            style=discord.ButtonStyle.blurple,
            emoji="🪟",
            custom_id="stock_msft",
        )
        async def msft_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="MSFT")
            await interaction.response.send_message(embed=embed)

        @discord.ui.button(
            label="Amazon (AMZN)",
            style=discord.ButtonStyle.blurple,
            emoji="📦",
            custom_id="stock_amzn",
        )
        async def amzn_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="AMZN")
            await interaction.response.send_message(embed=embed)

        @discord.ui.button(
            label="Next page",
            style=discord.ButtonStyle.blurple,
            emoji="➡️",
            custom_id="next_page_button",
        )
        async def next_page_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            view = await choose_Views("Stockmarket_page2")
            await interaction.response.edit_message(view=view)

    return Stockmarket_page1()


async def Stockmarket_page2():
    class Stockmarket_page2(View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)

        @discord.ui.button(
            label="previous page",
            style=discord.ButtonStyle.blurple,
            emoji="⬅️",
            custom_id="previous_page",
        )
        async def previous_layer_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            view = await choose_Views("Stockmarket_page1")
            await interaction.response.edit_message(view=view)

        async def googl_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="GOOGL")
            await interaction.response.send_message(
                "You selected Alphabet (GOOGL)!", ephemeral=True
            )

        @discord.ui.button(
            label="Meta (META)",
            style=discord.ButtonStyle.blurple,
            emoji="📘",
            custom_id="stock_meta",
        )
        async def meta_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="META")
            await interaction.response.send_message(
                "You selected Meta (META)!", ephemeral=True
            )

        @discord.ui.button(
            label="Tesla (TSLA)",
            style=discord.ButtonStyle.blurple,
            emoji="⚡",
            custom_id="stock_tsla",
        )
        async def tsla_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="TSLA")
            await interaction.response.send_message(
                "You selected Tesla (TSLA)!", ephemeral=True
            )

        @discord.ui.button(
            label="NVIDIA (NVDA)",
            style=discord.ButtonStyle.blurple,
            emoji="🎮",
            custom_id="stock_nvda",
        )
        async def nvda_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="NVDA")
            await interaction.response.send_message(
                "You selected NVIDIA (NVDA)!", ephemeral=True
            )

        @discord.ui.button(
            label="Next page",
            style=discord.ButtonStyle.blurple,
            emoji="➡️",
            custom_id="next_page_button",
        )
        async def next_page_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            view = await choose_Views("Stockmarket_page3")
            await interaction.response.edit_message(view=view)

    return Stockmarket_page2()


async def Stockmarket_page3():
    class Stockmarket_page3(View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)

        @discord.ui.button(
            label="previous page",
            style=discord.ButtonStyle.blurple,
            emoji="⬅️",
            custom_id="previous_page_3",
        )
        async def previous_layer_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            view = await choose_Views("Stockmarket_page2")
            await interaction.response.edit_message(view=view)

        @discord.ui.button(
            label="Berkshire Hathaway (BRK.A)",
            style=discord.ButtonStyle.blurple,
            emoji="🏦",
            custom_id="stock_brka",
        )
        async def brka_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="BRK.A")
            await interaction.response.send_message(
                "You selected Berkshire Hathaway (BRK.A)!", ephemeral=True
            )

        @discord.ui.button(
            label="JPMorgan Chase (JPM)",
            style=discord.ButtonStyle.blurple,
            emoji="💰",
            custom_id="stock_jpm",
        )
        async def jpm_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="JPM")
            await interaction.response.send_message(
                "You selected JPMorgan Chase (JPM)!", ephemeral=True
            )

        @discord.ui.button(
            label="Johnson & Johnson (JNJ)",
            style=discord.ButtonStyle.blurple,
            emoji="💊",
            custom_id="stock_jnj",
        )
        async def jnj_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            embed = await choose_Embeds("stock", ticker_symbol="JNJ")
            await interaction.response.send_message(
                "You selected Johnson & Johnson (JNJ)!", ephemeral=True
            )

    return Stockmarket_page3()
