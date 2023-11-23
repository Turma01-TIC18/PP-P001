# Operadores Aritméticos
a = 5.0
b = 2.0

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

# Operadores Aritméticos Compostos
a += 1
b *= 3

print(f"Após incremento de a: {a}")
print(f"Após multiplicação de b por 3: {b}")


# Maior potência de 2 representável
maior_potencia = 2.0 ** 1023
print(f"Maior potência de 2 representável: {maior_potencia}")

# Menor potência de 2 representável
menor_potencia = 2.0 ** -1022
print(f"Menor potência de 2 representável: {menor_potencia}")

# Variáveis numéricas são imutáveis
num = 3.14
print("Valor original:", num)

# Tentativa de alterar o valor
# Isso não funciona para variáveis numéricas em Python
num = num + 2.0
print("Novo valor:", num)

# Métodos disponíveis para variáveis de ponto flutuante
num = 3.14

# Método para converter o número em string
str_num = num.__str__()
print("Convertido para string:", str_num)

# Método para arredondar para o inteiro mais próximo
round_num = round(num)
print("Arredondado:", round_num)
