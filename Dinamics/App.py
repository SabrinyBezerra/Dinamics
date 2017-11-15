from Model.Usuario import Usuario

def Menu():
    print("\ \ \ \ D I N A M I C S / / / / \n"
          " 1 - Criar conta \n"
          " 2 - Sair")
    
def criarChatTB():
    import sqlite3
    conn = sqlite3.connect('dinamics.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE TB_Chat (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   id_usuario INTEGER,
                   conversa TEXT NOT NULL,
                   FOREIGN KEY(id_usuario) REFERENCES TB_Usuario(id)
    );
    """)

    conn.commit()

    conn.close()

def criarMensagemTB():
    import sqlite3
    conn = sqlite3.connect('dinamics.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE TB_Mensagem (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               id_amigo INTEGER NOT NULL,
               id_chat INTEGER NOT NULL,
               emoji TEXT,
               FOREIGN KEY(id_chat) REFERENCES TB_Chat(id)
    );
    """)

    conn.commit()

    conn.close()

def criarFeedTB():
    import sqlite3
    conn = sqlite3.connect('dinamics.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE TB_Feed (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   id_publicacao INTEGER NOT NULL,
                   publicacao VARCHAR(135) NOT NULL
    );
    """)

    conn.commit()

    conn.close()
    
def criarVisibilidadeTB():
    import sqlite3
    conn = sqlite3.connect('dinamics.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE TB_Visibilidade (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   publico BOOLEAN NOT NULL,
                   privado BOOLEAN NOT NULL
    );
    """)

    conn.commit()

    conn.close()
    
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
