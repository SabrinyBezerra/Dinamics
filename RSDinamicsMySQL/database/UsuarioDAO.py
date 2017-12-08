import mysql.connector
from model.Usuario import Usuario
from database.configDB import config

class UsuarioDAO():

    def inserirUsuario(usuario: Usuario):

        # Script de Inserção.
        query = "INSERT INTO usuario(id_usuario, nome, nascimento, genero, email, senha) " \
                "VALUES(%i, %s, %s, %c, %s, %s)"
        # Valores.
        values = (usuario.id_usuario, usuario.nome, usuario.nascimento, usuario.genero, usuario.email, usuario.senha)

        try:
            # Conexão com a base de dados.
            conn = mysql.connector.connect(**config)  # Nome do BD.
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)
            # Último id da redesocial inserida no banco.
            #if cursor.lastrowid:
                #idRedeSocial = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        #return id_usuario
