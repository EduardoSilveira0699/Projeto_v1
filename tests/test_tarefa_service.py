import pytest
from models.tarefa import Tarefa
from services.tarefa_service import TarefaService


def test_criar_tarefa_com_titulo_vazio():
    service = TarefaService()
    tarefa = Tarefa(titulo="", descricao="teste")

    with pytest.raises(ValueError):
        service.criar(tarefa)


def test_criar_tarefa_com_titulo_valido(monkeypatch):
    service = TarefaService()
    tarefa = Tarefa(titulo="Estudar Python", descricao="Service Layer")

    # Mock do repository (não acessa banco)
    monkeypatch.setattr(
        service.repo,
        "criar",
        lambda tarefa: 1
    )

    tarefa_id = service.criar(tarefa)

    assert tarefa_id == 1


def test_atualizar_status_invalido():
    service = TarefaService()

    with pytest.raises(ValueError):
        service.atualizar_status(1, "finalizado")


def test_atualizar_status_valido(monkeypatch):
    service = TarefaService()

    # Simula tarefa existente
    monkeypatch.setattr(
        service.repo,
        "buscar_por_id",
        lambda tarefa_id: {"id": tarefa_id, "status": "pendente"}
    )

    # Simula atualização sem banco
    monkeypatch.setattr(
        service.repo,
        "atualizar_status",
        lambda tarefa_id, status: None
    )

    service.atualizar_status(1, "pendente")
