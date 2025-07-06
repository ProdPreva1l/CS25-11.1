from abc import ABC, abstractmethod
from typing import override

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

class Staged(Level):
    def __init__(self, identifier: int, name: str, *stages: Stage):
        super().__init__(identifier, name)
        self._stages: dict[int, Stage] = {}

        for stage in stages:
            self._register_stage(stage)

    @override
    def run(self, player):
        self._run_staged(player)

    def _run_staged(self, player):
        """Run staged instead of just 1 part"""
        while not shared.exited:
            stage = self._stages.get(player.current_stage)
            if stage is None: break
            stage.run(player)
            player.next_stage()

    def _register_stage(self, stage):
        self._stages[stage.stage] = stage