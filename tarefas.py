from database import conectar


def cadastrar_tarefa():
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")
    responsavel = input("Responsável: ")
    situacao = "Pendente"

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, responsavel, situacao)
        VALUES (?, ?, ?, ?)
    """, (titulo, descricao, responsavel, situacao))

    conexao.commit()
    conexao.close()

    print("Tarefa cadastrada com sucesso!")


def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    print("\n===== TAREFAS CADASTRADAS =====")

    for tarefa in tarefas:
        print(tarefa)

    conexao.close()
