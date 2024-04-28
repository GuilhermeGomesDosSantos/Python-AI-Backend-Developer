"""
while True:

    numeros = int(input("Informe um número: "))

    if numeros == 10:
        break

print(numeros)
"""

"""
for numero in range(100):

    # if numero == 12:
        # break

    print(numero, end=" ")
"""
"""
for numero in range(100):

    if numero == 12:
        continue

    print(numero, end=" ")
"""

"""
for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")
"""

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)
