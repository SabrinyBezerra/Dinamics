import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

lista = [(1, 2, 'olá'),
         (2, 3, 'oi')]

cursor.executemany("""
INSERT INTO TB_Chat (id, id_usuario, conversa)
VALUES (?, ?, ?)
""", lista)

cursor.execute("""
SELECT * FROM TB_Chat;
""")

for linha in cursor.fetchall():
    print(linha)

id_chat = 1
novo_conversa = 'bom dia'

cursor.execute("""
UPDATE TB_Chat
SET conversa = ?
WHERE id = ?
""", (novo_conversa, id_chat))

cursor.execute("""
DELETE FROM TB_Chat
WHERE id = ?
""", (id_chat,))

conn.commit()

conn.close()
