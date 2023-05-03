menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=> """

Saldo = 0
Limite = 500
Extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            Saldo += valor
            Extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "b":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > Saldo

        excedeu_limite = valor > Limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo sufucuente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "c":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\nSaldo: R$ {Saldo:.2f}")
        print("======================================")
    
    elif opcao == "d":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")