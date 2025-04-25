from abc import ABC, abstractmethod

import shared
from levels.stage import Stage
from repositories.savable import Savable

class Level(Savable[int], ABC):
    def __init__(self, identifier: int, name: str):
        self.identifier = identifier
        self.name = name

    @abstractmethod
    def run(self, player):
        """Run the level"""
        pass

    def save(self):
        raise NotImplementedError("Levels cannot be saved")

class Staged(ABC):
    _stages: dict[int, Stage] = {}

    def run_staged(self, player):
        """Run staged instead of just 1 part"""
        while not shared.exited:
            stage = self._stages.get(player.current_stage)
            if stage is None: break
            stage.run(player)
            player.next_stage()

    def _register_stage(self, stage):
        self._stages[stage.stage] = stage