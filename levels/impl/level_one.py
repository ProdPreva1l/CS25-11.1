from typing import override

from levels.stage import Stage
from models.items.swords import BasicSword
from models.stats import Stat
from utils.utils import prompt_question, speak


class LevelOne:
    _loot_pool = [
        BasicSword()
    ]

    _upgrade_pool = {
        Stat.AGILITY: 1,
        Stat.STRENGTH: 1,
    }

    def upgrade(self):
        pass

    class StageOne(Stage):
        def __init__(self):
            super().__init__(1)

        @override
        def run(self, player):
            correct = prompt_question()
            if not correct:
                player.next_stage()


    class StageTwo(Stage):
        def __init__(self):
            super().__init__(2)

        @override
        def run(self, player):
            pass

    class StageThree(Stage):
        def __init__(self):
            super().__init__(3)

        @override
        def run(self, player):
            pass