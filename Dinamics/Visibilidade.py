import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

class Visibilidade():
    def __init__ (self, publico, privado):
        self.publico = publico
        self.privado = privado

    def inserir(self):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO TB_Mensagem (publico, privado)
        VALUES (self.publico, self.privado)
        """)
        conn.commit()
        conn.close()

    def atualizar(self, publico, privado):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE TB_Usuario
        SET publico = ?, privado = ?
        WHERE id = ?
        """, (publico, privado, id))
        conn.commit()
        conn.close()
