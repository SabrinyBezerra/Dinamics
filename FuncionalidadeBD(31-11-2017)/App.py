from Model.Usuario import Usuario
import sqlite3

def cadastrarUsuario():

    #Solicitando os dados para cadastramento do usuario

    usuario = []
    nome = input("Digite seu nome:  ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha de usuário: ")
    profissao = input("Digite sua profissão: ")
    sexo = input("Digite seu sexo: F/M/PREFIRO NÃO DIZER")
    data_nasc = input("Digite sua data de nascimento: ")
    usuario = Usuario(nome, email, senha, profissao, sexo, data_nasc)

    #Inserindo dados obtidos na tabela

    Usuario.inserir(usuario)

def menu():
    escolha = int(input('''
    MENU - D I N A M I C S -
1 - Cadastrar Usuario

escolha: '''))
    if escolha == 1:
        cadastrarUsuario()
    else:
        print('Escolha invalida, tente novamente')
        menu()

def main(args = []):
    menu()
    
if (__name__ == '__main__'):
     main()
