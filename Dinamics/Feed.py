import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()


class Feed():
    def __init__(self, id_publicacao, publicacao):
        self.id_publicacao = id_publicacao
        self.publicacao = publicacao

    def inserir(self):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute('''
                 INSERT INTO TB_Feed (id_publicacao, publicacao)
                 VALUES (self.id_publicacao, self.publicacao)
               ''')
        conn.commit()
        conn.close()

    def listar(self):
        Feed = []
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM TB_Feed;
        """)
        for linha in cursor.fetchall():
            id_publicacao = linha[1]
            publicaao= linha[2]
            feed = feed(id_usuario, conversa)
            feed.append(feed)
        conn.close()

        return feed

    def deletar(self, id):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        id = input("")
        cursor.execute("""
        DELETE FROM TB_Fedd
        WHERE id = ?
        """, (id))
        conn.commit()
        conn.close()

    def atualizar(self, id, id_publicacao, publicacao):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE TB_Feed
        SET id = ?, id_publicacao = ?, publicacao = ?
        WHERE id = ?
        """, (id, id_publicacao, publicacao))
        conn.commit()
        conn.close()


