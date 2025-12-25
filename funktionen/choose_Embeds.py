import discord
import asyncio


async def choose_Embeds(name, **kwargs):
    async def call_embed(func, **kw):
        if asyncio.iscoroutinefunction(func):
            return await func(**kw)
        else:
            return func(**kw)

    if name == "Main":
        from embeds.Settings.MainSettings import Mainsettings_Embed

        return Mainsettings_Embed

    elif name == "Welcome_channel":
        from embeds.Settings.WelcomeChannel import welcome_channel

        guild = kwargs.get("guild")
        if guild is None:
            raise ValueError("Guild is required for 'Welcome_channel' embed.")
        return await call_embed(welcome_channel, guild=guild)

    elif name == "Antispam":
        from embeds.Settings.Antispam import Antispam_embed

        return Antispam_embed

    elif name == "Message_Limit":
        from embeds.Settings.MessageLimit import MessageLimit_embed

        return MessageLimit_embed

    elif name == "action_on_spam":
        from embeds.Settings.action_on_spam import action_on_spam_embed

        return action_on_spam_embed

    elif name == "impostor_game":
        from embeds.Impostor import impostor_game

        return await call_embed(impostor_game, **kwargs)

    elif name == "edit_impostor":
        from embeds.Impostor import edit_impostor

        return await call_embed(edit_impostor, **kwargs)

    elif name == "Impostor_end":
        from embeds.Impostor import Impostor_end

        return await call_embed(Impostor_end, **kwargs)

    elif name == "cd":
        from embeds.cd import erstelle_cd_embed

        return await call_embed(erstelle_cd_embed, **kwargs)

    elif name == "cooldown_n_ready":
        from embeds.cd import erstelle_cd_n_ready

        return await call_embed(erstelle_cd_n_ready, **kwargs)

    elif name == "scratchcard_erstellen":
        from embeds.scratchcard import scratchcard_erstellen

        return await call_embed(scratchcard_erstellen, **kwargs)

    elif name == "help_erstellen":
        from embeds.info import help_erstellen

        return await call_embed(help_erstellen, **kwargs)

    elif name == "leaderboard":
        from embeds.leaderboard import leaderboard_erstellen

        return await call_embed(leaderboard_erstellen, **kwargs)
    elif name == "Job_liste":
        from embeds.Jobs.Job_liste import jobs_embed

        return await call_embed(jobs_embed, **kwargs)
    elif name == "aktueller_Job":
        from embeds.Jobs.aktueller_Job import aktueller_Job

        return await call_embed(aktueller_Job, **kwargs)
    elif name == "Sprachkanal":
        from embeds.Sprachkanal import Sprachkanal

        return await call_embed(Sprachkanal, **kwargs)
    elif name == "Test":
        from embeds.Test import embed

        return embed
    elif name == "stockmarket_main":
        from embeds.stockmarket.Menu_embeds import embed_main

        return embed_main
    
    elif name == "stockm_p1":
        from embeds.stockmarket.Stockmarket_pages import stockm_p1

        return stockm_p1

    elif name == "Create_stock_embed":
        from embeds.stockmarket.create_stock_embed import create_stock_embed

        return await call_embed(create_stock_embed, **kwargs)
    
    elif name == "your_portfolio":
        from embeds.stockmarket.Menu_embeds import your_portfolio

        return your_portfolio
    elif name == "Fincancial_statistics":
        from embeds.stockmarket.Menu_embeds import Fincancial_statistics

        return Fincancial_statistics
    elif name == "buy_stock":
        from embeds.stockmarket.transaction_embeds import embed

        return await call_embed(embed, **kwargs)
    else:
        raise ValueError(f"Embed '{name}' ist nicht definiert.")
