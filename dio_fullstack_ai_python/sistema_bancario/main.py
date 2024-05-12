# --------------------------------------------------------------------------------------------
# --- DESAFIO ---
#
# Criar uma conta bancária com os seguintes requisitos:
# máximo de 3 saques diários com limite máximo de R$500,00 por saque
# Caso não tenha saldo em conta, informar "Saldo Insuficiente"
# Todos os saques devem ser armazenados em uma variável e exibidos na operação "Extrato"
# --------------------------------------------------------------------------------------------

# Import das libs necessarias
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import ClassVar, List, Dict, Literal
from numbers import Number
import sys


@dataclass
class Cliente:
    '''
    Criação da classe Cliente
    '''

    # Gerador de ID: variável de classe checar o próximo id disponível
    _id_gen: ClassVar[int] = 1

    # Atributos da classe Cliente
    id: int = field(init=False, repr=True)  # o `id` será gerado automaticamente depois de inicializar a classe
    nome: str
    sobrenome: str
    data_nascimento: date
    cidade: str
    estado: str
    pais: str
    

    def __post_init__(self):

        # Define o ID da Cliente e incrementa o gerador de ID
        self.id = Cliente._id_gen
        Cliente._id_gen += 1


@dataclass
class ContaCorrente(Cliente):
    '''
    Criação da classe ContaCorrente
    '''

    _id_cc_gen: ClassVar[int] = 1

    id_cc: int = field(init=False, repr=True)
    agencia: int
    banco: int = 22
    saldo: float = 0
    id_conta:str = field(init=False, repr=True)
    nome_completo: str = field(init=False)

    # Definição de como será salvo os registros nas transações
    transacoes: Dict[int, Dict[str, object]] = field(default_factory=dict)
    _id_evento_gen: ClassVar[int] = 0  # Gerador de ID para eventos

    def __post_init__(self) -> None:
        # Gerar número do id da conta
        self.id_cc = ContaCorrente._id_cc_gen
        ContaCorrente._id_cc_gen += 1
        
        id_conta = f'{str(self.banco).zfill(3)}.{str(self.agencia).zfill(4)}.{str(self.id_cc).zfill(4)}'
        self.nome_completo = f"{self.nome} {self.sobrenome}"

    def contar_transacoes_do_dia(self, var_datetime) -> bool:
        count = 0
        for self.id_evento, self.evento in self.transacoes.items():
            if self.evento['datetime_evento'].date() == var_datetime.date():
                count +=1
        if count > 3:
            return False
        else:
            return True

    def adicionar_evento(self, tipo_evento: str, datetime_evento: datetime, nome_evento: str, valor_evento: float) -> None:
        if tipo_evento not in ['saque', 'deposito']:
            print("Tipo de evento deve ser 'saque' ou 'deposito'.")
            sys.exit()
        elif not isinstance(valor_evento, Number):
            print("O depósito precisa ser um valor numérico")
            sys.exit()
        elif tipo_evento == 'deposito' and valor_evento < 0:
            print("O depósito precisa ser um valor positivo")
            sys.exit()
        elif tipo_evento == 'saque' and valor_evento > 0:
            print("O saque precisa ser um valor negativo")
            sys.exit()
        elif self.contar_transacoes_do_dia(datetime_evento) is False:
            print("A quantidade máxima de saques diários já foi realizada")
            sys.exit()
        elif tipo_evento == 'saque' and valor_evento < -500:
            print("O valor máximo para saque é de R$500,00")
            sys.exit()

        id_evento = ContaCorrente._id_evento_gen
        ContaCorrente._id_evento_gen += 1

        self.transacoes[id_evento] = {
            'tipo_evento': tipo_evento,
            'datetime_evento': datetime_evento,
            'nome_evento': nome_evento,
            'valor_evento': valor_evento
        }

        self.saldo = self.saldo + valor_evento

        print(f'{tipo_evento} no dia {datetime_evento.date()} às {datetime_evento.hour}h{datetime_evento.minute}m no valor de R${float(valor_evento):.2f} realizado com sucesso')

    def extrato(self, data_inicio:date, data_fim:date):
        
        if not isinstance(data_inicio, date) and (data_fim, date):
            data_fim,data_inicio = date.today(), data_fim - timedelta(days=7)
        
        registro_extrato = ""
        for self.id_evento, self.evento in self.transacoes.items():
            if data_inicio <= self.evento['datetime_evento'].date() <= data_fim:
                registro_extrato += f"ID: {self.id_evento} - TIPO: {self.evento['tipo_evento'][0].upper()} - DATA/HORA: {self.evento['datetime_evento']} - EVENTO: {self.evento['nome_evento'].ljust(10,' ')} - VALOR: {self.evento['valor_evento']:.2f}\n"

        if not registro_extrato:
            result= 'Não há registro de transações no periodo escolhido!'
        else:
            result= registro_extrato
        
        return modelo_extrato(self.banco,self.agencia,self.id_cc,self.nome_completo.upper(),data_inicio,data_fim,result, self.saldo)


def modelo_extrato(num_banco,num_agencia, num_conta, nome_cliente, data_ini, data_fim, movimentacoes, saldo) -> None:
    print(f"""
---------------------------------------------------------------------------------------------------
BANCO XPTO {str(num_banco).zfill(3)} | AGENCIA {str(num_agencia).zfill(4)} | CONTA: {str(num_conta).zfill(4)} | DATA RELATORIO: {datetime.today().strftime('%Y-%m-%d %H:%M')}
---------------------------------------------------------------------------------------------------

CLIENTE: {nome_cliente}

RELATORIO DE TRANSACOES ENTRE OS DIAS {data_ini} E {data_fim}

{movimentacoes}

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SALDO ATUAL: R${saldo}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


----------------------------------------------------------------------------------------------------
""")


# --------------------------------------------------------------------------------------------
# Teste de cenario

if __name__ == '__main__':


    cc_01 = ContaCorrente(nome="Maria", sobrenome="Ferreira", data_nascimento=date(1985, 4, 12), cidade="Curitiba", estado="PR", pais="Brasil",agencia=37)

    # # exemplo de como o erro acontece ao tentar retirar um valor acima do saldo
    # cc_01.adicionar_evento('saque',datetime(2024,4,12,10,30),'retirada_tentativa',300)

    cc_01.adicionar_evento('deposito',datetime(2024,4,12,10,30),'deposito',5000)
    cc_01.adicionar_evento('saque',datetime(2024,4,12,11,35),'saque',-300)
    cc_01.adicionar_evento('saque',datetime(2024,4,12,12,35),'saque',-300)
    cc_01.adicionar_evento('saque',datetime(2024,4,12,15,50),'saque',-500)
    cc_01.adicionar_evento('saque',datetime(2024,4,14,11,35),'saque',-230)
    print(cc_01.saldo)

    cc_01.extrato(date(2024,4,10),date(2024,4,20))