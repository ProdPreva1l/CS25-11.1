from typing import override

from levels.stage import Stage
from models.items.swords import BasicSword
from models.stats import Stat
from utils.utils import prompt_question, speak, cls


class LevelTwo:
    _loot_pool = [
        BasicSword()
    ]

    _upgrade_pool = {
        Stat.AGILITY: 1,
        Stat.STRENGTH: 2,
        Stat.INTELLIGENCE: 1
    }

    def upgrade(self):
        pass

    class StageOne(Stage):
        def __init__(self):
            super().__init__(1)

        @override
        def run(self, player):
            print("Level Two: Stage One")
            correct = prompt_question(clear=False)
            if correct:
                player.next_stage()


    class StageTwo(Stage):
        def __init__(self):
            super().__init__(2)

        @override
        def run(self, player):
            cls()
            print("Level Two: Stage Two (Incorrect Previous)")
            prompt_question(clear=False)
            correct = prompt_question(clear=False)
            if not correct:
                player.set_stage(1)
            else:
                player.set_stage(-1)

    class StageThree(Stage):
        def __init__(self):
            super().__init__(3)

        @override
        def run(self, player):
            cls()
            print("Level Two: Stage Three (Correct Previous)")
            correct = prompt_question(clear=False)
            if not correct:
                player.set_stage(2)