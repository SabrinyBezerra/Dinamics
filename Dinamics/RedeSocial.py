from Model.Usuario import Usuario

def Menu():
    print("\ \ \ \ D I N A M I C S / / / / \n" #Menu 
          " 1 - Criar conta \n"
          " 2 - Fazer Login \n"
          " 3 - Sair")

def criarChatTB(): #Criação do Tabela Chat
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

def criarMensagemTB(): #Criação do Tabela Mensagem
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

def criarFeedTB(): #Criação do Tabela Feed
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

def criarVisibilidadeTB(): #Criação do Tabela Visibilidade
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

def criarUsuarioTB(): #Criação do Tabela Usuario
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

def PesquisarUsuario(): #Pesquisar Usuário pelo nome e/ou Adicionar como amigo ou Excluir
    user = input("Digite o nome do Usuário: ")
    op = int(input("O que você deseja?\n"
                   " 1 - Adicionar como amigo\n"
                   " 2 - Excluir Amizade"))
    if (op == 1):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT * FROM TB_Usuario
                WHERE nome = ?
                """,(user))
        except:
            print("Usuário não encontrado")
        print("Usuário adicionado com sucesso")

    if (op == 2):
       Usuario.deletar(user)

    else:
        print("Opção inválida!")

def FazerCadastro(): #Fazer cadastro na rede social

    criarUsuarioTB()

    nome = input("Digite seu nome completo: ")
    email = input("Digite seu email: ")
    profissao = input("Digite sua profissão: ")
    data_de_nascimento = input ("digite sua data de nascimento: (DD-MM-AA)")
    sexo = input("Digite seu sexo: F / M / PREFIRO NÃO DIZER")
    senha = input("Crie uma senha: ")

    usuario = Usuario(nome, email, senha, profissao, sexo, data_de_nascimento)

    return usuario
def EscreverPublicação(): #Publicar no Feed
    pass

def MenuDoUsuario(): #Menu para um usuário já cadastrado
    print(" /// OLÁ USUÁRIO! /// \n"
          " 1 - Pesquisar Usuário \n"
          " 2 - Mandar mensagem \n"
          " 3 - Escrever publicação \n")

    op = int(input("Digite a opção: "))
    if (op == 1):
        PesquisarUsuario()

    if(op == 2):
        Usuario.TrocarMensagem()

    if(op ==3):
        EscreverPublicação()

    else:
        print("Opção inválida!")

def FazerLogin(): #Fazer login na rede social após o cadastro

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    try:
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM TB_Usuario
        WHERE email LIKE email = ?, senha LIKE senha = ?
        """, (email, senha))
        conn.commit()

        MenuDoUsuario()

    except:
        print("Opa! Usuário não cadastrado\n")

def main(args = []):

    criarChatTB() #Criação das tabelas
    criarFeedTB()
    criarMensagemTB()
    criarVisibilidadeTB()

    Menu()

    continuar = True

    while continuar:
        try:
            op = int(input("digite a opção: "))

            if (op == 1):
                FazerCadastro()

            if(op == 2):
                FazerLogin()

            elif (op == 3):
                continuar = False
            else:
                print("Opção inválida!")

        except ValueError:
            print("Ops! Digite um valor válido")

if (__name__ == "__main__"):
    main()
