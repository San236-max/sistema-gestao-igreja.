import unittest
import os
from database import conectar, criar_tabelas


class TestSistema(unittest.TestCase):

    def setUp(self):
        criar_tabelas()
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    def test_conexao_banco(self):
        self.assertIsNotNone(self.conexao)

    def test_cadastrar_evento(self):
        self.cursor.execute("""
            INSERT INTO eventos (nome, data, horario, descricao)
            VALUES (?, ?, ?, ?)
        """, ("Culto Jovem", "20/11/2026", "19:00", "Evento de teste"))

        self.conexao.commit()

        self.cursor.execute(
            "SELECT nome FROM eventos WHERE nome = ?",
            ("Culto Jovem",)
        )

        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)

    def test_cadastrar_tarefa(self):
        self.cursor.execute("""
            INSERT INTO tarefas (titulo, descricao, responsavel, situacao)
            VALUES (?, ?, ?, ?)
        """, ("Organizar salão", "Preparar o espaço", "Secretaria", "Pendente"))

        self.conexao.commit()

        self.cursor.execute(
            "SELECT titulo FROM tarefas WHERE titulo = ?",
            ("Organizar salão",)
        )

        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)

    def tearDown(self):
        self.conexao.close()


if __name__ == "__main__":
    unittest.main()
