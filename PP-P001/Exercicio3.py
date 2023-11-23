#Imprimir cada caractere numérico e seu código numérico
for i in range(10):
    caractere = chr(ord('0') + i)
    codigo_numerico = ord(caractere)
    
    print(f"'{caractere}' - {codigo_numerico}")
    
#Imprimir cada caractere numérico e seu código numérico em decimal, octal e hexadecimal
for i in range(10):
    caractere = chr(ord('0') + i)
    codigo_numerico = ord(caractere)
    
    print(f"'{caractere}' - Decimal: {codigo_numerico}, Octal: {oct(codigo_numerico)}, Hexadecimal: {hex(codigo_numerico)}")
    
# Ler um caractere da entrada padrão
caractere_lido = input("Digite um caractere: ")
codigo_numerico = ord(caractere_lido)
print(f"'{caractere_lido}' - Decimal: {codigo_numerico}, Octal: {oct(codigo_numerico)}, Hexadecimal: {hex(codigo_numerico)}")


"""Em Python, a manipulação de caracteres especiais, como 'ç' e 'ã', é tratada de maneira natural, 
e você pode usar esses caracteres diretamente em strings. Python suporta a codificação Unicode, 
o que permite trabalhar com uma ampla variedade de caracteres especiais."""
exemplo_caracteres_especiais = "çã"
print(f"Exemplo com caracteres especiais: '{exemplo_caracteres_especiais}'")


