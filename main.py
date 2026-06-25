from sistema.criador_personagem import CriadorPersonagem
from sistema.equipamentos import Equipamentos

from itens.armas import Arma
from itens.armadura import Armadura
from itens.armas import EspadaMadeira
from sistema.testes import Testes
from personagens.atributo import Atributo

from sistema.dados import Dados

from sistema.combate import Combate
from personagens.inimigos.goblin import Goblin
from itens.armas import Adaga

criador = CriadorPersonagem()
jogador = criador.criar_personagem()

equip = Equipamentos()

equip.equipar_arma(jogador, EspadaMadeira())
equip.equipar_armadura(jogador, Armadura())

jogador.mostrar_ficha()

print()

goblin = Goblin()

equip.equipar_arma(goblin, Adaga())

resultado = Combate.atacar(
    jogador,
    goblin
)

resultado.mostrar()
