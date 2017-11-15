from Model.Usuario import Usuario

def Menu():
    print("\ \ \ \ D I N A M I C S / / / / \n"
          " 1 - Criar conta \n"
          " 2 - Sair")

def criarUsuarioTB():
    import sqlite3
    conn = sqlite3.connect('dinamics.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE TB_Usuario (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome VARCHAR(50) NOT NULL,
                   email VARCHAR(100) NOT NULL,
                   senha VARCHAR(50) NOT NULL,
                   profissao TEXT,
                   sexo TEXT,
                   data_nasc DATE
    );
    """)

    conn.commit()

    conn.close()

def FazerCadastro():

    criarUsuarioTB()

    nome = input("Digite seu nome completo: ")
    email = input("Digite seu email: ")
    profissao = input("Digite sua profissão: ")
    data_de_nascimento = input ("digite sua data de nascimento: (DD-MM-AA)")
    sexo = input("Digite seu sexo: F / M / PREFIRO NÃO DIZER")
    senha = input("Crie uma senha: ")

    usuario = Usuario(nome, email, senha, profissao, sexo, data_de_nascimento)

    return usuario

def main(args = []):

    Menu()

    continuar = True

    while continuar:
        try:
            op = int(input("digite a opção: "))

            if (op == 1):
                FazerCadastro()

            elif (op == 2):
                continuar = False
            else:
                print("Opção inválida!")

        except ValueError:
            print("Ops! Digite um valor válido")

if (__name__ == "__main__"):
    main()
