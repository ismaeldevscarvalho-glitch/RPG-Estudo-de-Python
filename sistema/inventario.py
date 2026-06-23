class Inventario:

    def adicionar_item(self, personagem, item):
        personagem.inventario.append(item)
        print(f"{item.nome} foi adicionado ao inventário.")

    def remover_item(self, personagem, item):

        if item in personagem.inventario:
            personagem.inventario.remover(item)
            print(f"{item.nome} foi removido.")
        else:
            print("Item não encontrado.")

    def listrar_itens(self, personagem):
        print("\n=======  INVENTÁRIO  =======")
        if len(personagem.inventario) == 0:
            print("Inventario vazio.")
            return
        for indice, item in enumerate(personagem.inventario, start=1):
            print(f"{indice}. {item.nome}")