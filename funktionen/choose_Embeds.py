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
        from embeds.stockmarket.create_stock_embed import create_stock_embed_sync
        return await asyncio.to_thread(create_stock_embed_sync, **kwargs)


    elif name == "buy_Stock":
        from embeds.stockmarket.buy_stock import buy_stock_embed
        return await call_embed(buy_stock_embed, **kwargs)



    else:
        raise ValueError(f"Embed '{name}' ist nicht definiert.")
