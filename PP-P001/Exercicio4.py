
nome_completo = "Lucas Silva"

nome, sobrenome = nome_completo.rsplit(' ', 1)
if nome < sobrenome:
    print(f"{nome} antecede {sobrenome} na ordem alfabética.")
else:
    print(f"{sobrenome} antecede {nome} na ordem alfabética.")

len_nome = len(nome)
len_sobrenome = len(sobrenome)
print(f"Quantidade de caracteres em '{nome}': {len_nome}")
print(f"Quantidade de caracteres em '{sobrenome}': {len_sobrenome}")

# Verifique se seu nome é uma palíndromo
nome_sem_espacos = nome_completo.replace(" ", "").lower()
if nome_sem_espacos == nome_sem_espacos[::-1]:
    print(f"{nome_completo} é um palíndromo.")
else:
    print(f"{nome_completo} não é um palíndromo.")
