class ResultadoTeste:
    def __init__(self,
                 dado,
                 modificador,
                 resultado,
                 dificuldade,
                 sucesso,
                 critico,
                 falha_critica
    ):

        self.dado = dado
        self.modificador = modificador
        self.resultado = resultado
        self.dificuldade = dificuldade

        self.sucesso = sucesso
        self.critico = critico
        self.falha_critica = falha_critica

    def mostrar(self):

        print("=" * 40)
        print("           RESULTADO DO TESTE")
        print("=" * 40)
        print(f"Dado............: {self.dado}")
        print(f"Modificador.....: {self.modificador}")
        print(f"Resultado.......: {self.resultado}")
        print(f"Dificuldade.....: {self.dificuldade}")

        if self.critico:
            print("SUCESSO CRÍTICO!")
        elif self.falha_critica:
            print("FALHA CRITICA!")
        elif self.sucesso:
            print("SUCESSO!")
        else:
            print("FALHA")

        print("=" * 40)