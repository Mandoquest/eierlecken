from datenbanken.inv import InventoryManager

_inv = InventoryManager()


def add_item(player_id, item, amount, category=None, tag=None):
    return _inv.add_item(player_id, item, amount, category=category, tag=tag)


def remove_item(player_id, item, amount):
    return _inv.remove_item(player_id, item, amount)


def get_inventory(player_id, item=None, category=None, tag=None):
    result = _inv.get_inventory(player_id, item=item, category=category, tag=tag)
    if item is not None:
        # If an item was requested, return its integer amount (default 0)
        if isinstance(result, dict):
            return result.get("amount", 0)
        # Fallback: if inventory returned something unexpected, try to coerce
        try:
            return int(result)
        except Exception:
            return 0

    return result
