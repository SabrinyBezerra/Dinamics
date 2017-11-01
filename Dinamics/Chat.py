import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

class Chat():
    def __init__(self, id_usuario, conversa):
        self.id_usuario = id_usuario
        self.conversa =  conversa

    def inserir(self):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute('''
                 INSERT INTO TB_Usuario (id_usuario, conversa)
                 VALUES (self.id_usuario, self.conversa)
               ''')
        conn.commit()
        conn.close()

    def listar(self):
        Chats = []
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM TB_Chat;
        """)
        for linha in cursor.fetchall():
            id_usuario = linha[1]
            conversa = linha[2]
            chat = chat(id_usuario, conversa)
            chat.append(chat)
        conn.close()

        return chat

    def deletar(self, id):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        id = input("")
        cursor.execute("""
        DELETE FROM TB_Chat
        WHERE id = ?
        """, (id))
        conn.commit()
        conn.close()

    def atualizar(self, id, id_usuario, conversa):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE TB_Chat
        SET id = ?, id_usuario = ?, conversa = ?
        WHERE id = ?
        """, (id, id_usuario, conversa))
        conn.commit()
        conn.close()


