import asyncio

async def choose_Views(name, **kwargs):
    async def call_view(cls, **kw):
        # cls ist die Klasse der View, erzeugt hier die Instanz
        if asyncio.iscoroutinefunction(cls):
            return await cls(**kw)
        else:
            return cls(**kw)

    view = None

    if name == "Main":
        from views.Settings.MainButtons import MainButtons
        view = MainButtons

    elif name == "Welcome_channel":
        from views.Settings.WelcomeChannel import WelcomeChannel_View
        view = WelcomeChannel_View

    elif name == "Antispam":
        from views.Settings.Antispam import AntispamButtons
        view = AntispamButtons

    elif name == "Message_Limit":
        from views.Settings.MessageLimit_view import MessageLimitButtons
        view = MessageLimitButtons

    elif name == "Impostor":
        from views.Impostor_view import ImpostorStart
        view = ImpostorStart

    elif name == "leaderboard":
        from views.Leaderboard_view import create_leaderboard_buttons
        view = create_leaderboard_buttons

    elif name == "Sprachkanal":
        from views.Sprachkanal import Sprachkanal_Buttons
        view = Sprachkanal_Buttons

    elif name == "Test":
        from views.Test import TestView
        view = TestView

    elif name== "leaderboard_erstellen":
        from views.Leaderboard_view import create_leaderboard_buttons
        view = create_leaderboard_buttons








    elif name == "stockmarket_main":
        from views.stockmarket.stockmarket_Main import stockmarket_main
        view = stockmarket_main

    elif name == "stockm_p1":
        from views.stockmarket.stockmarket_pages import stockm_p1
        view = stockm_p1

    elif name == "stockm_p2":
        from views.stockmarket.stockmarket_pages import stockm_p2
        view = stockm_p2

    elif name == "stockm_p3":
        from views.stockmarket.stockmarket_pages import stockm_p3
        view = stockm_p3

    elif name == "stockm_p4":
        from views.stockmarket.stockmarket_pages import stockm_p4
        view = stockm_p4

    elif name == "stock":
        from views.stockmarket.create_stock_buttons import create_stock_buttons
        view = create_stock_buttons

    elif name == "buy_Stock":
        from views.stockmarket.buy_stock import StockBuyView
        view = StockBuyView

    elif name == "sell_stock":
        from views.stockmarket.sell_stock import StockSellView
        view = StockSellView
    
    elif name == "your_portfolio":
        from views.stockmarket.your_portfolio import YourPortfolio
        view = YourPortfolio

    elif name == "Fincancial_Statistics":
        from views.stockmarket.Finacial_Statistics import FinancialStatisticsView
        view = FinancialStatisticsView

    else:
        raise ValueError(f"View '{name}' nicht gefunden.")

    
    return await call_view(view, **kwargs)
