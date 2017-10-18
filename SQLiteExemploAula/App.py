import sqlite3

conn = sqlite3.connect('rede_social.db')

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE usuario (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome VARCHAR(150) NOT NULL,
               nascimento DATE,
               genero VARCHAR(10) NOT NULL,
               email VARCGAR(100) NOT NULL,
               senha VARCHAR(10) NOT NULL
);
""")

print ('Tabela criada com sucesso')

conn.close()
