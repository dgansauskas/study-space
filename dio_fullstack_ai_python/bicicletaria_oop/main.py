# ----------------------------------------------------------------
# --- DESAFIO ---
#
# Criar uma bicicletaria. Requisitos:
# 1 - Informar: cor, modelo, ano, tem marcha?(bool), quant_marchas, valor
# 2 - Acoes: andar, correr, parar e buzinar
# ----------------------------------------------------------------

from dataclasses import dataclass, field

@dataclass
class Bicicleta:
    cor: str
    modelo: str
    ano: int
    quant_marchas: int
    tem_marcha: bool = field(init=False)
    valor: int

    def __post_init__(self):
        self.tem_marcha = self.quant_marchas > 0

    def buzinar(self):
        print('Bibibibibibibibibibi!!!!!')
    
    def andar(self):
        print('A bicicleta está andando')

    def correr(self):
        print('A bicicleta está correndo')

    def parar(self):
        print('A bicicleta está parada')


if __name__ == '__main__':
    
    b_01 = Bicicleta(
        cor='Verde',
        modelo='Cannondale',
        ano='2015',
        quant_marchas=18,
        valor=3500)

    print(b_01)
    b_01.correr()