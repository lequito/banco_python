menu = """
    [1] - | SACAR     |
    [2] - | DEPOSITAR |
    [3] - | EXTRATO   |
    [0] - | SAIR      |
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))

    if opcao == 2:
        valor = float(input("Informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"| Depósito: R$ {valor:.2f}\n"
        else:
            print("Falha na operação Valor inválido!!!")
    elif opcao == 1:
        
        valor = float(input("Informe o valor desejado: "))
        
        exedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        exedeu_saque = numero_saques >= LIMITE_SAQUE

        if exedeu_saldo:
            print("Falha na operação! saldo insuficiente.")
        elif exedeu_limite:
            print("Falha na operação! saque exede o limite.")
        elif exedeu_saque:
            print("Falha na operação! numero maximo de saques exedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"| Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou o valor informado é inválio")
    elif opcao == 3:
        print("========== | EXTRATO | ==========")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"Saldo R$ {saldo:.2f}")
        print("=================================")
    elif opcao == 0:
        break
    else:
        print("Operação inválida, selecione uma das opções válidas")