import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

lista = [(1, 2, ':)'),
         (2, 3, ':(')]

cursor.executemany("""
INSERT INTO TB_Mensagem (id, id_amigo, id_chat)
VALUES (?, ?, ?)
""", lista)

cursor.execute("""
SELECT * FROM TB_Mensagem;
""")

for linha in cursor.fetchall():
    print(linha)

id_msg = 1
novo_emoji = ':D'

cursor.execute("""
UPDATE TB_Mensagem
SET emoji = ?
WHERE id = ?
""", (novo_emoji, id_msg))

cursor.execute("""
DELETE FROM TB_Mensagem
WHERE id = ?
""", (id_msg,))

conn.commit()

conn.close()
