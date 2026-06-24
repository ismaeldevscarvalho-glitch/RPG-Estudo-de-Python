from sistema.criador_personagem import CriadorPersonagem
from sistema.equipamentos import Equipamentos

from itens.armas import Espada
from itens.armadura import Armadura

from sistema.testes import Testes
from personagens.atributo import Atributo

criador = CriadorPersonagem()
jogador = criador.criar_personagem()

equip = Equipamentos()

equip.equipar_arma(jogador, Espada())
equip.equipar_armadura(jogador, Armadura())

jogador.mostrar_ficha()

print()

resultado = Testes.testar(jogador, "forca", 15)