MAIOR_IDADE = 18
IDADE_ESPECIAL = 17


# idade = int (input("Informe sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar a CNH")

# if idade < MAIOR_IDADE:
#     print("Ainda não pode tirar a CNH")

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar a CNH")

# else:
#     print("Ainda não pode tirar a CNH")


# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar a CNH")

# elif idade == IDADE_ESPECIAL:
#     print("Pode fazer aulas teoricas, mas não pode fazer aulas praticas")

# else:
#     print("Ainda não pode tirar a CNH")



## IF ANINHADO
# conta_normal = False
# conta_universitaria = False

# saldo = 2000
# saque = 1500
# cheque_especial = 450
# conta_especial = True

# if conta_normal:
#     if saldo >= saque:
#         print("Saque realizado com sucesso!")
#     elif saque <= (saldo + cheque_especial):
#         print("Saque realizado com uso do cheque especiaç!")
#     else:
#         print("Não foi possivel realizar o saque, Saldo insuficiente!")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("Saque realizado com sucesso!")
#     else:
#         print("Saldo insuficiente!")
# elif conta_especial:
#     print("Conta especial selecionada!")

# else:
#     print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente")


## IF TERNARIO

saldo = 20000
saque = 2500
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")