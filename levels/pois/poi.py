from abc import ABC

class Poi(ABC):
    def __init__(self, name: str):
        self.name = name