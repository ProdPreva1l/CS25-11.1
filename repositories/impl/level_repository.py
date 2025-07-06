from levels.impl.level_one import LevelOne
from levels.impl.tutorial import Tutorial
from levels.level import Level, Staged
from repositories.repository import ImmutableRepository

class LevelRepository(ImmutableRepository[int, Level]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LevelRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super(LevelRepository, self).__init__()
        self._register(Tutorial())
        self._register(Staged(
            1, "The Forest",
            LevelOne.StageOne(),

        ))