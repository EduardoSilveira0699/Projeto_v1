from controllers.tarefa_controller import TarefaController
from models.tarefa import Tarefa
from views.menu import exibir_menu
from utils.validation import ler_int, validar_status
from utils.logger import logger

controller = TarefaController()

def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            titulo = input("Título: ").strip()
            descricao = input("Descrição: ").strip()
            if not titulo:
                print("Título não pode ficar vazio.")
                continue
            tarefa = Tarefa(titulo=titulo, descricao=descricao)
            try:
                tarefa_id = controller.criar(tarefa)
                print(f"Tarefa criada com ID: {tarefa_id}")
                logger.info(f"Tarefa criada: id={tarefa_id} titulo='{titulo}'")
            except Exception as e:
                print("Erro ao criar tarefa. Veja o log para detalhes.")
                logger.exception("Erro criando tarefa")

        elif opcao == "2":
            try:
                tarefas = controller.listar()
                if not tarefas:
                    print("Nenhuma tarefa encontrada.")
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} - {t['status']}")
                logger.info("Listagem de tarefas executada")
            except Exception:
                print("Erro ao listar tarefas. Verifique o log.")
                logger.exception("Erro listando tarefas")

        elif opcao == "3":
            tarefa_id = ler_int("ID da tarefa: ")
            novo_status = input("Novo status (pendente/concluido): ").strip().lower()

            if not validar_status(novo_status):
                print("Status inválido. Use 'pendente' ou 'concluido'.")
                continue

            try:
                controller.atualizar_status(tarefa_id, novo_status)
                print("Status atualizado com sucesso!")
            except Exception as e:
                print("Erro ao atualizar status. Veja o log.")
                logger.exception(f"Erro atualizando status: {e}")


        elif opcao == "4":
            tarefa_id = ler_int("ID da tarefa para deletar: ")
            confirm = input(f"Confirma excluir a tarefa {tarefa_id}? (s/n): ").strip().lower()
            if confirm != 's':
                print("Exclusão cancelada.")
                continue
            try:
                controller.deletar(tarefa_id)
                print("Tarefa deletada!")
                logger.info(f"Tarefa deletada: id={tarefa_id}")
            except Exception:
                print("Erro ao deletar tarefa. Veja o log.")
                logger.exception("Erro deletando tarefa")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()