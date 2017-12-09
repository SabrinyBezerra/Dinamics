from model.Usuario import Usuario
from model.RedeSocialDinamics import RedeSocialDinamics
from database.RedeSocialDinamicsDAO import RedeSocialDinamicsDAO
from database.UsuarioDAO import UsuarioDAO

usuario = None

'''
    Função para exibir o menu. Defina os números para acessar as opções.
'''
def exibirMenu():
    print("\ \ \ \ D I N A M I C S / / / / \n"
        "                                    "
        "     \ \ \ \ M E N U / / / /"
        " 1 - Definir nome da rede social\n"
        " 2 - Cadastrar Usuario\n"
        " 3 - Login\n"
        " 4 - Listar Usuario\n"
        " 5 - Excluir Amizade\n"
        " 0 - Sair")
'''
    Login do Usuario
'''
def loginUSER():
    email = input("Digite seu email: \n")
    senha = input("Digite sua senha: \n")
    try:
        UsuarioDAO.LOGINDAO(email, senha)
    except:
        print("Usuario não tem cadastro...")

'''
    Criação da Rede Social.
'''
def criarRedeSocial():
    # Necessário inicializar os valores da RedeSocial.
    nome = str(input("Digite um nome da Rede Social: "))
    redeSocial = RedeSocialDinamics(nome)
    redeSocialDAO = RedeSocialDinamicsDAO()
    idRedeSocial = redeSocialDAO.inserirRedeSocial(redeSocial)

'''
    Criação do Usuário.
'''
def criarUsuario(usuario: Usuario):

    #Solicitando os dados para cadastramento do usuario

    usuario = []
    nome = input("Digite seu nome:  ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha de usuário: ")
    profissao = input("Digite sua profissão: ")
    sexo = input("Digite seu sexo: ")
    data_nasc = input("Digite sua data de nascimento: ")
    usuario = Usuario(nome, email, senha, profissao, sexo, data_nasc)

'''
    Listar os Usuários.
'''
def listarUsuarios():
    UsuarioDAO.listarUsuario()

'''
    Remover um Usuário.
'''
def removerUsuario(id: int):
    UsuarioDAO.removerAmigo(id)

def main(args = []):

    continuar = True

    while continuar:
        try:
            # Exibição do Menu de Opções.
            exibirMenu()
            # Continuar a execução do programa.
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                criarRedeSocial()

            elif (opcao == 2):
                criarUsuario()
                
            elif (opcao == 3):
                loginUSER() 
                
            elif (opcao == 4):     
                listarUsuarios()
                
            elif (opcao == 5):
                removerUsuario()
                
            elif (opcao == 0):
                continuar = False
            else:
                print("Opção inválida!!")

        except ValueError:
            print("ERROR! Digite um valor válido")

if (__name__ == "__main__"):
    main()
