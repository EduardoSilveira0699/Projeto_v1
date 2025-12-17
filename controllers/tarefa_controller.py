from mysql.connector import Error

from database.conexao import conectar
from models.tarefa import Tarefa
from utils.logger import logger
from utils.validation import validar_status


class TarefaController:

    def criar(self, tarefa: Tarefa) -> int:
        """
        Cria uma nova tarefa no banco de dados
        """
        if not tarefa.titulo:
            raise ValueError("O título da tarefa não pode ser vazio.")

        try:
            conn = conectar()
            cursor = conn.cursor()

            sql = """
                INSERT INTO tarefas (titulo, descricao, status)
                VALUES (%s, %s, %s)
            """
            cursor.execute(
                sql,
                (tarefa.titulo, tarefa.descricao, tarefa.status)
            )
            conn.commit()

            tarefa_id = cursor.lastrowid
            logger.info(f"Tarefa criada: id={tarefa_id}, titulo='{tarefa.titulo}'")

            return tarefa_id

        except Error:
            logger.exception("Erro ao criar tarefa")
            raise

        finally:
            cursor.close()
            conn.close()

    # --------------------------------------------------

    def listar(self) -> list[dict]:
        """
        Retorna todas as tarefas cadastradas
        """
        try:
            conn = conectar()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT id, titulo, descricao, status FROM tarefas"
            cursor.execute(sql)

            tarefas = cursor.fetchall()
            logger.info("Listagem de tarefas realizada")

            return tarefas

        except Error:
            logger.exception("Erro ao listar tarefas")
            raise

        finally:
            cursor.close()
            conn.close()

    # --------------------------------------------------

    def atualizar_status(self, tarefa_id: int, novo_status: str) -> None:
        if not validar_status(novo_status):
            logger.warning(
                f"Tentativa de status inválido: id={tarefa_id}, status={novo_status}"
            )
            raise ValueError("Status inválido. Use 'pendente' ou 'concluido'.")

        try:
            conn = conectar()
            cursor = conn.cursor()

            sql = "UPDATE tarefas SET status = %s WHERE id = %s"
            cursor.execute(sql, (novo_status, tarefa_id))

            if cursor.rowcount == 0:
                logger.warning(
                    f"Tentativa de atualizar tarefa inexistente: id={tarefa_id}"
                )
                raise ValueError("Tarefa não encontrada.")

            conn.commit()
            logger.info(
                f"Status atualizado: id={tarefa_id}, novo_status={novo_status}"
            )

        except Error:
            logger.exception("Erro de banco ao atualizar status")
            raise

        finally:
            cursor.close()
            conn.close()



    # --------------------------------------------------

    def deletar(self, tarefa_id: int) -> None:
        """
        Remove uma tarefa do banco de dados
        """
        try:
            conn = conectar()
            cursor = conn.cursor()

            sql = "DELETE FROM tarefas WHERE id = %s"
            cursor.execute(sql, (tarefa_id,))

            if cursor.rowcount == 0:
                raise ValueError("Tarefa não encontrada.")

            conn.commit()
            logger.info(f"Tarefa deletada: id={tarefa_id}")

        except Error:
            logger.exception("Erro ao deletar tarefa")
            raise

        finally:
            cursor.close()
            conn.close()
