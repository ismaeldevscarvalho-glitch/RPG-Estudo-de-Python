from personagens.personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            classe="Mago Clériga das Cinzas",
            pv=5,
            defesa=10,
            forca=-1,
            agilidade=-1,
            esperteza=3,
            imunidade=2

        )