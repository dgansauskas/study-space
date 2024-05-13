# ----------------------------------------------------------------------------------
# ---- DESAFIO ----
#
# 1.0 - Criar funções para operações existentes: saque, deposito e extrato
    # 1.1 - A função saque deve receber apenas por keywords. 
    #       Sugestões de argumentos: saldo, valor do extrato, limite, numero_saques, limite_saques
    #       Sugestão de retorno: saldo e extrato
    # 1.2 - A função depósito deve receber argumentos apenas por posição
    #       Sugestão de argumentos: saldo, valor e extrato
    #       Sugestão de retorno: saldo e extrato
    # 1.3 - A função de extrato deve receber argumentos por posição e nome.
    #       Argumentos posicionais: saldo; argumentos nomeados: extrato
# 2.0 - Criar duas novas funções: criar cliente do banco e criar conta corrente
    #       Pode criar mais funções. Ex.: listar contas
# 3.0 - O programa deve armazenar o usuário em uma lista.
    # 3.1 - Um cliente é composto por: nome, data de nascimento, cpf e endereco
    # 3.2 - O endereço é uma string com o formato: logradouro - numero - bairro - cidade/sigla_estado.
    # 3.3 - Deve ser armazenado apenas os numeros do CPF.
    # 3.4 - Não podemos cadastrar dois usuários com o mesmo CPF.
# 4.0 - O programa deve armazenar as contas correntes em uma lista.
    # 4.1 - Uma conta é composta por: agencia, numero da conta, e usuário.
    # 4.2 - O numero da conta é sequencial, iniciando em 1.
    # 4.3 - O numero da agência é fixo: '0001'.
    # 4.4 - O usuário pode ter mais de uma conta. Mas uma conta pertence apenas a um usuário
# ----------------------------------------------------------------------------------
import textwrap


def menu():
    menu="""

    [1]\tDeposito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNovo Cliente
    [5]\tNova Conta
    [6]\tListar Contas
    [7]\tListas Clientes
    [8]\tSair
    => """
    return input(textwrap.dedent(menu))


def deposito(saldo:float, extrato: str, valor: float):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\t\tR$ {valor:.2f}\n"
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def saque(saldo:float, numero_saques:int, limite:int, extrato:str, limite_saques:int, valor:float):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:   \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso! ===")
    else:
        print("@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("+=========================================")


def filtrar_clientes(cpf, bd_clientes):
    clientes_filtrados = [cliente for cliente in bd_clientes if cliente['cpf']==cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def add_cliente(bd_clientes):
    cpf = input('Informe o CPF (somente números): ')
    check_cliente = filtrar_clientes(cpf, bd_clientes)

    if check_cliente:
        print("\n@@@ Já existe um cliente cadastrado com esse CPF! @@@")
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço completo (logradouro, numero - bairro - cidade/UF): ')

    bd_clientes.append(
        {
        'nome':nome,
        'data_nascimento':data_nascimento,
        'cpf':cpf,
        'endereco':endereco
        }
    )
    print('=== Cliente adicionado com sucesso! ===')
        

def add_conta(agencia, numero_conta, bd_clientes, bd_contas):
    cpf = input('Informe o CPF do cliente (somente números): ')
    check_cliente = filtrar_clientes(cpf, bd_clientes)

    if check_cliente:
        print('\n=== Conta criada com sucesso! ===')
        bd_contas.append({
            'agencia':agencia,
            'numero_conta':numero_conta,
            'cliente': check_cliente
        })

    else:
        print('\n@@@ Usuário não encontrado, fluxo de criação de contas encerrado! @@@')

def listar_clientes(bd_clientes):
    if bd_clientes:
        for cliente in bd_clientes:
            linha = f"""
            CPF:          \t{cliente['cpf']}
            NOME:         \t{cliente['nome']}
            DT_NASCIMENTO:\t{cliente['data_nascimento']}
            ENDERECO:     \t{cliente['endereco']}
            """
            print('='*100)
            print(textwrap.dedent(linha))
    else:
        print('\n@@@ Nenhum cliente consta em nossa base! @@@')

def listar_contas(bd_contas):
    if bd_contas:
        for conta in bd_contas:
            linha = f"""\
                Agencia:        \t{conta['agencia']}
                CC:             \t{conta['numero_conta']}
                Titular:        \t{conta['cliente']['nome']}
                Data Nascimento:\t{conta['cliente']['data_nascimento']}
                Endereco:       \t{conta['cliente']['endereco']}
            """
            print('='*100)
            print(textwrap.dedent(linha))
    
    else:
        print('\n@@@ Nenhuma conta consta em nossa base! @@@')


def run():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    bd_clientes =[]
    bd_contas =[]

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(
                saldo=saldo, 
                extrato=extrato,
                valor=valor)

        elif opcao == '2':
            valor:int = float(input("Informe o valor do saque: "))
            
            saldo, extrato = saque(
                saldo=saldo, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques =LIMITE_SAQUES,
                extrato=extrato,
                valor=valor
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            add_cliente(bd_clientes)

        elif opcao == '5':
            numero_conta = len(bd_contas)+1
            conta = add_conta(
                agencia=AGENCIA, 
                numero_conta=numero_conta,
                bd_clientes=bd_clientes,
                bd_contas=bd_contas)

            if conta:
                bd_contas.append(conta)
        
        elif opcao == '6':
            listar_contas(bd_contas)

        elif opcao == '7':
            listar_clientes(bd_clientes)

        elif opcao == '8':
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == '__main__':
    run()
