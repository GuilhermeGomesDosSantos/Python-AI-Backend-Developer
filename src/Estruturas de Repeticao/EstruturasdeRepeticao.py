"""
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")# end="", vai evitar a quebra de linha
        # print(letra)
    
print()
"""

texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")# end="", vai evitar a quebra de linha
        # print(letra)
else:

    print()
    print("Executa no final do laço")