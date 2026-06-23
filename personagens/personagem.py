from personagens.atributos import Atributos

class Personagem:
    def __init__(self, nome, classe, pv, defesa, forca, agilidade,
                 esperteza, imunidade
                 ):

        self.nome = nome
        self.classe = classe

        self.pv = pv
        self.pv_max = pv

        self.defesa = defesa

        self.atributos = Atributos(
            forca,
            agilidade,
            esperteza,
            imunidade
        )

        # Inventário
        self.inventario = []
        self.ouro = 0

        # Equipamentos
        self.arma = None
        self.armadura = None

    def mostrar_ficha(self):

        print("=" *40)
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print("=" * 40)

        print(f"PV: {self.pv}/{self.pv_max}")
        print(f"Defesa: {self.defesa}")

        self.atributos.mostrar()

        print("=" * 40)

        print("\nEquipamentos")
        if self.arma:
            print(f"Arma:{self.arma.nome}")
        else:
            print("Arma: Nenhema")

        if self.armadura:
            print(f"Armadura: {self.armadura.nome}")
        else:
            print("Armadura: Nenhema")

        print("=" * 40)