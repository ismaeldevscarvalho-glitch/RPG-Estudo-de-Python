from personagens.personagem import Personagem


class Goblin(Personagem):

    def __init__(self):

        super().__init__(
            nome="Goblin",
            classe="Monstro",

            pv=8,
            defesa=11,

            forca=1,
            agilidade=2,
            esperteza=0,
            imunidade=0
        )