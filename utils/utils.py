import os
import textwrap
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def speak(text: str, delay: float = 0.05):
    for char in textwrap.dedent(text):
        time.sleep(delay)
        print(char, end='', flush=True)

def menu(prompt: str, *args: str, clear: bool = True) -> (int, str):
    if args is None:
        raise Exception("No arguments provided for menu")

    if clear:
        cls()

    text = prompt + "\n"
    for idx, arg in enumerate(args, 1):
        text += f" {idx}. {arg}\n"

    result = input(text)

    if not result.isnumeric():
        return menu(prompt + " (You did not enter a valid option!)", *args)

    num = int(result)

    if args[num - 1] is None:
        return menu(prompt + " (You did not enter a valid option!)", *args)

    return num, args[num - 1]