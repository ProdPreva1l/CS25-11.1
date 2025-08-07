from levels.questions import question_processors
from levels.questions.question_type import QuestionType
from repositories.savable import Savable

class Question(Savable[str]):
    def __init__(self, question_type: QuestionType, word: str, *answers: str):
        self.question_type = question_type
        self.word = word
        self.identifier = word
        self.answers = answers

        if question_type.requires_answer and len(answers) == 0:
            raise ValueError(f"Answer cannot be None for {question_type}")

    def test(self, answer: str) -> (bool, str):
        match self.question_type:
            case QuestionType.UNSCRAMBLE:
                return question_processors.test_unscramble(self, answer)
            case QuestionType.CORRECT:
                return question_processors.test_correct(self, answer)
            case QuestionType.COMPLETE:
                return question_processors.test_complete(self, answer)
            case QuestionType.DEFINE:
                return question_processors.test_define(self, answer)
        return False, "Unknown"

    def ask(self) -> str:
        replacement = self.word
        match self.question_type:
            case QuestionType.UNSCRAMBLE:
                replacement = question_processors.scramble(self.word)
            case QuestionType.COMPLETE:
                replacement = question_processors.hide(self.word)
        return input(self.question_type.text.replace("%word%", replacement))