"""
Fomos contratados por um granfe banco para desenvolver o seu novo sistema.
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 operações: déposito, saque e extrato

Deve ser possível depositar valores positivos para a minha conta bancária.
A V1 do projeto trabalha apenas com 1 usuário dessa forma não precisamos nos preocupar em identificar qual
é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variávek e exibidos na operação de extrato.

O sistema dever permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
informando que não será possível sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$1500.45
"""

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu.lower())

    if opcao == "d":
        print("Depósito")
        print("Saldo atual: R$", saldo)
        
        valorDepositar = (float) (input("Informe o valor que você deseja depositar: R$"))

        if valorDepositar > 0:
        
            saldo += valorDepositar
            print(f"SALDO ATUAL: {saldo:.2f}")

            extrato += f"Depósito: R$ {valorDepositar:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido")
    
    elif opcao == "s":
        numero_saques += 1
        if (numero_saques <= 3):
            print("Sacar")
            print("Saldo ATUAL: R$", saldo)
            valorSacar = (float) (input("Informe o valor que você deseja sacar: R$"))

            if(valorSacar <= saldo):
                saldo -= valorSacar
                print(f"O valor de R${valorSacar} foi sacado com Sucesso!")

                print(f"Saldo ATUAL: R${saldo}")
                extrato += f"Saque: R$ {valorSacar:.2f}\n"

            elif (valorSacar > saldo):
                print(f"O valor desejado de R$:{saldo}, é maior que o seu saldo atual")
                print(f"Saldo ATUAL: R${saldo}")
        elif (numero_saques > 3):
            print("Você não pode mais fazer saques porque já realizou os limite de 3 saques diários")
            break

    elif opcao == "e":
        print("\n===================Extrato===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")
        
    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada")

