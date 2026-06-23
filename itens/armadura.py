from itens.item import Item

class Armadura(Item):
    def __init__(self):
        super().__init__(
            nome="Armadura de Ferro",
            valor=35,
            peso=2
        )

        self.bonus_defesa = 1