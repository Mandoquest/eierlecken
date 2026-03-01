import os
import traceback
import datetime
import random
import asyncio
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "errors.log"


def _make_code():
    return f"ERR-{int(datetime.datetime.utcnow().timestamp())}-{random.randint(1000,9999)}"


async def report_exception(bot, exc, context=None, admin_user_id=None, admin_channel_id=None):
    """Loggt die Exception und schickt eine kurze Benachrichtigung mit Fehlercode.

    - `bot` ist die discord Bot-Instanz (Client)
    - `exc` ist das Exception-Objekt
    - `context` ist optionaler zusätzlicher Context-String
    - `admin_user_id` oder `admin_channel_id` bestimmt das Ziel der Benachrichtigung

    Liefert den generierten Fehlercode zurück.
    """
    code = _make_code()
    ts = datetime.datetime.utcnow().isoformat()
    tb = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__)) if exc else "No traceback available"
    entry = f"[{ts}] {code}\nContext: {context}\n{tb}\n\n"

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        print("Fehler beim Schreiben desError-Logs:", e)

    # Kurze Benachrichtigung (nur Zusammenfassung)
    short_msg = f"Fehler aufgetreten — Code: {code}\n{type(exc).__name__}: {str(exc)[:1800]}"

    try:
        if admin_channel_id:
            try:
                ch = await bot.fetch_channel(int(admin_channel_id))
                await ch.send(short_msg)
            except Exception:
                # Fallback: try get_channel (cache) then fetch_user
                ch = bot.get_channel(int(admin_channel_id))
                if ch:
                    await ch.send(short_msg)
        elif admin_user_id:
            user = await bot.fetch_user(int(admin_user_id))
            await user.send(short_msg)
    except Exception as send_exc:
        print("Fehler beim Senden der Fehlerbenachrichtigung:", send_exc)

    return code
