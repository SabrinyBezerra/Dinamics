import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

class Mensagem():
    def __init__(self, emoji):
        self.emoji = emoji

    def inserir(self):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        lista = [(':)'),
                (':(')]
        cursor.executemany("""
        INSERT INTO TB_Mensagem (emoji)
        VALUES (?)
        """, lista)
        conn.commit()
        conn.close()

    def listar(self):
        mensagens = []
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM TB_Mensagem;
        """)
        for linha in cursor.fetchall():
            emoji = linha[1]
            mensagem = Mensagem(emoji)
            mensagens.append(mensagem)
        conn.close()

        return mensagens
