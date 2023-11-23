L = [1,2,3,4,5,6,7,8,9]

print(L[::-1])

print(L[-1::])

print(L[:-1:])

print(L[::-2])

print(L[-2::])

print(L[:-2:])


#Signo no zodíaco chinês

signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

ano_nascimento = input("Digite seu ano de nascimento: ")
indice = int(ano_nascimento) % 12
print(f"Seu signo no zodíaco chinês é: {signos[indice]}")
