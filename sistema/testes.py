from sistema.dados import Dados
from sistema.resultado_teste import ResultadoTeste

class Testes:

    @staticmethod
    def testar(personagem, atributo, dificuldade):

        atributo_obj = getattr(personagem.atributos, atributo)

        modificador = atributo_obj.total

        dado = Dados.d20()

        resultado = dado + modificador

        critico = dado == 20
        falha_critica = dado == 1

        sucesso = resultado >= dificuldade

        if critico:
            sucesso = True

        if falha_critica:
            sucesso = False

        return ResultadoTeste(
            dado,
            modificador,
            resultado,
            dificuldade,
            sucesso,
            critico,
            falha_critica
        )

        '''print("=" * 35)
        print(f"Teste de {atributo_obj.nome}")
        print(f"D20.................: {dado}")
        print(f"Atributo............: {atributo_obj.total:+}")
        print(f"Resultado...........: {total:+}")
        print(f"Dificuldade.........: {dificuldade}")
    
        if total >= dificuldade:
            print("Sucesso!")
            return True
    
        print("Falhou")
        return False
    
        return total'''