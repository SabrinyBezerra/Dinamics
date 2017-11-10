from Model.Usuario import Usuario

def Menu():
    print("///// D I N A M I C S /////")
    print("     1 - FAZER CADASTRO    ")

def FazerCadastro():
    nome = input("Digite seu nome completo: ")
    email = input("Digite seu email: ")
    profissao = input("Digite sua profissão: ")
    data_de_nascimento = input ("digite sua data de nascimento: (DD-MM-AA)")
    sexo = input("Digite seu sexo: F / M / PREFIRO NÃO DIZER")
    senha = input("Crie uma senha: ")

    usuario = Usuario(nome, email, senha, profissao, sexo, data_de_nascimento)

    return usuario

def main(args = []):

    Menu()



if (__name__ == "__main__"):
    main()