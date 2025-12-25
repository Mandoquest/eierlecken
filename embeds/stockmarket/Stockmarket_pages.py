import discord 

stockm_p1 = discord.Embed(
    title="🔍 Stock Market Overview",
    description=(
        "Explore the latest stock market data here!\n"
        "Get insights on price movements, trends, and market dynamics."
    ),
    color=discord.Color.blue(),
)
stockm_p1.add_field(
    name="🍎 APPLE INC (AAPL)",
    description="for more info click the button below",
)
stockm_p1.add_field(
    name="🚗 TESLA INC (TSLA)",
    description="for more info click the button below",
)
stockm_p1.add_field(
    name="💼 MICROSOFT CORP (MSFT)",
    description="for more info click the button below",
)

stockm_p1.set_footer(text="Use the buttons below to get detailed stock info.")