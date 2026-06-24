from sistema.dados import Dados

class Testes:

    @staticmethod
    def testar(personagem, atributo):

        atributo_obj = getattr(personagem.atributos, atributo)

        modificador = atributo_obj.total

        dado = Dados.d20()

        total = dado + modificador

        print(f"D20: {dado}")
        print(f"{atributo.capitalize()}: {modificador:+}")
        print(f"Resultado: {total}")

        return total