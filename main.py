from controllers.tarefa_controller import TarefaController
from models.tarefa import Tarefa

def menu():
    print("\n==== Gerenciador de Tarefas ====")
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar status")
    print("4. Deletar tarefa")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    controller = TarefaController()

    while True:
        opcao = menu()

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            tarefa = Tarefa(titulo=titulo, descricao=descricao)
            tarefa_id = controller.criar(tarefa)
            print(f"Tarefa criada com ID: {tarefa_id}")

        elif opcao == "2":
            tarefas = controller.listar()
            for t in tarefas:
                print(f"{t['id']} - {t['titulo']} - {t['status']}")

        elif opcao == "3":
            tarefa_id = int(input("ID da tarefa: "))
            novo_status = input("Novo status (pendente/concluido): ")
            controller.atualizar_status(tarefa_id, novo_status)
            print("Status atualizado com sucesso!")

        elif opcao == "4":
            tarefa_id = int(input("ID da tarefa para deletar: "))
            controller.deletar(tarefa_id)
            print("Tarefa deletada!")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()