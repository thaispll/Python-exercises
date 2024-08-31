#variaveis do sistema
import mysql.connector as db
import os
#Importações de Módulos e Bibliotecas


#conexão com o SGBD
conexao = db.connect(host = "localhost", user="root" , passwd = 'alunolab')
#Criação do Cursor
cursor = conexao.cursor()
#Criar o banco de dados e usa-lo.
cursor.execute('CREATE DATABASE IF NOT EXISTS menu;')
cursor.execute('USE menu;')
#Cria a tabela Pessoas
cursor.execute('CREATE TABLE IF NOT EXISTS tarefa(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50) NOT NULL);')


#Funções do Software
def exibirMenu():
    os.system('cls')
    print("=-"*30+"=")
    print("\033[1;4mMenu:\033[m".center(61))
    print("1. Adicionar nova tarefa.")
    print("2. Exibir tarefas existentes.")
    print("3. Excluir tarefas.")
    print("0. Sair.")
    print("=-"*30+"=")


def adicionarTarefa():
    nome = input("(Digite 'Sair' para finalizar)\nDigite um nome para a tarefa:").upper()
    while nome != 'SAIR':
        comando = f'INSERT INTO tarefa (nome) VALUES ("{nome}")'
        cursor.execute(comando)
        conexao.commit()
        nome = input("(Digite 'Sair' para finalizar)\nDigite um nome para a tarefa:").upper()
    return None

def exibirTarefas():
    cursor.execute('SELECT nome FROM tarefa;')
    for i in cursor:
        print(i[0])
    input("Pressione 'Enter' para continuar.")
    return None


def excluirTarefa():
    id = -1
    while id != 0:
        os.system('cls')
        print('Essas são as tarefas')
        cursor.execute('SELECT id, nome FROM tarefa;')  # Busca também o ID da tarefa
        tarefas = cursor.fetchall()
        for tarefa in tarefas:
            print(f"{tarefa[0]} - {tarefa[1]}")  # Mostra o ID e o nome da tarefa

        # Solicita o ID para apagar
        id = int(input("Insira 0 para sair.\nDigite o ID da tarefa que deseja apagar: "))

        if id == 0:
            break

        # Tenta apagar pelo ID
        cursor.execute('DELETE FROM tarefa WHERE id = %s;', (id,))
        conexao.commit()
        print(f"Tarefa com ID {id} excluída.")

    return None

def principal():
    while True:
        exibirMenu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionarTarefa()
        elif opcao == "2":
            exibirTarefas()
        elif opcao == "3":
            excluirTarefa()
        elif opcao == "0":
            exit()
        else:
            print("Opção inválida. Tente novamente.")

# Corrige a linha de execução principal
if __name__ == "__main__":
    principal()

#Fecha a conexao com o banco de dados
conexao.close()