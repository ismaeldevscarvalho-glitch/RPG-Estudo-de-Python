from sistema.dados import Dados
from sistema.resultados.resultado_teste import ResultadoTeste

class Testes:

    @staticmethod
    def testar(personagem, atributo, dificuldade):

        atributo_obj = getattr(personagem.atributos, atributo)

        modificador = atributo_obj.total

        rolagem = Dados.rolar("1d20")

        resultado_dado = rolagem.total

        resultado_final = resultado_dado + modificador

        critico = resultado_dado == 20
        falha_critica = resultado_dado == 1

        sucesso = resultado_final >= dificuldade

        if critico:
            sucesso = True

        if falha_critica:
            sucesso = False

        return ResultadoTeste(
            rolagem,
            modificador,
            resultado_final,
            dificuldade,
            sucesso,
            critico,
            falha_critica
        )
