from dataclasses import dataclass

@dataclass
class Tarefa:
    id: int | None = None
    titulo: str = ''
    descricao: str = ''
    status: str = 'pendente'