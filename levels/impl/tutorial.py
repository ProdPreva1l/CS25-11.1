from typing import override

from levels.level import Level
from utils.utils import menu, cls, speak


class Tutorial(Level):
    def __init__(self):
        super().__init__(0, "Tutorial")

    @override
    def run(self, player):
        speak(f"""
            Hey there {player.name}, Welcome to The Parade!
            Here are some basic things you need to know!
            If you are given a menu you must enter the option (usually a number) and then hit enter to confirm your selection.
            You cannot change your change your character, so if you chose wrong, restart now before its too late!
            Your progress is saved at the beginning of each stage so if you quit half way through a stage your progress will not be saved!
            
            Lets try out some of the things you may encounter while play!
        """)

        ready = menu("Are you ready to continue?", "Yeah!", "Not yet...", clear=False)
        if ready[0] == 1:
            cls()
        if ready[0] == 2:
            cls()
            input("Oh! ok... just press enter when you are!")
        speak("Great, good luck on your ventures!")
