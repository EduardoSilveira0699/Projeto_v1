import logging
from logging.handlers import RotatingFileHandler
import os

# Cria a pasta logs se não existir
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Configuração do logger
logger = logging.getLogger("gerenciador_tarefas")
logger.setLevel(logging.INFO)

# Evita logs duplicados
if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Handler para arquivo (rotativo)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=2_000_000,  # 2MB
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
