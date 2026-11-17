from flask import Flask, render_template_string
import sqlite3
from database import criar_tabelas

app = Flask(__name__)

criar_tabelas()

def conectar():
    return sqlite3.connect("igreja.db")

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sistema da Igreja</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f4f7;
            margin: 0;
            padding: 25px;
            color: #263238;
        }
        main {
            max-width: 800px;
            margin: auto;
        }
        h1 { color: #245b45; }
        section {
            background: white;
            padding: 20px;
            margin: 18px 0;
            border-radius: 10px;
        }
        li { padding: 7px; }
    </style>
</head>
<body>
<main>
    <h1>Organização da Igreja</h1>
    <p>Consulta de eventos e tarefas</p>

    <section>
        <h2>Eventos</h2>
        <ul>
        {% for evento in eventos %}
            <li>{{ evento }}</li>
        {% else %}
            <li>Nenhum evento cadastrado.</li>
        {% endfor %}
        </ul>
    </section>

    <section>
        <h2>Tarefas</h2>
        <ul>
        {% for tarefa in tarefas %}
            <li>{{ tarefa }}</li>
        {% else %}
            <li>Nenhuma tarefa cadastrada.</li>
        {% endfor %}
        </ul>
    </section>
</main>
</body>
</html>
"""

@app.route("/")
def inicio():
    eventos = []
    tarefas = []

    try:
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute(
            "SELECT nome, data, horario FROM eventos"
        )
        eventos = cursor.fetchall()

        cursor.execute(
            "SELECT titulo, responsavel, situacao FROM tarefas"
        )
        tarefas = cursor.fetchall()

        banco.close()

    except sqlite3.Error:
        eventos = ["Banco de dados ainda não disponível."]
        tarefas = ["Banco de dados ainda não disponível."]

    return render_template_string(
        HTML,
        eventos=eventos,
        tarefas=tarefas
    )

if __name__ == "__main__":
    app.run()
