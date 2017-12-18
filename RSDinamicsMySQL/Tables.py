import mysql.connector
from database.configDB import config

def main():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE TB_RedeSocial (
                   id INTEGER PRIMARY KEY,
                   nome VARCHAR (50),
                   descricao TEXT
        
        );
        """)

        cursor.execute("""
        CREATE TABLE TB_Pessoa(
                      id INTEGER PRIMARY KEY AUTO_INCREMENT,
                      nome VARCHAR(50),
                      genero TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE TB_Usuario (
                       id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       nome VARCHAR(50) NOT NULL,
                       email VARCHAR(100) NOT NULL,
                       senha VARCHAR(50) NOT NULL,
                       profissao TEXT,
                       genero TEXT,
                       nascimento DATE
                      
        );
        """)

        cursor.execute("""
                CREATE TABLE TB_Amigo (
                               id INTEGER NOT NULL PRIMARY KEY,
                               nome VARCHAR(50),
                               nascimento DATE,
                               genero VARCHAR(50)
                );
        """)

        cursor.execute("""
                CREATE TABLE TB_UsuarioAmigo(
                            id INTEGER PRIMARY KEY, 
                            nome_amigo VARCHAR(50),
                            amizade VARCHAR(50),
                            solicitacao VARCHAR(50),
                            id_usuario INTEGER,
                            FOREIGN KEY(id_usuario) REFERENCES TB_Usuario(id)

                );
        """)

        cursor.execute("""
        CREATE TABLE TB_Chat (
                       id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       id_usuario INTEGER,
                       texto TEXT,
                       emoji TEXT,
                       id_amigo INTEGER,
                       conversa TEXT NOT NULL,
                       FOREIGN KEY(id_usuario) REFERENCES TB_Usuario(id),
                       FOREIGN KEY(id_amigo) REFERENCES TB_Amigo(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE TB_Mensagem (
                       id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       id_amigo INTEGER NOT NULL,
                       texto TEXT,
                       emoji TEXT,
                       FOREIGN KEY(id_amigo) REFERENCES TB_Amigo(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE TB_Feed (
                       id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       id_publicacao INTEGER NOT NULL,
                       publicacao VARCHAR(135) NOT NULL,
                       texto TEXT,
                       tipo TEXT,
                       id_amigo INTEGER,
                       emoji TEXT,
                       FOREIGN KEY(id_amigo) REFERENCES TB_Amigo(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE TB_Visibilidade (
                       id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       publico BOOLEAN NOT NULL,
                       privado BOOLEAN NOT NULL
        );
        """)

        conn.commit()

        conn.close()
    except mysql.connector.Error as err:
        print(err)

if __name__ == '__main__':
    main()
