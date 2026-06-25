from itens.arma import Arma

class EspadaMadeira(Arma):
    def __init__(self):
        super().__init__(
            nome="Espada de Madeira",
            peso=3,
            valor=50,
            dano="1d6",
            atributo="forca"
        )
class EspadaLonga(Arma):
    def __init__(self):
        super().__init__(
            nome="Espada Longa",
            peso=6,
            valor=70,
            dano="1d8",
            atributo="forca"

        )

class Cajado(Arma):
    def __init__(self):
        super().__init__(
            nome="Cajado do Infinito",
            peso=2,
            valor=45,
            dano="1d6",
            atributo="esperteza"
        )

class Adaga(Arma):
    def __init__(self):
        super().__init__(
            nome="Adaga Fina",
            peso=3,
            valor=50,
            dano="1d4",
            atributo="agilidade"
        )