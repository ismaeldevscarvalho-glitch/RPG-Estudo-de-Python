from personagens.personagem import Personagem

class Danger(Personagem):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            classe="Danger Pária das Sombras",
            pv=7,
            defesa=14,
            forca=0,
            agilidade=3,
            esperteza=1,
            imunidade=-2

        )