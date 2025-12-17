from models.tarefa import Tarefa
from services.tarefa_service import TarefaService


class TarefaController:

    def __init__(self):
        self.service = TarefaService()

    def criar(self, tarefa: Tarefa) -> int:
        return self.service.criar(tarefa)

    def listar(self):
        return self.service.listar()

    def atualizar_status(self, tarefa_id: int, novo_status: str) -> None:
        self.service.atualizar_status(tarefa_id, novo_status)

    def deletar(self, tarefa_id: int) -> None:
        self.service.deletar(tarefa_id)
