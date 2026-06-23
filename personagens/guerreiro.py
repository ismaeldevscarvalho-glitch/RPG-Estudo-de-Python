from personagens.personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            classe="Guerreiro Maculado",
            pv=10,
            defesa=13,
            forca=2,
            agilidade=1,
            esperteza=-1,
            imunidade=0

        )