from abc import ABC

from models.items.item import Item
from models.entity.player import Player
from models.items.item_types import Damager


class BaseSword(Item, Damager, ABC):
    def __init__(self, name: str, max_uses: int):
        self._name = name
        self._available_uses = max_uses
        self._max_uses = max_uses

    @property
    def name(self) -> str:
        return self._name

    @property
    def available_uses(self) -> int:
        return self._available_uses

    @property
    def max_uses(self) -> int:
        return self._max_uses

    def use(self, player: Player):
        self._available_uses -= 1
        print(f"You used {self.name}!")

class BasicSword(BaseSword):
    def __init__(self):
        super().__init__('Basic Sword', 60)

    def attack_damage(self) -> int:
        return 5