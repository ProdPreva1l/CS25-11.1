from enum import Enum

class QuestionType(Enum):
    UNSCRAMBLE = (0, "Unscramble the word \"%word%\": ")
    DEFINE = (1, "What is the definition of \"%word%\": ", True)
    COMPLETE = (2, "Fill in the missing letters \"%word%\": ")
    CORRECT = (3, "Correct the spelling \"%word%\": ", True)

    def __init__(self, ordinal: int, text: str, requires_answer: bool = False):
        self._value_ = ordinal
        self.text = text
        self.requires_answer = requires_answer

    @property
    def ordinal(self):
        return self.value