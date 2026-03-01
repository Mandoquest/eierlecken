import asyncio



async def choose_Embeds(name: str, **kwargs):
    async def call_embed(func, **kw):
        if asyncio.iscoroutinefunction(func):
            return await func(**kw)
        return func(**kw)


    if name == "Main":
        from embeds.Settings.MainSettings import Mainsettings_Embed
        return Mainsettings_Embed

    elif name == "Test":
        from embeds.Test import create_embed
        embed = await call_embed(create_embed)
        return embed


    elif name == "scratchcard_erstellen":
        from embeds.scratchcard import scratchcard_erstellen
        return await call_embed(scratchcard_erstellen, **kwargs)
    elif name == "cooldown_n_ready":
        from embeds.cooldown_n_ready import create_embed

        return await create_embed(**kwargs)
    
    elif name == "cd":
        from embeds.cd import erstelle_cd_embed
        return await call_embed(erstelle_cd_embed, **kwargs)
    
    elif name == "help_erstellen":
        from embeds.info import help_erstellen
        return await call_embed(help_erstellen, **kwargs)

    elif name == "impostor_game":
        from embeds.Impostor import impostor_game
        return await call_embed(impostor_game, **kwargs)

    elif name == "edit_impostor":
        from embeds.Impostor import edit_impostor
        return await call_embed(edit_impostor, **kwargs)

    elif name == "Impostor_end":
        from embeds.Impostor import Impostor_end
        return await call_embed(Impostor_end, **kwargs)
    

    elif name == "leaderboard":
        from embeds.leaderboard import leaderboard_erstellen
        return await call_embed(leaderboard_erstellen, **kwargs)
    

    elif name == "stockmarket_main":
        from embeds.stockmarket.Menu_embeds import embed_main
        return embed_main 

    elif name == "stockm_p1":
        from embeds.stockmarket.Stockmarket_pages import stockm_p1
        return stockm_p1

    elif name == "stockm_p2":
        from embeds.stockmarket.Stockmarket_pages import stockm_p2
        return stockm_p2 

    elif name == "stockm_p3":
        from embeds.stockmarket.Stockmarket_pages import stockm_p3
        return stockm_p3

    elif name == "stockm_p4":
        from embeds.stockmarket.Stockmarket_pages import stockm_p4
        return stockm_p4

    elif name == "stock":
        from embeds.stockmarket.create_stock_embed import create_stock_embed
        return await create_stock_embed(**kwargs)


    elif name == "buy_Stock":
        from embeds.stockmarket.buy_stock import buy_stock_embed
        return await call_embed(buy_stock_embed, **kwargs)
    
    elif name == "sell_stock":
        from embeds.stockmarket.sell_stock import sell_stock_embed
        return sell_stock_embed(**kwargs)
    

    elif name == "your_portfolio":
        print(f"choose_Embeds called with name 'your_portfolio' and kwargs: {kwargs}")
        from embeds.stockmarket.your_portfolio import create_your_portfolio_embed
        print(f"Calling create_your_portfolio_embed with kwargs: {kwargs}")
        embed = create_your_portfolio_embed(**kwargs)
        return embed
    
    elif name == "Fincancial_Statistics":
        print(f"choose_Embeds called with name 'Fincancial_Statistics' and kwargs: {kwargs}")
        from embeds.stockmarket.financial_statistics import create_financial_statistics_embed
        print(f"Calling create_financial_statistics_embed ")
        embed = await call_embed(create_financial_statistics_embed)
        return embed

    else:
        raise ValueError(f"Embed '{name}' ist nicht definiert.")
