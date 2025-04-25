from abc import ABC, abstractmethod

class Stage(ABC):
    def __init__(self, stage: int, level):
        self.stage = stage
        self._level = level

    @abstractmethod
    def run(self, player):
        """Run the stage"""
        pass