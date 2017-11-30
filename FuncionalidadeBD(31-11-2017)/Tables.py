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

cursor.execute("""
CREATE TABLE TB_Chat (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               id_usuario INTEGER,
               conversa TEXT NOT NULL,
               FOREIGN KEY(id_usuario) REFERENCES TB_Usuario(id)
);
""")

cursor.execute("""
CREATE TABLE TB_Mensagem (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               id_amigo INTEGER NOT NULL,
               id_chat INTEGER NOT NULL,
               emoji TEXT,
               FOREIGN KEY(id_chat) REFERENCES TB_Chat(id)
);
""")

cursor.execute("""
CREATE TABLE TB_Feed (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               id_publicacao INTEGER NOT NULL,
               publicacao VARCHAR(135) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE TB_Visibilidade (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               publico BOOLEAN NOT NULL,
               privado BOOLEAN NOT NULL
);
""")

conn.commit()

conn.close()