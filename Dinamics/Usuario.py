import sqlite3
conn = sqlite3.connect('dinamics.db')
cursor = conn.cursor()

class Usuario():
    def __init__(self, nome, email, senha, profissao, sexo, data_nasc):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.profissao = profissao
        self.sexo = sexo
        self.data_nasc = data_nasc

    def inserir(self):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute('''
          INSERT INTO TB_Usuario (nome, email, senha, profissao, sexo, data_nasc)
          VALUES (self.nome, self.email, self.senha, self.profissao,
           self.sexo, self.data_nasc)
        ''')
        conn.commit()
        conn.close()

    def listar(self):
        usuarios = []
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM TB_Usuario;
        """)
        for linha in cursor.fetchall():
            nome = linha[1]
            email = linha[2]
            senha = linha[3]
            profissao = linha[4]
            sexo = linha[5]
            data_nasc = linha[6]
            usuario = Usuario(nome, email, senha, profissao, sexo, data_nasc)
            usuarios.append(usuario)
            
            

        conn.close()

        return usuarios

    def deletar(self, id):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        id = input("")
        cursor.execute("""
        DELETE FROM TB_Usuario
        WHERE id = ?
        """, (id))
        conn.commit()
        conn.close()


    def atualizar(self, id, nome, email, senha, profissao, sexo, data_nasc):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE TB_Usuario
        SET email = ?, senha = ?, nome = ?, profissao = ?, sexo = ?, data_nasc = ?
        WHERE id = ?
        """, (email, senha, nome, profissao, sexo, data_nasc, id))
        conn.commit()
        conn.close()
       
    def TrocarMensagem(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        mensagem = str(input("Digite a mensagem para ser enviada: "))
        usuario = str(input("Digite o nome do amigo que receberá a mensagem: "))
        cursor.execute("""
        SELECT nome FROM TB_Usuario
        WHERE nome=?
        """, (usuario))
        cursor.execute("""
        UPDATE TB_Mensagem
        SET mensagem=?
        """, (mensagem))
