from datetime import datetime
from services.tarefa_service import TarefaService

def test_concluir_tarefa_define_data_conclusao(monkeypatch):
    service = TarefaService()

    # Simula tarefa existente
    monkeypatch.setattr(
        service.repo,
        "buscar_por_id",
        lambda tarefa_id: {"id": tarefa_id, "status": "pendente"}
    )

    def fake_update(tarefa_id, status, data_conclusao):
        assert status == "concluido"
        assert isinstance(data_conclusao, datetime)

    monkeypatch.setattr(
        service.repo,
        "atualizar_status",
        fake_update
    )

    service.atualizar_status(1, "concluido")
