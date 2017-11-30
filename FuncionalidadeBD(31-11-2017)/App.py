from Model.Usuario import Usuario
import sqlite3

def menu():
    escolha = int(input('''
    MENU - D I N A M I C S -
1 - Cadastrar Usuario

escolha: '''))
    if escolha == 1:
        print('Opção A escolhida')
    else:
        print('Escolha invalida, tente novamente')
        menu()

def main(args = []):
    menu()
    
if (__name__ == '__main__'):
     main()