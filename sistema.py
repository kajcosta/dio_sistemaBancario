saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""
while True:
    menu = int(input("""Bem-vindo ao ElphBank!
Selecione a opção desejada:
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
"""))
    match menu:
        case 1:
            valor = float(input("Digite o valor a ser depositado: R$"))
            if valor < 1:
                print("Operação falhou! O valor informado é inválido.\n")
            else:
                saldo += valor
                print(f"Deposito de R$ {valor:.2f} realizado com sucesso.\n")
                extrato += f"Deposito: R$ {valor:.2f}\n"
        case 2:
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if valor < 0:
                print("Valor inválido.\n")
            elif valor > limite:
                print("Saque indisponível. O valor ultrapassa o limite.\n")
            elif numero_saques >= LIMITE_SAQUES:
                print("Limite de saques diários atingido.\n")
            elif valor > saldo:
                print("Saldo insuficiente.\n")
            else:
                saldo -= valor
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
                extrato += f"Saque: R$ {valor:.2f}\n"
        case 3:
            if extrato == "":
                print("Não foram realizadas movimentações.\n")
            else:
               print(f"Saldo atual: R$ {saldo:.2f}\n", extrato)
        case 4:
            print("Obrigado por usar o ElphBank. Até logo!")
            break
        case _:
            print("Opção inválida.\n")
