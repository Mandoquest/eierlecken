import asyncio


async def choose_Views(name, **kwargs):
    async def call_view(func, **kw):
        if asyncio.iscoroutinefunction(func):
            return await func(**kw)
        else:
            return func(**kw)

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

    elif name == "Job_liste":
        from views.Jobs.jobs import WorkView
        from datenbanken.job_list import jobs

        return await call_view(WorkView, jobs)

    elif name == "Sprachkanal":
        from views.Sprachkanal import Sprachkanal_Buttons

        view = Sprachkanal_Buttons

    elif name == "Test":
        from views.Test import Test

        view = Test

    elif name == "stockmarket":
        from views.stockmarket.stockmarket import StockMarketView

        view = StockMarketView

    elif name == "Stockmarket_page1":
        from views.stockmarket.stockmarket_pages import Stockmarket_page1

        view = Stockmarket_page1

    elif name == "Stockmarket_page2":
        from views.stockmarket.stockmarket_pages import Stockmarket_page2

        view = Stockmarket_page2
    elif name == "Stockmarket_page3":
        from views.stockmarket.stockmarket_pages import Stockmarket_page3

        view = Stockmarket_page3
    elif name == "stock":
        from views.stockmarket import create_stock_buttons

        return await call_view(create_stock_buttons, **kwargs)

    else:
        raise ValueError(f"View '{name}' nicht gefunden.")

    return await call_view(view, **kwargs)
