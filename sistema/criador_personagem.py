from personagens.guerreiro import Guerreiro
from personagens.mago import Mago
from personagens.danger import Danger

class CriadorPersonagem:

    def __init__(self):
        self.personagem = None

    def criar_personagem(self):

        print("=" * 40)
        print("      CRIAR PERSONAGEM")
        print("=" * 40)

        nome = input("Nome do personagem: ")

        print("\nEscolha uma classe")
        print("[1] Guerreiro Maculado")
        print("[2] Mago Clériga das Cinzas")
        print("[3] Danger Pária das Sombras")

        while True:

            escolha = input("\nOpção: ")
            if escolha == "1":
                self.personagem = Guerreiro(nome)
                break
            elif escolha == "2":
                self.personagem = Mago(nome)
                break
            elif escolha == "3":
                self.personagem = Danger(nome)
                break
            else:
                print("Opção invalida!")
        print("\nPersonagem criado com sucesso!")
        return self.personagem