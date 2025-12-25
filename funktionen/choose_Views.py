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

    elif name == "stockmarket_main":
        from views.stockmarket.Stockmarket_Main import Stockmarket_Main

        view = Stockmarket_Main


    elif name == ("stockm_p1"):
        from views.stockmarket.stockmarket_pages import stockm_p1

        view = stockm_p1

    elif name == "stock":
        from views.stockmarket.buy_stock import StockBuyView

        return StockBuyView(**kwargs)

    else:
        raise ValueError(f"View '{name}' nicht gefunden.")

    return await call_view(view, **kwargs)
