from __future__ import annotations

import json
import os
import tempfile
from typing import Dict, Optional


def _db_path() -> str:
    return os.path.join(os.path.dirname(__file__), "sprachkanaele.json")


def _load_data() -> Dict[str, int]:
    path = _db_path()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {str(k): int(v) for k, v in data.items()}
    except (json.JSONDecodeError, ValueError):
        return {}


def _save_data(data: Dict[str, int]) -> None:
    path = _db_path()
    dirpath = os.path.dirname(path)
    os.makedirs(dirpath, exist_ok=True)
    fd, tmp = tempfile.mkstemp(
        dir=dirpath, prefix="." + os.path.basename(path), text=True
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass


def get_channel(guild_id: int) -> Optional[int]:
    data = _load_data()
    v = data.get(str(guild_id))
    if v is None:
        return None
    return int(v)


def set_channel(guild_id: int, channel_id: Optional[int]) -> None:
    data = _load_data()
    key = str(guild_id)
    if channel_id is None:
        data.pop(key, None)
    else:
        data[key] = int(channel_id)
    _save_data(data)


def remove_guild(guild_id: int) -> None:
    set_channel(guild_id, None)


def all_guilds() -> Dict[int, int]:
    return {int(k): int(v) for k, v in _load_data().items()}


__all__ = ["get_channel", "set_channel", "remove_guild", "all_guilds"]
