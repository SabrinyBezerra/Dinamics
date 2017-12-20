from model.Usuario import Usuario
from model.RedeSocialDinamics import RedeSocialDinamics
from database.RedeSocialDinamicsDAO import RedeSocialDinamicsDAO
from database.UsuarioDAO import UsuarioDAO

usuario = None

'''
Função referente ao usuário cadastrado na rede social
'''
def menuUsuario(usuario: Usuario):
    while True:
        try:
            print("\ \ \ \ D I N A M I C S / / / / \n"
                  "                                    "
                  "     \ \ \ \ M E N U / / / /")
            opcao = int(input(
                "\n 1 - Ver Dados\n" \
                "2 - Adicionar Amigo\n" \
                "3 - Mandar mensagem\n" \
                "4 - Ver amigos\n" \
                "0 - Sair\n\n" \
 \
                ))
        except:
            print("Opção inválida.")
            continue
#Opção de SAIR
        if (opcao == 0):
            break
#Opção de ver dados/perfil
        elif (opcao == 1):
            print("\ \ \ \ D I N A M I C S / / / / \n")
            print("\nNome: %s" \
                  "\nE-mail: %s" \
                  "\nSexo: %s" \
                  "\nCidade: %s" \
                  "\nData de nascimento: %s" % (
                  usuario.nome, usuario.email, usuario.sexo, usuario.cidade, usuario.data_nascimento))
#Opção de ADICIONAR AMIGOS pela pesquisa do nome
        elif (opcao == 2):
            print("\ \ \ \ D I N A M I C S / / / / \n")
            nome = input("Nome: ")

            usuarios = UsuarioDAO().PesquisaNome(nome)

            if (len(usuarios) == 0):
                print("Nenhum usuário encontrado.")
                continue
            elif (len(usuarios) == 1):
                try:
                    UsuarioDAO().inserirUsuario(usuario.id, usuarios[0].id)
                    print("Amigo adicionado.")
                except Exception as err:
                    print(err)
            else:
                #Pesquisa do usuário pelo ID
                print()
                i = 1
                for u in usuarios:
                    print("%s) %s - %s" % (i, u.nome, u.email))
                    i += 1

                n = input("Digite o número do usuário: ")

                u = UsuarioDAO().PesquisaID(usuarios[u - 1].id)

                if (u is None):
                    print("Usuário inválido.")
                else:
                    UsuarioDAO().inserirUsuario(usuario.id, u.id)
                    print("%s foi adicionado aos seus amigos." % (u.nome))
#Opção de MANDAR MENSAGEM
        elif (opcao == 3):
            print("\ \ \ \ D I N A M I C S / / / / \n")
            nome = input("Nome: ")

            usuarios = UsuarioDAO().PesquisaNome(nome)

            if (len(usuarios) == 0):
                print("Nenhum usuário encontrado.")
                continue
            elif (len(usuarios) == 1):
                try:
                    texto = input("Mensagem: ")
                    mensagem = Mensagem(usuario, usuarios[0], texto, str(date.today()))

                    MensagemDAO().insert(mensagem)
                    print("Mensagem enviada.")
                except Exception as err:
                    print(err)
            else:
            #Mandar mensagem pelo ID do usuário
                print()
                i = 1
                for u in usuarios:
                    print("%s) %s - %s" % (i, u.nome, u.email))
                    i += 1

                n = input("Digite o número do usuário: ")

                u = UsuarioDAO().PesquisaID(usuarios[u - 1].id)

                if (u is None):
                    print("Usuário inválido.")
                else:
                    try:
                        texto = input("Mensagem: ")
                        mensagem = Mensagem(usuario, usuarios[0], texto, str(date.today()))

                        MensagemDAO().insert(mensagem)
                        print("Mensagem enviada.")
                    except Exception as err:
                        print(err)
#Opção de ver AMIGOS
        elif (opcao == 4):
            print("\ \ \ \ D I N A M I C S / / / / \n")
            amigos = UsuarioDAO().listarAmigos(usuario.id)

            i = 1
            for amigo in amigos:
                print("%s) %s" % (i, amigo.nome))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

'''
    Função para exibir o menu. Defina os números para acessar as opções.
'''
def menu():
    while True:
        try:
            print("\ \ \ \ D I N A M I C S / / / / \n"
            "                                    ")
            opcao = int(input(
                "1 - Login\n" \
                "2 - Registro\n" \
                "0 - Sair\n" \

            ))
        except:
            print("Opção inválida.")
            continue
#opção de SAIR
        if(opcao == 0):
            break
#opção de efetuar o LOGIN
        elif(opcao == 1):
            email = input("E-mail: ")
            senha = input("Senha: ")

            UsuarioDAO.LOGINDAO(email, senha)
#Caso o usuário não exista o programa apresentará a seguinte mensagem
        if(usuario is None):
            print("Credenciais incorretos.\n")
            continue
#Caso o usuário exista, será chamada a função menuDeUsuario
        else:
            menuDeUsuario(usuario)
#Opção de efetuar REGISTRO na rede social
        if(opcao == 2):
            try:
                nome = input("Nome: ")
                email = input("E-mail: ")
                senha = input("Senha: ")
                sexo = input("Sexo: ")
                cidade = input("Cidade: ")
                data_nascimento = input("Data de nascimento: ")

                usuario = Usuario(nome, email, senha, sexo, cidade, data_nascimento)
               
                menuDeUsuario(usuario)
            except:
                print("Erro!")
                continue

       
def main():
    menu()

if __name__ == '__main__':
    main()
