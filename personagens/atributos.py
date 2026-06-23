class Atributos:

    def __init__(self, forca, agilidade, esperteza, imunidade):

        self.forca = forca
        self. agilidade = agilidade
        self.esperteza = esperteza
        self.imunidade = imunidade

    def mostrar(self):

        print("===== ATRIBUTOS =====")
        print(f"Força           : {self.forca:+}")
        print(f"Agilidade       : {self.agilidade:+}")
        print(f"Esperteza       : {self.esperteza:+}")
        print(f"Iminidade       : {self.imunidade:+}")