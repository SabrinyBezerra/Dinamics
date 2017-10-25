import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

lista = [(1, True, False),
         (2, False, True),
         (3, False, False)]

cursor.executemany("""
INSERT INTO TB_Visibilidade (id, publico, privado)
VALUES (?, ?, ?)
""", lista)

cursor.execute("""
SELECT * FROM TB_Visibilidade;
""")

for linha in cursor.fetchall():
    print(linha)

id_vis = 1
novo_publico = False
novo_privado = True

cursor.execute("""
UPDATE TB_Visibilidade
SET publico = ?, privado = ?
WHERE id = ?
""", (novo_publico, novo_privado, id_vis))

cursor.execute("""
DELETE FROM TB_Visibilidade
WHERE id = ?
""", (id_vis,))

conn.commit()

conn.close()
