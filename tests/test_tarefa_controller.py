import pytest
from controllers.tarefa_controller import TarefaController


def test_criar_tarefa_sem_titulo():
    controller = TarefaController()

    with pytest.raises(ValueError):
        controller.criar(
            tarefa=type("TarefaFake", (), {"titulo": "", "descricao": "", "status": "pendente"})()
        )
        
def test_atualizar_status_invalido():
    controller = TarefaController()

    with pytest.raises(ValueError):
        controller.atualizar_status(1, "finalizado")
