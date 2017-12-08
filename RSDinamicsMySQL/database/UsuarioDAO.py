import mysql.connector
from model.Usuario import Usuario
from model.Amigo import Amigo
from model.Usuario_Amigo import Usuario_Amigo
from database.configDB import config

class UsuarioDAO():

    def inserirUsuario(usuario: Usuario):
        try:
            # Conexão com a base de dados.
            conn = mysql.connector.connect(**config)  # Nome do BD.
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            # Script de Inserção.
            query = "INSERT INTO usuario(id_usuario, nome, nascimento, genero, email, senha) " \
                    "VALUES(%i, %s, %s, %c, %s, %s)"
            # Valores.
            values = (usuario.id_usuario, usuario.nome, usuario.nascimento, usuario.genero, usuario.email, usuario.senha)
            cursor.execute(query, values)
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def removerAmigo(self, id_amigo):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            query = "DELETE FROM usuario_Amigo" \
                    "WHERE id_amigo = %i"

            values = (id_amigo)
            cursor.execute(query, values)
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def adicionarAmigo(self, usuario = Usuario_Amigo):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            query = "UPDATE FROM usuario, amigo, usuario_amigo" \
                    "SET solicitacao = %s, amizade = %s" \
                    "WHERE nome = %s"
            values = (usuario.nome_amigo)
            cursor.execute(query, values)
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def listarUsuario(self):
        try:
            usuarios = []
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            query = "SELECT * FROM usuario"
            usuarios.append(query)
            for linha in usuarios():
                nome = linha[1]
                nascimento = linha[2]
                genero = linha[3]
                email = linha[4]
                senha = linha[5]
                usuarios = Usuario(nome, nascimento, genero, email, senha)
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def LOGINDAO(self, email, senha):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            query = "SELECT email, senha FROM usuario WHERE email = %s, senha = %s"
            values = (email, senha)
            cursor.execute(query, values)
            if (query, values is None):
                return False
            else:
                return True
        except mysql.connector.Error as error:
            print(error)
            return False
        finally:
            cursor.close()
            conn.close()
