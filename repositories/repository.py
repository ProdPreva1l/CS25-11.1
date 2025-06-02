from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic, List, override

from repositories.savable import Savable

T = TypeVar('T', bound=Savable)

class Repository(ABC, Generic[T]):
    @abstractmethod
    def get(self, identifier: str) -> Optional[T]:
        """Load an item from the repository"""
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Get all items from the repository"""
        pass


class MutableRepository(Repository[T], ABC):
    @abstractmethod
    def save(self, item: T) -> None:
        """Save an item to the repository"""
        pass

    @abstractmethod
    def delete(self, item: T) -> None:
        """Delete an item from the repository"""
        pass

K = TypeVar('K')

class ImmutableRepository(Repository[Savable[K]], Generic[K, T]):
    def __init__(self):
        self._data: dict[K, T] = {}

    def _register(self, data: T):
        """Register an item to the repository"""
        self._data[data.identifier] = data

    @override
    def get(self, identifier: K) -> Optional[T]:
        """Load an item from the repository"""
        return self._data.get(identifier)

    @override
    def get_all(self) -> List[T]:
        """Get all items from the repository"""
        return list(self._data.values())
