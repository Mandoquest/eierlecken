def choose_Views(name, **kwargs):
    if name == "Main":
        from views.Settings.MainButtons import MainButtons

        return MainButtons(**kwargs)

    elif name == "Welcome_channel":
        from views.Settings.WelcomeChannel import WelcomeChannel_View

        return WelcomeChannel_View(**kwargs)

    elif name == "Antispam":
        from views.Settings.Antispam import AntispamButtons

        return AntispamButtons(**kwargs)

    elif name == "Message_Limit":
        from views.Settings.MessageLimit_view import MessageLimitButtons

        return MessageLimitButtons(**kwargs)

    elif name == "Impostor":
        from views.Impostor_view import ImpostorStart

        return ImpostorStart(**kwargs)

    elif name == "leaderboard":
        from views.Leaderboard_view import create_leaderboard_buttons

        user = kwargs.get("user")
        top = kwargs.get("top")
        if user is None or top is None:
            raise ValueError("Leaderboard View benötigt 'user' und 'top'.")
        return create_leaderboard_buttons(top=top, user=user)

    elif name == "Job_liste":
        from views.Jobs.jobs import WorkView
        from datenbanken.job_list import jobs

        return WorkView(jobs)
    elif name == "Sprachkanal":
        from views.Sprachkanal import Sprachkanal_Buttons

        return Sprachkanal_Buttons(**kwargs)
    elif name == "Test":
        from views.Test import Test

        return Test()
    else:
        raise ValueError(f"View '{name}' nicht gefunden.")
