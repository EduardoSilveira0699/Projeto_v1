from controllers.tarefa_controller import TarefaController
from models.tarefa import Tarefa
from views.menu import exibir_menu
from utils.validation import ler_int
from utils.logger import logger


def main():
    controller = TarefaController()

    while True:
        opcao = exibir_menu()

        # -------------------------------
        # CRIAR TAREFA
        # -------------------------------
        if opcao == "1":
            titulo = input("Título: ").strip()
            descricao = input("Descrição: ").strip()

            try:
                tarefa = Tarefa(titulo=titulo, descricao=descricao)
                tarefa_id = controller.criar(tarefa)
                print(f"Tarefa criada com sucesso! ID: {tarefa_id}")

            except ValueError as e:
                # erro de regra de negócio / usuário
                print(f"Erro: {e}")

            except Exception:
                # erro interno do sistema
                print("Erro interno ao criar tarefa. Veja o log.")
                logger.exception("Erro ao criar tarefa")

        # -------------------------------
        # LISTAR TAREFAS
        # -------------------------------
        elif opcao == "2":
            try:
                tarefas = controller.listar()

                if not tarefas:
                    print("Nenhuma tarefa cadastrada.")
                    continue

                print("\n--- TAREFAS ---")
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} - {t['status']}")

            except Exception:
                print("Erro interno ao listar tarefas. Veja o log.")
                logger.exception("Erro ao listar tarefas")

        # -------------------------------
        # ATUALIZAR STATUS
        # -------------------------------
        elif opcao == "3":
            tarefa_id = ler_int("ID da tarefa: ")
            novo_status = input("Novo status (pendente/concluido): ").strip().lower()

            try:
                controller.atualizar_status(tarefa_id, novo_status)
                print("Status atualizado com sucesso!")

            except ValueError as e:
                # status inválido, id inexistente etc.
                print(f"Erro: {e}")

            except Exception:
                print("Erro interno ao atualizar status. Veja o log.")
                logger.exception("Erro ao atualizar status")

        # -------------------------------
        # DELETAR TAREFA
        # -------------------------------
        elif opcao == "4":
            tarefa_id = ler_int("ID da tarefa para deletar: ")
            confirmacao = input(
                f"Confirma excluir a tarefa {tarefa_id}? (s/N): "
            ).strip().lower()

            if confirmacao != "s":
                print("Exclusão cancelada.")
                continue

            try:
                controller.deletar(tarefa_id)
                print("Tarefa deletada com sucesso!")

            except ValueError as e:
                print(f"Erro: {e}")

            except Exception:
                print("Erro interno ao deletar tarefa. Veja o log.")
                logger.exception("Erro ao deletar tarefa")

        # -------------------------------
        # SAIR
        # -------------------------------
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        # -------------------------------
        # OPÇÃO INVÁLIDA
        # -------------------------------
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
