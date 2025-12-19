from models.tarefa import Tarefa
from repositories.tarefa_repository import TarefaRepository
from datetime import datetime


class TarefaService:

    def __init__(self):
        self.repo = TarefaRepository()

    def criar(self, tarefa: Tarefa):
        if not tarefa.titulo.strip():
            raise ValueError("Título não pode ser vazio")

        return self.repo.criar(tarefa)

    def listar(self):
        return self.repo.listar()

    from datetime import datetime

    def atualizar_status(self, tarefa_id: int, status: str):
        if status not in ("pendente", "concluido"):
            raise ValueError("Status inválido")

        tarefa = self.repo.buscar_por_id(tarefa_id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada")

        data_conclusao = None
        if status == "concluido":
            data_conclusao = datetime.now()

        return self.repo.atualizar_status(
            tarefa_id,
            status,
            data_conclusao
        )


    def deletar(self, tarefa_id: int):
        tarefa = self.repo.buscar_por_id(tarefa_id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada")

        return self.repo.deletar(tarefa_id)
