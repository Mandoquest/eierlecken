import discord

def sekunden_in_stunden(sekunden):
    stunde = sekunden  // 3600
    minuten = stunde // 60
    sekunden = sekunden % 60

    return f"{stunde}h, {minuten}m and {sekunden}s"