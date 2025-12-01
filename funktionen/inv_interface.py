from datenbanken.inv import InventoryManager

_inv = InventoryManager()


def add_item(player_id, item, amount):
    return _inv.add_item(player_id, item, amount)


def remove_item(player_id, item, amount):
    return _inv.remove_item(player_id, item, amount)


def get_inventory(player_id, item=None):
    return _inv.get_inventory(player_id, item)
