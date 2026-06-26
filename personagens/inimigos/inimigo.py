from personagens.personagem import Personagem

class Inimigo(Personagem):
    def __init__(
            self,
            nome,
            especie,
            pv,
            defesa,
            forca,
            agilidade,
            esperteza,
            imunidade

    ):
        super().__init__(
            nome= nome,
            classe= especie,
            pv=pv,
            defesa=defesa,
            forca=forca,
            agilidade=agilidade,
            esperteza=esperteza,
            imunidade=imunidade
        )

        self.especie = especie
        self.xp = 0