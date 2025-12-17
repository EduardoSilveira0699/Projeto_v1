from database.conexao import conectar

class TarefaRepository:

    def criar(self, tarefa):
        conn = conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO tarefas (titulo, descricao)
        VALUES (%s, %s)
        """
        cursor.execute(sql, (tarefa.titulo, tarefa.descricao))
        conn.commit()

        tarefa_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return tarefa_id

    def listar(self):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()

        cursor.close()
        conn.close()
        return tarefas

    def buscar_por_id(self, tarefa_id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM tarefas WHERE id=%s", (tarefa_id,))
        tarefa = cursor.fetchone()

        cursor.close()
        conn.close()

        return tarefa

    def atualizar_status(self, tarefa_id, status):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE tarefas SET status=%s WHERE id=%s",
            (status, tarefa_id)
        )
        conn.commit()

        cursor.close()
        conn.close()

    def deletar(self, tarefa_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tarefas WHERE id=%s", (tarefa_id,))
        conn.commit()

        cursor.close()
        conn.close()
