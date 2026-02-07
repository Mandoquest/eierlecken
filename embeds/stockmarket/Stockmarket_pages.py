import discord


stockm_p1 = discord.Embed(
    title="📊 Stock Market Overview",
    description=(
        "**Discover popular stocks at a glance**\n"
        "Click the buttons below to view detailed market data, trends and price movements."
    ),
    color=discord.Color.blurple(),
)
stockm_p1.add_field(
    name="🍎 Apple Inc.",
    value="`AAPL`\nClick below for details",
    inline=True,
)
stockm_p1.add_field(
    name="🚗 Tesla Inc.",
    value="`TSLA`\nClick below for details",
    inline=True,
)
stockm_p1.add_field(
    name="💼 Microsoft Corp.",
    value="`MSFT`\nClick below for details",
    inline=True,
)
stockm_p1.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2103/2103658.png")
stockm_p1.set_footer(text="Page 1 • Stock Market Dashboard")



stockm_p2 = discord.Embed(
    title="📊 Stock Market Overview",
    description=(
        "**Discover popular stocks at a glance**\n"
        "Click the buttons below to view detailed market data, trends and price movements."
    ),
    color=discord.Color.blurple(),
)
stockm_p2.add_field(
    name="📦 Amazon",
    value="`AMZN`\nClick below for details",
    inline=True,
)
stockm_p2.add_field(
    name="🔵 Google",
    value="`GOOGL`\nClick below for details",
    inline=True,
)
stockm_p2.add_field(
    name="🎬 Netflix",
    value="`NFLX`\nClick below for details",
    inline=True,
)
stockm_p2.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2103/2103658.png")
stockm_p2.set_footer(text="Page 2 • Stock Market Dashboard")



stockm_p3 = discord.Embed(
    title="📊 Stock Market Overview",
    description=(
        "**Discover popular stocks at a glance**\n"
        "Click the buttons below to view detailed market data, trends and price movements."
    ),
    color=discord.Color.blurple(),
)
stockm_p3.add_field(
    name="🍔 McDonald's",
    value="`MCD`\nClick below for details",
    inline=True,
)
stockm_p3.add_field(
    name="🎮 Ubisoft",
    value="`UBSFY`\nClick below for details",
    inline=True,
)
stockm_p3.add_field(
    name="🥤 Coca-Cola Company",
    value="`KO`\nClick below for details",
    inline=True,
)
stockm_p3.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2103/2103658.png")
stockm_p3.set_footer(text="Page 3 • Stock Market Dashboard")



stockm_p4 = discord.Embed(
    title="📊 Stock Market Overview",
    description=(
        "**Discover popular stocks at a glance**\n"
        "Click the buttons below to view detailed market data, trends and price movements."
    ),
    color=discord.Color.blurple(),
)
stockm_p4.add_field(
    name="🟢 NVIDIA",
    value="`NVDA`\nClick below for details",
    inline=True,
)
stockm_p4.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2103/2103658.png")
stockm_p4.set_footer(text="Page 4 • Stock Market Dashboard")
