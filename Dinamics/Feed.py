import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

lista = [(1, 1, 'BOM DIA GENTE'),
         (2, 2, 'BOA TARDE GENTE'),
         (3, 3, 'BOA NOITE GALERA')]

cursor.executemany("""
INSERT INTO TB_Feed (id, id_publicacao, publicacao)
VALUES (?, ?, ?)
""", lista)

cursor.execute("""
SELECT * FROM TB_Feed;
""")

for linha in cursor.fetchall():
    print(linha)

id_feed = 1
novo_publicacao = 'BOM DIA GALERA'

cursor.execute("""
UPDATE TB_Feed
SET publicacao = ?
WHERE id = ?
""", (novo_publicacao, id_feed))

cursor.execute("""
DELETE FROM TB_Feed
WHERE id = ?
""", (id_feed,))

conn.commit()

conn.close()
