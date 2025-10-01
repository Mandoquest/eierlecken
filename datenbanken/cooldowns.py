import json, time, os

COOLDOWN_FILE = "datenbanken/cooldowns.json"

if not os.path.exists(COOLDOWN_FILE):
    with open(COOLDOWN_FILE, "w") as f:
        json.dump({}, f)


def load_cooldowns():
    with open(COOLDOWN_FILE, "r") as f:
        return json.load(f)


def save_cooldowns(data):
    with open(COOLDOWN_FILE, "w") as f:
        json.dump(data, f, indent=4)


def check_cooldown(user_id: str, command_name: str, cd_time: int):

    cooldowns = load_cooldowns()
    now = time.time()

    if user_id in cooldowns and command_name in cooldowns[user_id]:
        last_used = cooldowns[user_id][command_name]
        if now - last_used < cd_time:
            return int(cd_time - (now - last_used))

    return 0


def update_cooldown(user_id: str, command_name: str):
    cooldowns = load_cooldowns()
    now = time.time()

    if user_id not in cooldowns:
        cooldowns[user_id] = {}
    cooldowns[user_id][command_name] = now

    save_cooldowns(cooldowns)
