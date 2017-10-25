import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

lista = [(1, 'Sabriny', 'sabriny@gmail.com', '123456', 'estudante', 'feminino', '2001-04-26'),
         (2, 'Pedro', 'Pedro@hotmail.com', '12345', 'estudante', 'masculino', '2001-10-09'),
         (3, 'Larryce', 'Larryce@gmail.com', '123', 'estudante', 'feminino', '2001-10-31')]

cursor.executemany("""
INSERT INTO TB_Usuario (id, nome, email, senha, profissao, sexo, data_nasc)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", lista)

cursor.execute("""
SELECT * FROM TB_Usuario;
""")

for linha in cursor.fetchall():
    print(linha)

id_user = 1
novo_email = 'bezerrinha@gmail.com'
novo_senha = '12'

cursor.execute("""
UPDATE TB_Usuario
SET email = ?, senha = ?
WHERE id = ?
""", (novo_email, novo_senha, id_user))

cursor.execute("""
DELETE FROM TB_Usuario
WHERE id = ?
""", (id_user,))

conn.commit()

conn.close()
