import atexit

import shared
from models.characters import Character
from models.entity.player import Player
from repositories.impl.level_repository import LevelRepository
from repositories.impl.player_repository import PlayerRepository
from utils.utils import menu, cls, speak
from repositories.connection_manager import ConnectionManager

def character_select(extra = "") -> Character:
    cls()

    result = input(
f"""
Choose your character, you get a base set of stats that you can upgrade later on! {extra}
1. Luna
   | Intelligence: 30
   | Strength: 70
   | Agility: 50
2. Roxy
   | Intelligence: 80
   | Strength: 40
   | Agility: 30
3. Baker
   | Intelligence: 30
   | Strength: 35
   | Agility: 85
4. Dom
   | Intelligence: 20
   | Strength: 85
   | Agility: 45
"""
    )

    if not result.isnumeric():
        return character_select("(You did not enter a valid option!)")

    num = int(result)

    if num == 1:
        return Character.luna()
    elif num == 2:
        return Character.roxy()
    elif num == 3:
        return Character.baker()
    elif num == 4:
        return Character.dom()
    else:
        return character_select("(You did not enter a valid option!)")

def main():
    shared.test_mode = False
    ConnectionManager().initialize()
    start_result: (int, str) = menu("Welcome to The Parade!", "Start New Game", "Load From Save", "Quit")
    if start_result[0] == 1:
        new_game()
    elif start_result[0] == 2:
        load_game()
    elif start_result[0] == 3:
        quit()

def new_game():
    character = character_select()

    current = PlayerRepository().get(character.name)
    if current is not None:
        override = menu("You already have a save with this character!", "Load From Save", "Override",
                        "Choose Different Character")

        if override[0] == 1:
            start_game(current)
        elif override[0] == 2:
            player = Player(character)
            start_game(player)
    start_game(Player(character))


def load_game():
    cls()
    saves: list[Player] = PlayerRepository().get_all()
    if saves is None or len(saves) == 0:
        print("No saves found! Prompting to start a new game...")
        new_game()
        return

    save_dict: dict[str, Player] = {}
    for save in saves:
        save_dict[save.identifier] = save

    save_result: (int, str) = menu("Choose a Save", *save_dict.keys())
    player = save_dict[save_result[1]]

    start_game(player)


# Main game loop
def start_game(player: Player):
    shared.current_player = player
    level = LevelRepository().get(player.current_level)
    if level.identifier == 0:
        skip = menu("Would you like to skip the tutorial?", "Yes, lets get stated!",
                    "Nah, I still need to get the hang of it.")
        if skip[0] == 1:
            player.next_level()

    while not shared.exited:
        level = LevelRepository().get(player.current_level)
        cls()
        if level is None:
            speak("Woah! You complete the game! Good job.")
            print("Check back later to see if we have more content for you to play!")
            break
        print(f"Level {level.identifier} - {level.name}")
        level.run(player)
        player.next_level()
        player.save()


@atexit.register
def on_exit():
    if shared.exited or shared.test_mode: return
    shared.exited = True
    print("Game Closing!")
    if shared.current_player is not None:
        shared.current_player.save()
    ConnectionManager().shutdown()
    print("Thank you for playing!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        on_exit()
