import time
from typing import override

from levels.level import Level
from utils.utils import menu, cls, speak, prompt_question


class Tutorial(Level):
    def __init__(self):
        super().__init__(0, "Tutorial")

    def _test_question(self):
        print("Lets try this one: ")
        correct = prompt_question(clear=False)

        time.sleep(0.3)
        cls()

        if correct:
            print("\nGood Job! Your a natural! That's all for now.")
        else:
            print("\nThat's ok, some of these questions can be tricky.")
            try_again = menu("Would you like to try again?", "Ok", "I'm good", clear=False)
            if try_again[0] == 1:
                cls()
                self._test_question()
            elif try_again[0] == 2:
                cls()

    @override
    def run(self, player):
        speak(f"""
            Hey there {player.name}, Welcome to The Parade!
            Here are some basic things you need to know!
            If you are given a menu you must input the option (usually a number) and then hit enter to confirm your selection.
            You cannot change your character, so if you chose wrong, restart now before its too late!
            Your progress is saved at the end of each stage so if you quit half way through a stage your progress will not be saved!
            
            Lets try out some of the things you may encounter while playing!
            
        """)

        time.sleep(0.5)

        print("You will encounter beasts. To be able to slay them, you must answer the question correctly!")
        self._test_question()

        ready = menu("Are you ready to continue?", "Yeah!", "Not yet...", clear=False)
        if ready[0] == 1:
            cls()
        elif ready[0] == 2:
            cls()
            input("Oh! ok... just press enter when you are!")
        speak("Great, good luck on your ventures!")
