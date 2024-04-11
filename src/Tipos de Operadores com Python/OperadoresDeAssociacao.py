# são operadores utilizados para verificar se um objeto está presente em uma sequência
# usasse IN para verificar a assosiação

frutas = ['Limão', 'Uva']
curso = "Curso de Python"
print("Laranja" in frutas)
print("laranja" in frutas)

frutas = ['Limão', 'Uva', 'Laranja']
print("Laranja" in frutas)
print("laranja" in frutas)

print("laranja" not in frutas)
print("limao" not in frutas)

print("Python" in curso)
