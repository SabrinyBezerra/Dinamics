def menu():
    while True:
        try:
            opcao = int(input(
                "1) Login\n" \
                "2) Registro\n" \
                "0) Sair\n\n" \

            ))
        except:
            print("Opção inválida.")
            continue

        if(opcao == 0):
            break
        elif(opcao == 1):
            email = input("E-mail: ")
            senha = input("Senha: ")

             UsuarioDAO.LOGINDAO(email, senha)

            if(usuario is None):
                print("Credenciais incorretos.\n")
                continue
            else:
                menuDeUsuario(usuario)
        elif(opcao == 2):
            try:
                nome = input("Nome: ")
                email = input("E-mail: ")
                senha = input("Senha: ")
                sexo = input("Sexo: ")
                cidade = input("Cidade: ")
                data_nascimento = input("Data de nascimento: ")

               usuario = Usuario(nome, email, senha, profissao, sexo, data_nasc)
               
                menuDeUsuario(usuario)
            except:
                print("Erro!")
                continue

def menuUsuario(usuario: Usuario):
    while True:
        try:
            opcao = int(input(
                "\n 1) Ver Dados\n" \
                "2) Adicionar Amigo\n" \
                "3) Mandar mensagem\n" \
                "4) Ver amigos\n" \
                "0) Sair\n\n" \
                
            ))
        except:
            print("Opção inválida.")
            continue

        if(opcao == 0):
            break
        elif(opcao == 1):
            print("\nNome: %s" \
                  "\nE-mail: %s" \
                  "\nSexo: %s" \
                  "\nCidade: %s" \
                  "\nData de nascimento: %s" % (usuario.nome, usuario.email, usuario.sexo, usuario.cidade, usuario.data_nascimento))
        elif(opcao == 2):
            nome = input("Nome: ")

            usuarios = UsuarioDAO().PesquisaNome(nome)

            if(len(usuarios) == 0):
                print("Nenhum usuário encontrado.")
                continue
            elif(len(usuarios) == 1):
                try:
                    UsuarioDAO().inserirUsuario(usuario.id, usuarios[0].id)
                    print("Amigo adicionado.")
                except Exception as err:
                    print(err)
            else:
                print()
                i = 1
                for u in usuarios:
                    print("%s) %s - %s" % (i, u.nome, u.email))
                    i += 1

                n = input("Digite o número do usuário: ")

                u = UsuarioDAO().PesquisaID(usuarios[u - 1].id)

                if(u is None):
                    print("Usuário inválido.")
                else:
                    UsuarioDAO().inserirUsuario(usuario.id, u.id)
                    print("%s foi adicionado aos seus amigos." % (u.nome))
        elif(opcao == 3):
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

        elif(opcao == 4):
            amigos = UsuarioDAO().listarAmigos(usuario.id)

            i = 1
            for amigo in amigos:
                print("%s) %s" % (i, amigo.nome))
       
def main():
    menu()

if __name__ == '__main__':
    main()
