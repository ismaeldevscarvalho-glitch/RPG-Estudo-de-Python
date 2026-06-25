class ResultadoAtaque:
    def __init__(
            self,
            atacante,
            alvo,
            teste,
            rolagem_dano,
            dano_total,
            acertou

    ):
        self.atacante = atacante
        self.alvo = alvo

        self.teste = teste

        self.rolagem_dano = rolagem_dano
        self.dano_total = dano_total

        self.acertou = acertou

    def mostrar(self):

        print("=" * 40)
        print("ATAQUE")
        print("=" * 40)

        print(f"Ataque  : {self.atacante.nome}")
        print(f"Alvo    : {self.alvo.nome}")

        print()

        print("TESTE DE ACERTO")
        print(F"D20..........: {self.teste.rolagem.total}")
        print(f"Modificador..: {self.teste.modificador}")
        print(f"Resultado....: {self.teste.resultado}")

        if self.acertou:

            print("\n O ataque acertou!")

            print(f"Rolagem dano....: {self.rolagem_dano.rolagens}")
            print(f"Dano total....: {self.dano_total}")

            if self.teste.critico:
                print("ACERTO CRÍTICO")


        else:

            print("\n O ataque errou!")

        print("=" * 40)
