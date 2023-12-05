import json

def Reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salario'] *= 1.10

def main():
    while True:
        try:
            print("\n\n*********> Menu <*********")
            print("-------------------------------------------------------------")
            print("1. Ler dados")
            print("2. Listar dados")
            print("3. Reajustar em 10%")
            print("4. Mostrar Lista Reajustada")
            print("5. Sair")
            print("-------------------------------------------------------------")
            opcao = input("Digite uma opção (1-5): ") 
        
            if opcao == '1':
                with open('funcionarios.json', 'r') as arquivo:
                    lista_empregados = json.load(arquivo)
                    if open:
                        print("-------------------------------------------------------------")
                        print("Dados Lidos com Sucesso!")
                    
            elif opcao == '2':
                print("-------------------------------------------------------------")
                print("Informações dos empregados antes do reajuste:")
                print("-------------------------------------------------------------")
                for empregado in lista_empregados:
                    print(empregado)

            elif opcao == '3':
                Reajusta_dez_porcento(lista_empregados)
                print("-------------------------------------------------------------")
                print("Reajuste realizado com Sucesso!!")
                print("-------------------------------------------------------------")


            elif opcao == '4':
                print("-------------------------------------------------------------")
                print("Informações dos empregados após o reajuste:")
                print("-------------------------------------------------------------")
                for empregado in lista_empregados:
                    print(empregado)
            elif opcao == '5':
                print(" ")
                print("Programa Encerrado com Sucesso!")
                print("-------------------------------------------------------------")
                break
            else:
                print("-------------------------------------------------------------")
                print("Opção inválida. Tente novamente.")

            # Atualização do arquivo com as informações após o reajuste
            with open('funcionarios.json', 'w') as arquivo:
                json.dump(lista_empregados, arquivo, indent=2)

        except FileNotFoundError:
            print("-------------------------------------------------------------")
            print("Arquivo 'funcionarios.json' não encontrado.")
        except json.JSONDecodeError:
            print("-------------------------------------------------------------")
            print("Erro ao decodificar o arquivo JSON.")
        except Exception as e:
            print("-------------------------------------------------------------")
            print(f"Ocorreu um erro: {e}")
        

if __name__ == "__main__":
    main()
