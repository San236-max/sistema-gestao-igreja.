import sqlite3

def conectar():
    return sqlite3.connect("igreja.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT,
            descricao TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            responsavel TEXT,
            situacao TEXT DEFAULT 'Pendente'
        )
    """)

    conexao.commit()
    conexao.close()
