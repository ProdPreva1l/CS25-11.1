from abc import ABC, abstractmethod

class Damager(ABC):
    @property
    @abstractmethod
    def attack_damage(self) -> int:
        pass

class Armour(ABC):
    @property
    @abstractmethod
    def absorption(self) -> int:
        pass