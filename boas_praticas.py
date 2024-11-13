import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "mybank.sqlite")
cursor = conexao.cursor()

cursor.execute(
    """CREATE TABLE clientes (id INTEGET PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100), email VARCHAR(150))'"""
)
