from models.tarefa import Tarefa
from repositories.tarefa_repository import TarefaRepository


class TarefaService:

    def __init__(self):
        self.repo = TarefaRepository()

    def criar(self, tarefa: Tarefa):
        if not tarefa.titulo.strip():
            raise ValueError("Título não pode ser vazio")

        return self.repo.criar(tarefa)

    def listar(self):
        return self.repo.listar()

    def atualizar_status(self, tarefa_id: int, status: str):
        if status not in ("pendente", "concluido"):
            raise ValueError("Status inválido")

        return self.repo.atualizar_status(tarefa_id, status)

    def deletar(self, tarefa_id: int):
        return self.repo.deletar(tarefa_id)
