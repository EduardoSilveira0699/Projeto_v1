from database.conexao import conectar
from models.tarefa import Tarefa
from mysql.connector import Error

class TarefaController:

    def criar(self, tarefa: Tarefa) -> int:
        conn = conectar()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO tarefas (titulo, descricao, status) VALUES (%s, %s, %s)"
            cursor.execute(sql, (tarefa.titulo, tarefa.descricao, tarefa.status))
            conn.commit()
            tarefa_id = cursor.lastrowid
            return tarefa_id
        except Error as e:
            print('Erro ao criar tarefa:', e)
            raise
        finally:
            cursor.close()
            conn.close()

    def listar(self) -> list:
        conn = conectar()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM tarefas ORDER BY criado_em DESC')
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def atualizar_status(self, tarefa_id: int, novo_status: str) -> None:
        conn = conectar()
        try:
            cursor = conn.cursor()
            sql = 'UPDATE tarefas SET status = %s WHERE id = %s'
            cursor.execute(sql, (novo_status, tarefa_id))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def deletar(self, tarefa_id: int) -> None:
        conn = conectar()
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tarefas WHERE id = %s', (tarefa_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()