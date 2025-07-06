from abc import ABC, abstractmethod

class Stage(ABC):
    def __init__(self, stage: int):
        self.stage = stage

    @abstractmethod
    def run(self, player):
        """Run the stage"""
        pass