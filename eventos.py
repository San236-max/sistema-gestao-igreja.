from database import conectar


def cadastrar_evento():
    nome = input("Nome do evento: ")
    data = input("Data (DD/MM/AAAA): ")
    horario = input("Horário: ")
    descricao = input("Descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO eventos (nome, data, horario, descricao)
        VALUES (?, ?, ?, ?)
    """, (nome, data, horario, descricao))

    conexao.commit()
    conexao.close()

    print("Evento cadastrado com sucesso!")


def listar_eventos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM eventos")
    eventos = cursor.fetchall()

    print("\n===== EVENTOS CADASTRADOS =====")

    for evento in eventos:
        print(evento)

    conexao.close()
