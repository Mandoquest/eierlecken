from datenbanken.inv import InventoryManager

_inv = InventoryManager()


def add_item(player_id, item, amount, category=None, tag=None):
    return _inv.add_item(player_id, item, amount, category=category, tag=tag)


def remove_item(player_id, item, amount):
    return _inv.remove_item(player_id, item, amount)


def get_inventory(player_id, item=None, category=None, tag=None):
    return _inv.get_inventory(player_id, item=item, category=category, tag=tag)
