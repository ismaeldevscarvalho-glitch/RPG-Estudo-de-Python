import random

class Dados:

    @staticmethod
    def d20():
        return random.randint(1, 20)

    @staticmethod
    def d12():
        return random.randint(1, 12)

    @staticmethod
    def d10():
        return random.randint(1, 10)

    @staticmethod
    def d8():
        return random.randint(1, 8)

    @staticmethod
    def d6():
        return random.randint(1, 6)

    @staticmethod
    def d4():
        return random.randint(1, 4)