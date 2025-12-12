from mysql.connector import connect, Error
from dotenv import load_dotenv
import os
from utils.logger import logger

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "tarefas_db")

def conectar():
    try:
        conn = connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return conn
    
    except Error as e:
        # Mensagem clara para o usuário e log com stack trace
        logger.exception("Erro na conexão com o banco de dados")
        # Re-raise error para capa superior (controller/main) lidar se quiser
        raise ConnectionError("Não foi possível conectar ao banco de dados. Verifique credenciais/serviço.") from e
