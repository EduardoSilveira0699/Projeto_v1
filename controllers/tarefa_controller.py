from database.conexao import conectar
from models.tarefa import Tarefa
from mysql.connector import Error
from utils.logger import logger

class TarefaController:

    def criar(self, tarefa: Tarefa) -> int:
        try:
            conn = conectar()
        except Exception as e:
            logger.error("Falha ao conectar ao banco no método criar(): %s", e)
            raise

        try:
            cursor = conn.cursor()

            sql = """
                INSERT INTO tarefas (titulo, descricao, status)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (tarefa.titulo, tarefa.descricao, tarefa.status))
            conn.commit()

            tarefa_id = cursor.lastrowid
            logger.info(f"Tarefa criada no banco: id={tarefa_id}")

            return tarefa_id

        except Error:
            logger.exception("Erro executando INSERT no método criar()")
            raise

        finally:
            cursor.close()
            conn.close()

    def listar(self) -> list:
        try:
            conn = conectar()
        except Exception as e:
            logger.error("Falha ao conectar no listar: %s", e)
            raise

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM tarefas ORDER BY criado_em DESC')
            resultado = cursor.fetchall()
            return resultado
        except Error:
            logger.exception("Erro executando SELECT em listar()")
            raise
        finally:
            cursor.close()
            conn.close()

    def atualizar_status(self, tarefa_id: int, novo_status: str) -> None:
        try:
            conn = conectar()
        except Exception as e:
            logger.error("Falha ao conectar no método atualizar_status(): %s", e)
            raise

        try:
            cursor = conn.cursor()

            sql = "UPDATE tarefas SET status = %s WHERE id = %s"
            cursor.execute(sql, (novo_status, tarefa_id))
            conn.commit()

            logger.info(f"Status atualizado: id={tarefa_id}, novo_status={novo_status}")

        except Error:
            logger.exception("Erro no UPDATE no método atualizar_status()")
            raise

        finally:
            cursor.close()
            conn.close()

    def deletar(self, tarefa_id: int) -> None:
        try:
            conn = conectar()
        except Exception as e:
            logger.error("Falha ao conectar no método deletar(): %s", e)
            raise

        try:
            cursor = conn.cursor()

            sql = "DELETE FROM tarefas WHERE id = %s"
            cursor.execute(sql, (tarefa_id,))
            conn.commit()

            logger.info(f"Tarefa deletada: id={tarefa_id}")

        except Error:
            logger.exception("Erro executando DELETE no método deletar()")
            raise

        finally:
            cursor.close()
            conn.close()