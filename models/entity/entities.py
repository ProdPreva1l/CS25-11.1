from typing import override

from models.entity.entity import Entity

class DandelionDestroyer(Entity):
    _health = 25

    @property
    @override
    def max_health(self) -> int:
        return 25

    @property
    @override
    def health(self) -> int:
        return self._health

    @property
    @override
    def name(self) -> str:
        return "DandelionDestroyer"

    @override
    def die(self):
        pass