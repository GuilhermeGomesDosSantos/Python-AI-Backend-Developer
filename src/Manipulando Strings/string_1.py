nome = 'guilherme'

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = '  olá mundo   '
print(texto)
print(texto.strip() + '.')
print(texto.rstrip() + '.')
print(texto.lstrip() + '.')

menu = 'Python'
# menu = 'Java'

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20, '#'))
print("P-y-t-h-o-n")
print("-".join(menu))

for letra in menu:
    print(letra, end="-")
