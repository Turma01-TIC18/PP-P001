import json

def Reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salario'] *= 1.10

def main():

    try:
         while True:
            print("\n*********> Menu <*********")
            print("1. Ler dados")
            print("2. Listar dados")
            print("3. Reajustar em 10%")
            print("4. Mostrar Lista Reajustada")
            print("5. Sair")
            opcao = input("Digite uma opção (1-5): ") 
        
            if opcao == '1':
                with open('funcionarios.json', 'r') as arquivo:
                    lista_empregados = json.load(arquivo)
                    if open:
                        print("Dados Lidos com Sucesso!")
                    
            elif opcao == '2':
                print("Informações dos empregados antes do reajuste:")
                for empregado in lista_empregados:
                    print(empregado)

            elif opcao == '3':
                Reajusta_dez_porcento(lista_empregados)

            elif opcao == '4':
                print("\nInformações dos empregados após o reajuste:")
                for empregado in lista_empregados:
                    print(empregado)
            elif opcao == '5':
                print(" ")
                print("Programa Encerrado com Sucesso!")
                break
            else:
                print("-------------------------------------------------------------")
                print("Opção inválida. Tente novamente.")

        # Atualização do arquivo com as informações após o reajuste
            with open('funcionarios.json', 'w') as arquivo:
                json.dump(lista_empregados, arquivo, indent=2)

    except FileNotFoundError:
        print("Arquivo 'funcionarios.json' não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
