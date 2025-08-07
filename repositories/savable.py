from typing import TypeVar

from sqlalchemy.orm import DeclarativeBase

class Storable(DeclarativeBase):
    pass

K = TypeVar('K')

class Savable[K]:
    identifier: K

    def save(self):
        """Save the object into the database"""
        pass
