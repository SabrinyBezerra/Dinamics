from model.Mensagem import Mensagem
from database.configDB import config
import mysql.connector

'''
Classe DAO de MENSAGEM e funções de inserirMensagem e listar
'''
class MensagemDAO():
    def inserirMensagem(self, mensagem: Mensagem):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            query = "INSERT INTO mensagem(texto, tipo, id_amigo, emoji)" \
                    "VALUES (%s, %s, %i, %i)"
            values = (mensagem.texto, mensagem.tipo, mensagem.id_amigo, mensagem.emoji)
            cursor.execute(query, values)
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def listarMensagem(self):
        try:
            mensagens = []
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            query = "SELECT * FROM mensagem"
            mensagens.append(query)
            for linha in mensagens():
                texto = linha[1]
                tipo = linha[2]
                id_amigo = linha[3]
                emoji = linha[4]
                mensagens = Mensagem(texto, tipo, id_amigo, emoji)

        except mysql.connector.Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
