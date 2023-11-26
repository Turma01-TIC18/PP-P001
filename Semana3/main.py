from supermercado import Supermercado

def main():
    supermercado = Supermercado()

    while True:
        print("\n*********> Menu <*********")
        print("1. Inserir novo produto")
        print("2. Excluir produto")
        print("3. Listar todos os produtos")
        print("4. Consultar preço")
        print("5. Sair")
        opcao = input("Digite uma opção (1-5): ")        

        if opcao == '1':
            codigo = input("Digite o código do produto (13 dígitos): ")
            if len(codigo) != 13:
                print("-------------------------------------------------------------")
                print("O código deve ser de 13 dígitos!")
                continue
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            supermercado.inserir_produto(codigo, nome, preco)
        elif opcao == '2':
            codigo = input("Digite o código do produto a ser excluído: ")
            supermercado.excluir_produto(codigo)
        elif opcao == '3':
            supermercado.listar_produtos()
        elif opcao == '4':
            codigo = input("Digite o código do produto para consultar o preço: ")
            supermercado.consultar_preco(codigo)
        elif opcao == '5':
            print(" ")
            print("Programa Encerrado com Sucesso!")
            break
        else:
            print("-------------------------------------------------------------")
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


