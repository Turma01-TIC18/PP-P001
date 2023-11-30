import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def validar_ano(ano):
    try:
        int(ano)
        return True
    except ValueError:
        return False


def validar_salario(salario):
    try:
        float(salario)
        return True
    except ValueError:
        return False


def cadastrar_funcionario(empregados):
    limpar_tela()
    nome = input("Digite o nome do funcionário: ")
    sobrenome = input("Digite o sobrenome do funcionário: ")
    
    ano_nascimento = input("Digite o ano de nascimento do funcionário: ")
    while not validar_ano(ano_nascimento):
        ano_nascimento = input("Ano de nascimento inválido. Digite novamente: ")

    RG = input("Digite o RG do funcionário: ")

    ano_admissao = input("Digite o ano de admissão do funcionário: ")
    while not validar_ano(ano_admissao):
        ano_admissao = input("Ano de admissão inválido. Digite novamente: ")

    salario = input("Digite o salário do funcionário: ")
    while not validar_salario(salario):
        salario = input("Salário inválido. Digite novamente: ")

    novo_funcionario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'ano_nascimento': int(ano_nascimento),
        'RG': RG,
        'ano_admissao': int(ano_admissao),
        'salario': float(salario)
    }

    empregados.append(novo_funcionario)
    print("Funcionário cadastrado com sucesso!")


def salvar_em_arquivo(empregados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for empregado in empregados:
            linha = "{},{},{},{},{},{}\n".format(
                empregado['nome'],
                empregado['sobrenome'],
                empregado['ano_nascimento'],
                empregado['RG'],
                empregado['ano_admissao'],
                empregado['salario']
            )
            arquivo.write(linha)

def reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado['salario'] *= 1.1
    input("Pressione Enter para continuar...") 


def ler_informacoes_arquivo(nome_arquivo):
    empregados = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                if len(dados) == 6:
                    empregado = {
                        'nome': dados[0],
                        'sobrenome': dados[1],
                        'ano_nascimento': int(dados[2]),
                        'RG': dados[3],
                        'ano_admissao': int(dados[4]),
                        'salario': float(dados[5])
                    }
                    empregados.append(empregado)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
    return empregados


def exibir_informacoes_empregados(empregados):
    for empregado in empregados:
        print("Nome: {}, Sobrenome: {}, Ano de Nascimento: {}, RG: {}, Ano de Admissão: {}, Salário: R${:.2f}".format(
            empregado['nome'],
            empregado['sobrenome'],
            empregado['ano_nascimento'],
            empregado['RG'],
            empregado['ano_admissao'],
            empregado['salario']
        ))
    input("Pressione Enter para continuar...")


def main():
    nome_arquivo = 'funcionarios.txt'
    lista_empregados = ler_informacoes_arquivo(nome_arquivo)

    while True:
        limpar_tela()
        print("Menu de Opções:")
        print("1. Inserir um novo funcionário")
        print("2. Reajustar salários em 10%")
        print("3. Listar todos os funcionários")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            cadastrar_funcionario(lista_empregados)
        elif escolha == '2':
            reajusta_dez_porcento(lista_empregados)
        elif escolha == '3':
            exibir_informacoes_empregados(lista_empregados)
        elif escolha == '0':
            salvar_em_arquivo(lista_empregados, nome_arquivo)
            print("Programa encerrado. As informações foram salvas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()