from levels.questions.question import Question
from levels.questions.question_type import QuestionType
from repositories.repository import ImmutableRepository

class QuestionRepository(ImmutableRepository[str, Question]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(QuestionRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super(QuestionRepository, self).__init__()
        self._register(Question(QuestionType.CORRECT, "Paneting", "Painting"))
        self._register(Question(QuestionType.UNSCRAMBLE, "Banana"))
        self._register(Question(
            QuestionType.DEFINE,
            "Radiator",
            "a thing that radiates or emits light, heat, or sound."
        ))