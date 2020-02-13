# Class Item which can exist in a room and in a player's inventory


class Item:
    """class representing items that exit inside of rooms and in player's inventory"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} –– {self.description}'

    def __repr__(self):
        return f'{self.name} --- {self.description}'

    def on_take(self):
        print(f'You have picked up {self.name}')

    def on_drop(self):
        print(f'You have dropped {self.name}')
