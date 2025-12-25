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
            data = json.load(f)
        changed = False
        for item, val in list(data.get("items", {}).items()):
            if isinstance(val, int):
                data["items"][item] = {"amount": val}
                changed = True

        if changed:
            self.save_player(player_id, data)

        return data

    
    def save_player(self, player_id, data):
        filepath = self.get_player_file(player_id)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    
    
    
    
    def add_item(self, player_id, item, amount, category=None, tag=None):
        data = self.load_player(player_id)
        if data is None:
            self.create_player(player_id)
            data = self.load_player(player_id)

        if item not in data["items"]:
            data["items"][item] = {
                "amount": amount
            }
            if category is not None:
                data["items"][item]["category"] = category
            if tag is not None:
                data["items"][item]["tag"] = tag
        else:
            data["items"][item]["amount"] += amount
            if category is not None:
                data["items"][item]["category"] = category
            if tag is not None:
                data["items"][item]["tag"] = tag

        self.save_player(player_id, data)


    
    def remove_item(self, player_id, item, amount):

        data = self.load_player(player_id)
        if data is None:
            raise ValueError("Player not found")

        if item not in data["items"]:
            raise ValueError(f"Item {item} not found in inventory")

        if data["items"][item]["amount"] < amount:
            raise ValueError(f"Not enough {item} to remove")

        data["items"][item]["amount"] -= amount

        if data["items"][item]["amount"] == 0:
            del data["items"][item]

        self.save_player(player_id, data)
        return f"Removed {amount} of {item} from player {player_id}"

    
    
    
    def get_inventory(self, player_id, item=None, tag=None, category=None):
        data = self.load_player(player_id)
        if data is None:
            self.create_player(player_id)
            return {}

        items = data["items"]

        if item is not None:
            return items.get(item, {"amount": 0})

        if tag is not None:
            return {
                name: info for name, info in items.items()
                if info.get("tag") == tag
            }

        if category == "__none__":
            return {
                name: info for name, info in items.items()
                if "category" not in info
            }

        if category is not None:
            return {
                name: info for name, info in items.items()
                if info.get("category") == category
            }

        return items


