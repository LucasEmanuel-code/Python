nome = str(input("Escreva seu nome: ")).strip()
print(nome.upper())
print(nome.lower())
n1 = len(nome) -nome.count(" ")
print(f'Seu nome tem: {n1} letras;')
print(nome.find(" "))