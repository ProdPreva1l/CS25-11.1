import os
import textwrap
import time
import random

from levels.questions.question import Question
from levels.questions.question_processors import AIHandler
from levels.questions.question_type import QuestionType
from repositories.impl.question_repository import QuestionRepository


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def speak(text: str, delay: float = 0.05):
    i = 1
    for char in textwrap.dedent(text):
        time.sleep(delay)
        if i == len(text):
            end = '\n'
        else:
            end = ''
        print(char, end=end, flush=True)
        i += 1

def prompt_question(clear: bool = True) -> bool:
    if clear:
        cls()

    all_questions = QuestionRepository().get_all()
    if AIHandler().is_rate_limited():
        all_questions = [q for q in all_questions if q.question_type is not QuestionType.DEFINE]
    question: Question = random.choice(all_questions)
    answer = question.ask()
    result = question.test(answer)
    if result[0]:
        speak("Your answer is... CORRECT!")
        print(f"Well done! The correct answer was: \"{result[1]}\". Your answer: \"{answer}\"")
        return True
    else:
        speak("Your answer is... WRONG!")
        print(f"Oh no! The correct answer was: \"{result[1]}\". Your answer: \"{answer}\"")
        if question.question_type is QuestionType.DEFINE:
            print("If you believe we got this wrong, notify your teacher!")
        return False

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