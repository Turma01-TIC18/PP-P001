#Operadores Aritméticos:
#Adição
a = 5
b = 3
resultado = a + b
print(resultado) 

#Subtração
a = 5
b = 3
resultado = a - b
print(resultado)  

#Multiplicação
a = 5
b = 3
resultado = a * b
print(resultado) 

#Divisão
a = 5
b = 3
resultado = a / b
print(resultado) 

#Divisão Inteira
a = 5
b = 3
resultado = a // b
print(resultado)  

#Módulo
a = 5
b = 3
resultado = a % b
print(resultado)  


#Operadores Aritméticos Compostos:

#Atribuição com Adição (+=)
a = 5
a += 3
print(a)  

#Atribuição com Subtração (-=)
a = 5
a -= 3
print(a)

#Atribuição com Multiplicação (*=)  
a = 5
a *= 3
print(a)  

#Atribuição com Divisão (/=)
a = 5
a /= 3
print(a)  

"""Diferenças em relação a C/C++:
- Divisão (/): Em Python, a divisão de dois inteiros resulta em um número de ponto flutuante, enquanto em C/C++, ela permaneceria 
como um número inteiro (parte inteira).

- Tipagem Dinâmica: Em Python, as variáveis não precisam ser explicitamente declaradas com um tipo, pois Python usa tipagem dinâmica.
Em C/C++, você precisa declarar o tipo da variável.

-Sem Overflow: Em Python, não há preocupação com estouro de inteiros, pois o tipo int em Python é de precisão arbitrária, 
enquanto em C/C++, pode haver problemas de estouro se não forem tratados adequadamente."""


# Calculando o fatorial de 30 em Python
fatorial_30 = 1
for i in range(1, 31):
    fatorial_30 *= i

print(f'O fatorial de 30 em Python é: {fatorial_30}')

"""Ao executar esses códigos, você notará que o fatorial de 30 em Python será calculado sem problemas, 
enquanto o maior valor inteiro representável em C/C++ (LLONG_MAX) é consideravelmente menor do que o resultado do fatorial de 30 em Python.
Isso destaca a capacidade de Python de lidar com inteiros de precisão arbitrária, o que é uma característica poderosa para manipulação 
de grandes valores inteiros."""


#Imutabilidade de variáveis numéricas
a = 5
print("Valor original de a:", a)

a = a + 2
print("Novo valor de a:", a),

"""No exemplo acima, ao realizar a = a + 2, não estamos modificando o valor original de a, 
mas criando um novo objeto int com o valor resultante de a + 2 e associando esse novo objeto à variável a"""

#Métodos disponíveis para variáveis inteiras
a = 50

# Método para converter o número em uma string
str_a = a.__str__()
print("Convertido para string:", str_a)

# Método para calcular o valor absoluto
abs_a = abs(a)
print("Valor absoluto:", abs_a)





