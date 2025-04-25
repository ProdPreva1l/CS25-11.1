class Character:
    def __init__(
            self,
            name: str,
            intelligence: int,
            strength: int,
            agility: int,
    ):
        self.name = name
        self.intelligence = intelligence
        self.strength = strength
        self.agility = agility

    @staticmethod
    def luna():
        return Character(
            "Luna",
            30,
            70,
            50
        )

    @staticmethod
    def roxy():
        return Character(
            "Roxy",
            80,
            40,
            30
        )

    @staticmethod
    def baker():
        return Character(
            "Baker",
            30,
            35,
            85
        )

    @staticmethod
    def dom():
        return Character(
            "Dom",
            20,
            85,
            45
        )