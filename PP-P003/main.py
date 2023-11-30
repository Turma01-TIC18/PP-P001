import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def validar_codigo(codigo):
    return len(codigo) == 13 and codigo.isdigit()


def validar_nome(nome):
    return nome and nome[0].isupper()


def validar_preco(preco):
    try:
        float(preco)
        return True
    except ValueError:
        return False


def inserir_produto(produtos):
    limpar_tela()
    codigo = input("Digite o código do produto (13 dígitos): ")
    while not validar_codigo(codigo):
        codigo = input("Código inválido. Digite novamente: ")

    nome = input("Digite o nome do produto: ")
    while not validar_nome(nome):
        nome = input("Nome inválido. Digite novamente: ")

    preco = input("Digite o preço do produto: ")
    while not validar_preco(preco):
        preco = input("Preço inválido. Digite novamente: ")

    produto = {'codigo': codigo, 'nome': nome, 'preco': float(preco)}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def excluir_produto(produtos):
    limpar_tela()
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")


def listar_produtos(produtos):
    limpar_tela()
    print("Lista de Produtos:")
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
    input("Pressione Enter para continuar...")


def consultar_preco(produtos):
    limpar_tela()
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"O preço de {produto['nome']} é R${produto['preco']:.2f}")
            input("Pressione Enter para continuar...")
            return
    print("Produto não encontrado.")

def main():
    produtos = []

    while True:
        limpar_tela()
        print("Menu de Opções:")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            inserir_produto(produtos)
        elif escolha == '2':
            excluir_produto(produtos)
        elif escolha == '3':
            listar_produtos(produtos)
        elif escolha == '4':
            consultar_preco(produtos)
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


