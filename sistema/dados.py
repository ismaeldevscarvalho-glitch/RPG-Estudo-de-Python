import random

from sistema.resultados.resultado_rolagem import ResultadoRolagem

class Dados:

    @staticmethod
    def rolar(expressao):

        quantidade, faces = expressao.lower().split("d")

        quantidade = int(quantidade)
        faces = int(faces)

        rolagens = []

        for _ in range(quantidade):
            rolagens.append(random.randint(1, faces))

        return ResultadoRolagem(expressao, rolagens)
