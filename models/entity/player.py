from typing import override

from sqlalchemy import PickleType, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.characters import Character
from models.entity.entity import Entity
from models.items.item import Item
from models.items.item_types import Armour, Damager
from repositories.impl.player_repository import PlayerRepository
from repositories.savable import Savable, Storable

class Inventory(Savable[int], Storable):
    __tablename__ = 'inventories'

    identifier: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    armour: Mapped[Armour] = mapped_column(PickleType, nullable=True)
    first: Mapped[Item] = mapped_column(PickleType, nullable=True)
    second: Mapped[Item] = mapped_column(PickleType, nullable=True)
    third: Mapped[Item] = mapped_column(PickleType, nullable=True)
    fourth: Mapped[Item] = mapped_column(PickleType, nullable=True)
    fifth: Mapped[Item] = mapped_column(PickleType, nullable=True)

    player = relationship("Player", back_populates="inventory")

    @override
    def save(self):
        PlayerRepository().save(self)


class Player(Entity, Savable[str], Storable):
    __tablename__ = 'players'

    identifier: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    intelligence: Mapped[int] = mapped_column(nullable=False)
    strength: Mapped[int] = mapped_column(nullable=False)
    agility: Mapped[int] = mapped_column(nullable=False)

    health: Mapped[float] = mapped_column(nullable=False)
    inventory_id: Mapped[int] = mapped_column(ForeignKey('inventories.identifier'), nullable=False)
    inventory: Mapped[Inventory] = relationship(
        "Inventory",
        back_populates="player"
    )

    current_level: Mapped[int] = mapped_column(nullable=False)
    current_stage: Mapped[int] = mapped_column(nullable=False)
    highest_level: Mapped[int] = mapped_column(nullable=False)

    def __init__(
            self,
            character: Character
    ) -> None:
        super().__init__()
        self.identifier = character.name
        self.character = character
        self.intelligence = character.intelligence
        self.strength = character.strength
        self.agility = character.agility
        self.health = 100
        self.inventory = Inventory()
        self.current_level = 0
        self.current_stage = 1
        self.highest_level = 0

    def next_level(self):
        self.set_level(self.current_level + 1)

    def next_stage(self):
        self.set_stage(self.current_stage + 1)

    def set_stage(self, stage):
        self.current_stage = stage

    def set_level(self, level):
        self.current_level = level
        self.current_stage = 1
        if self.highest_level < level:
            self.highest_level = level

    @override
    def damage(self, source: Damager):
        pass

    @override
    def die(self):
        """todo: finish this """
        input("You died! Press Enter to continue...\n")

    @property
    @override
    def max_health(self):
        return 100

    @property
    def name(self) -> str:
        return self.identifier

    @override
    def save(self):
        PlayerRepository().save(self)