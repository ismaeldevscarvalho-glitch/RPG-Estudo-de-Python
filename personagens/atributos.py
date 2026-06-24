from personagens.atributo import Atributo

class Atributos:

    def __init__(self, forca, agilidade, esperteza, imunidade):

        self.forca = Atributo("Força", forca)
        self.agilidade = Atributo("Agilidade", agilidade)
        self.esperteza = Atributo("Esperteza", esperteza)
        self.imunidade = Atributo("Imunidade", imunidade)

    def mostrar(self):

        print("===== ATRIBUTOS =====")
        print(self.forca.mostrar())
        print(self.agilidade.mostrar())
        print(self.esperteza.mostrar())
        print(self.imunidade.mostrar())