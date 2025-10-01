import os 
import json



FILE_PATH = "antispam.json"

LIMIT_STUFEN = ["aus", "leicht", "mittel", "stark"]

def load_config():
    """Lädt die Konfigurationsdatei oder erstellt sie, wenn sie nicht existiert."""
    if not os.path.isfile(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump({}, f)

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        with open(FILE_PATH, "w") as f:
            json.dump({}, f)
        return {}

def save_config(config):
    """Speichert das gegebene Config-Dictionary."""
    with open(FILE_PATH, "w") as f:
        json.dump(config, f, indent=4)

def get_messagelimit_status(guild_id: int) -> str:
    """Gibt die aktuelle Limit-Stufe für einen Server zurück. Standard: 'aus'"""
    config = load_config()
    return config.get(str(guild_id), {}).get("Limit_level", "aus")

def set_message_limit(guild_id: int, level: str) -> bool:
    """
    Setzt die Limit-Stufe für einen Server.
    Rückgabe: True bei Erfolg, False bei ungültiger Eingabe.
    """
    if level not in LIMIT_STUFEN:
        return False

    config = load_config()
    config.setdefault(str(guild_id), {})["Limit_level"] = level
    save_config(config)
    return True

def cycle_message_limit(guild_id: int) -> str:
    """
    Schaltet zur nächsten Limit-Stufe weiter.
    Rückgabe: neue Limit-Stufe als String.
    """
    current = get_messagelimit_status(guild_id)
    index = LIMIT_STUFEN.index(current)
    next_index = (index + 1) % len(LIMIT_STUFEN)
    new_level = LIMIT_STUFEN[next_index]
    set_message_limit(guild_id, new_level)
    return new_level