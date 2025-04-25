from abc import ABC, abstractmethod

class Item(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def available_uses(self) -> int:
        pass

    @property
    @abstractmethod
    def max_uses(self) -> int:
        pass

    @abstractmethod
    def use(self, player):
        """Make player use the item."""
        pass