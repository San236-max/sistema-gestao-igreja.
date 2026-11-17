from database import criar_tabelas
from eventos import cadastrar_evento, listar_eventos
from tarefas import cadastrar_tarefa, listar_tarefas


def menu():
    criar_tabelas()

    while True:
        print("\n===== SISTEMA DE GESTÃO DA IGREJA =====")
        print("1 - Cadastrar evento")
        print("2 - Listar eventos")
        print("3 - Cadastrar tarefa")
        print("4 - Listar tarefas")
        print("5 - Ativar modo de leitura acessível")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_evento()
        elif opcao == "2":
            listar_eventos()
        elif opcao == "3":
            cadastrar_tarefa()
        elif opcao == "4":
            listar_tarefas()
        elif opcao == "5":
            print("\033[97;40m")
            print("MODO DE ALTO CONTRASTE ATIVADO!")
            print("O texto será exibido em branco sobre fundo preto.")  
        elif opcao == "0":
            print("Sistema encerrado!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
