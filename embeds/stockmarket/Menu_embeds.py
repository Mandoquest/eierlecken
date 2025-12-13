import discord


embed_main = discord.Embed(
    title="📈 Global Stock Exchange",
    description=(
        "Welcome to the **Stock Center**!\n"
        "Here you can browse market data, manage your portfolio, "
        "and analyze your financial performance."
    ),
    color=discord.Color.green(),
)

embed_main.add_field(
    name="🔍 Market Overview",
    value="View current prices, trends, and market movements.",
    inline=False,
)

embed_main.add_field(
    name="💼 Portfolio",
    value="Manage your open positions and check your account balance.",
    inline=False,
)

embed_main.add_field(
    name="📊 Statistics",
    value="See detailed information about your gains, losses, and total wealth.",
    inline=False,
)

embed_main.set_footer(text="Use the buttons below to continue.")
embed_main.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1170/1170576.png")


embed_market = discord.Embed(
    title="🔍 Market Overview",
    description=(
        "Here you can view the latest market analysis.\n"
        "Prices, trends, volatility, and trading volume — all in one place."
    ),
    color=discord.Color.blue(),
)

embed_market.add_field(
    name="📉 Falling Prices",
    value="Shows stocks currently trending downward.",
    inline=False,
)

embed_market.add_field(
    name="📈 Rising Prices",
    value="View the strongest gainers on the market right now.",
    inline=False,
)

embed_market.add_field(
    name="🌐 Global Trend",
    value="Overall market direction based on average indicators.",
    inline=False,
)

embed_market.set_footer(text="Refresh frequently to stay up to date.")
embed_market.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/414/414974.png")


your_portfolio = discord.Embed(
    title="💼 Your Portfolio",
    description=(
        "This page shows your open positions, total net worth, "
        "and your transaction history."
    ),
    color=discord.Color.gold(),
)

your_portfolio.add_field(
    name="📦 Open Positions",
    value="Shows all the stocks you currently own.",
    inline=False,
)

your_portfolio.add_field(
    name="💰 Account Balance", value="Your available funds for investing.", inline=False
)

your_portfolio.add_field(
    name="📜 Transaction History",
    value="A list of all your past buys and sells.",
    inline=False,
)

your_portfolio.set_footer(text="A clear overview leads to smarter decisions.")
your_portfolio.set_thumbnail(
    url="https://cdn-icons-png.flaticon.com/512/1997/1997928.png"
)


Fincancial_statistics = discord.Embed(
    title="📊 Financial Statistics",
    description=(
        "Here you can analyze your performance.\n"
        "Profit, loss, total value trends, and portfolio distribution."
    ),
    color=discord.Color.purple(),
)

Fincancial_statistics.add_field(
    name="📈 Total Value Progress",
    value="Displays how your wealth changed over time (if available).",
    inline=False,
)

Fincancial_statistics.add_field(
    name="💹 Profit & Loss",
    value="A breakdown of your profitability based on completed trades.",
    inline=False,
)

Fincancial_statistics.add_field(
    name="📊 Portfolio Balance",
    value="Shows how diversified your current portfolio is.",
    inline=False,
)

Fincancial_statistics.set_footer(text="Smart analysis leads to smart investing.")
Fincancial_statistics.set_thumbnail(
    url="https://cdn-icons-png.flaticon.com/512/3798/3798381.png"
)
