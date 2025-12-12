import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("projeto_tarefas")
logger.setLevel(logging.INFO)

# File handler (rotacionamento simples por dia não instalado; usar RotatingFileHandler se quiser)
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "app.log"), encoding="utf-8")
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Evita adicionar handlers duplicados se o módulo for importado várias vezes
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
