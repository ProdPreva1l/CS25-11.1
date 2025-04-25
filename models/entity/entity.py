from abc import abstractmethod

from models.items.item_types import Damager

class Entity:
    def damage(self, source: Damager):
        """Damage the entity with a damager"""
        self.health -= source
        if self.health <= 0:
            self.die()


    @abstractmethod
    def die(self):
        """Called when the entity dies"""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """The entity's name"""
        pass

    @property
    @abstractmethod
    def health(self) -> int:
        """The entity's health"""
        pass

    @health.setter
    @abstractmethod
    def health(self, value: int) -> None:
        """Set the entity's health"""
        pass

    @property
    @abstractmethod
    def max_health(self) -> int:
        """The entity's maximum health"""
        pass