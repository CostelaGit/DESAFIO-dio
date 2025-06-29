#position: * | keywords: **


# def saque(**saldo,**valor,**extrato,**limite,**numero_saques,**limite_saques)
# sugestão de retorno: saldo e extrato

# def extrato(*saldo,**extrato)

# tem que se criar 2 funções, criar usuario e criar conta
# def criarusuario()
# possui: nome, data_nascimento, cpf, endereço,
# endereço: logradouro, bairro, cidade/sigla estado
# deve ser armazenado somente os numeros do cpf .. não se pode cadastrar 2 usuarios com cpfs iguais
# além de ter um campo com campo contas

# def criarcontacorrente()
# armazenar contas em 1 lista
# possui: agencia, numero da conta, usuario
# numero da conta sequencial, iniciando em 1
# numero da agencia é fixo: 0001
# usuario pode ter mais de 1 conta, mas uma conta só pode ter 1 usuario


# dica: vincular um usuario a uma conta, 
# filtre a lista de usuarios buscando o numero do cpf informado para cada usuario
# da lista

def menu():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuario
[nc] Nova Conta
[lc] Lista conta
[q] Sair

=> """
    return menu

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito R${valor:.2f}\n'
    else:
        print('a operação falhou. o valor informado foi invalido!')
    
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

"""
def sacar():

def exibir_extrato():

def criar_usuario():

def filtrar_usuario():

def criar_conta():

def listar_contas():"""


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = input(menu())

        if opcao == "d":
            valor = int(input('digite o quanto você deseja depositar: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        
        elif opcao == "nu":
            pass
        
        elif opcao == "nc":
            pass
        
        elif opcao == "lc":
            pass

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        

            

main()