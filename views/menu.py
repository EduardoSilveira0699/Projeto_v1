def exibir_menu() -> str:
    print("\n==== GERENCIADOR DE TAREFAS ====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar status")
    print("4 - Deletar tarefa")
    print("0 - Sair")
    opc = input("Escolha: ").strip()
    return opc
