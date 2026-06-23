from sistema.dados import Dados

class Testes:

    @staticmethod
    def testar(personagem, atributo):

        modificador = getattr(personagem.atributos, atributo)

        dado = Dados.d20()

        total = dado + modificador

        print(f"D20: {dado}")
        print(f"{atributo.capitalize()}: {modificador:+}")
        print(f"Resultado: {total}")

        return total