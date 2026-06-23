from itens.item import Item

class Espada(Item):
    def __init__(self):
        super().__init__(
            nome="Espada de Madeira",
            peso=3,
            valor=50
        )
        self.bonus_forca = 2