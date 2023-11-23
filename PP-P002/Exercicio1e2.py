try:
    with open('todolist.txt', "r") as arquivo_leitura:
        tarefas = [linha.strip() for linha in arquivo_leitura.readlines()]
except FileNotFoundError:
    tarefas = []
while True:
    opcao = int(input("[1] Registrar nova tarefa \n[2] Editar tarefa \n[3] Marcar tarefa como realizada\n[4] Listar tarefas\n[0] Sair \n: "))
    match opcao:
        case 1:
            descricao = input("Digite a descrição da nova tarefa: ").capitalize()
            tarefas.append(f"{len(tarefas)+1}.{descricao} [ ]")
            print("Tarefa registrada!")
        case 2:
            idx_tarefa = int(input("Digite o ID da tarefa a ser editada: ")) - 1
            if 0 <= idx_tarefa < len(tarefas):
                nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
                tarefas[idx_tarefa] = f"{idx_tarefa + 1}.{nova_descricao} {tarefas[idx_tarefa][-3:]}"
                print("Tarefa editada!")
            else:
                print("ID inválido. Nenhuma alteração realizada.")
        case 3:
            idx_tarefa = int(input("Digite o ID da tarefa a ser marcada como realizada: ")) - 1
            if 0 <= idx_tarefa < len(tarefas):
                tarefa = tarefas.pop(idx_tarefa)
                tarefas.insert(0, tarefa.replace("[ ]", "[x]"))
                print("Tarefa marcada como realizada!")
            else:
                print("ID inválido. Nenhuma alteração realizada.")
        case 4:
            print("Lista de Tarefas:")
            for idx, tarefa in enumerate(tarefas, start=1):
                print(f"{idx}. {tarefa}")
        case 0:
            with open('todolist.txt', "w") as arquivo_escrita:
                for tarefa in tarefas:
                    arquivo_escrita.write(tarefa + "\n")
                    print("Tarefas salvas. Saindo do programa...")
            exit(1)
        case _:
            print("Opção inválida!")