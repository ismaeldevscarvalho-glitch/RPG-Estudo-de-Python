from sistema.dados import Dados

class Testes:

    @staticmethod
    def testar(personagem, atributo, dificuldade):

        atributo_obj = getattr(personagem.atributos, atributo)


        dado = Dados.d20()

        total = dado + atributo_obj.total

        print("=" * 35)
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

        return total