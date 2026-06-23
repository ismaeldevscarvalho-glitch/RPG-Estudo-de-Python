class Equipamentos:

    def equipar_arma(self,personagem, arma):

        personagem.arma = arma

        print(f"{personagem.nome} equipou {arma.nome}.")

    def equipar_armadura(self, personagem, armadura):

        personagem.armadura = armadura

        print(f"{personagem.nome} equipou {armadura.nome}.")