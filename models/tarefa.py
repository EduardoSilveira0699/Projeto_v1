from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Tarefa:
    id: int | None = None
    titulo: str = ''
    descricao: str = ''
    status: str = 'pendente'

    # NOVOS CAMPOS
    data_criacao: datetime | None = None
    data_prazo: date | None = None
    data_conclusao: datetime | None = None
