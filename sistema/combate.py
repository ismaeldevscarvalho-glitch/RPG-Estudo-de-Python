from sistema.testes import Testes
from sistema.dados import Dados

from sistema.resultados.resultado_ataque import ResultadoAtaque


class Combate:

    @staticmethod
    def atacar(atacante, alvo):

        arma = atacante.arma

        teste = Testes.testar(
            atacante,
            arma.atributo,
            alvo.defesa
        )

        if not teste.sucesso:

            return ResultadoAtaque(
                atacante,
                alvo,
                teste,
                None,
                0,
                False
            )

        rolagem_dano = Dados.rolar(
            arma.dano
        )

        modificador = getattr(
            atacante.atributos,
            arma.atributo
        ).total

        dano_total = rolagem_dano.total + modificador

        if teste.critico:
            dano_total *= 2

        return ResultadoAtaque(
            atacante,
            alvo,
            teste,
            rolagem_dano,
            dano_total,
            True
        )