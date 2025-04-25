from typing import override

from levels.level import Level, Staged
from levels.stage import Stage


class LevelOne(Level, Staged):
    def __init__(self):
        super().__init__(1, "The Forest")
        for s in [
            LevelOne.StageOne(self)
        ]: self._register_stage(s)

    @override
    def run(self, player):
        self.run_staged(player)

    class StageOne(Stage):
        def __init__(self, level: Level):
            super().__init__(1, level)

        @override
        def run(self, player):
            pass