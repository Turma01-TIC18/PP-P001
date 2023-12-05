class Supermercado:
    def __init__(self):
        self.produtos = {}

    def inserir_produto(self, codigo, nome, preco):
        self.produtos[codigo] = {'nome': nome, 'preco': preco}

    def excluir_produto(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo]
            print("-------------------------------------------------------------")
            print(f"Produto com código {codigo} removido.")
            print("-------------------------------------------------------------")
        else:
            print("-------------------------------------------------------------")
            print(f"Produto com código {codigo} não encontrado.")
            print("-------------------------------------------------------------")

    def listar_produtos(self):
        print("Lista de Produtos:")
        for codigo, produto in self.produtos.items():
            print("-------------------------------------------------------------")
            print(f"Código: {codigo}, Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}")
            print("-------------------------------------------------------------")

    def consultar_preco(self, codigo):
        if codigo in self.produtos:
            print("-------------------------------------------------------------")
            print(f"O preço do produto {self.produtos[codigo]['nome']} é R$ {self.produtos[codigo]['preco']:.2f}.")
            print("-------------------------------------------------------------")
        else:
            print("-------------------------------------------------------------")
            print(f"Produto com código {codigo} não encontrado.")
            print("-------------------------------------------------------------")