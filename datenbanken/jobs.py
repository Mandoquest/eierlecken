import json
import os

FILENAME = "datenbanken/jobs.json"


def _load_all():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, "r", encoding="utf-8") as file:
        return json.load(file)


def _save_all(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def set_job(user_id: int, job: str):

    # job setzen bzw überschreiben

    data = _load_all()
    data[str(user_id)] = job
    _save_all(data)
    return f"Job für Nutzer {user_id} wurde auf '{job}' gesetzt."


def get_job(user_id: int):

    # job ausgeben None falls nicht vorhaben

    data = _load_all()
    return data.get(str(user_id))


def remove_job(user_id: int):

    # job entfernen

    data = _load_all()
    if str(user_id) in data:
        del data[str(user_id)]
        _save_all(data)
        return f"Job für Nutzer {user_id} wurde entfernt."
    return "Kein Job vorhanden, der entfernt werden kann."
