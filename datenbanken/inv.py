import json
import os

PLAYER_FOLDER = "player_data"


class InventoryManager:
    def __init__(self):
        pass

    def get_player_file(self, player_id):
        return os.path.join(PLAYER_FOLDER, f"{player_id}.json")

    def create_player(self, player_id):

        filepath = self.get_player_file(player_id)

        if not os.path.exists(filepath):
            data = {"player_id": player_id, "items": {}}
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True

        return False

    def load_player(self, player_id):

        filepath = self.get_player_file(player_id)

        if not os.path.exists(filepath):
            return None

        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_player(self, player_id, data):
        filepath = self.get_player_file(player_id)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add_item(self, player_id, item, amount):
        data = self.load_player(player_id)
        if data is None:
            self.create_player(player_id)
        data = self.load_player(player_id)

        data["items"][item] = data["items"].get(item, 0) + amount
        self.save_player(player_id, data)
        return f"Added {amount} of {item} to player {player_id}"

    def remove_item(self, player_id, item, amount):
        data = self.load_player(player_id)
        if data is None:
            raise ValueError("Player not found")

        if item not in data["items"]:
            raise ValueError(f"Item {item} not found in inventory")

        if data["items"][item] < amount:
            raise ValueError(f"Not enough {item} to remove")

        data["items"][item] -= amount
        if data["items"][item] == 0:
            del data["items"][item]

        self.save_player(player_id, data)
        return f"Removed {amount} of {item} from player {player_id}"

    def get_inventory(self, player_id, item=None):
        data = self.load_player(player_id)
        if not data:
            self.create_player(player_id)
            data = self.load_player(player_id)
            return data["items"].get(item, 0)

        if item is None:
            return data["items"]
        else:
            return data["items"].get(item, 0)
