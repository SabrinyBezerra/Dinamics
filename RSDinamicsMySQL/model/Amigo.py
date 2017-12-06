from model.Pessoa import Pessoa

class Amigo(Pessoa):
    def __init__(self, id_amigo, nome, nascimento, genero):
        super(Amigo, self).__init__(nome, genero)
        self.id_amigo = id_amigo
        self.nascimento = nascimento

    def __str__(self):
        return "Amigo <%s>" % (self.nome)

    def __repr__(self):
        return self.__str__()
