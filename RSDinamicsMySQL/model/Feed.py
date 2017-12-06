from model.Mensagem import Mensagem
class Feed(Mensagem):
    def __init__(self, id_publicacao, publicacao, texto, tipo, id_amigo, emoji):
        super(Feed, self).__init__(texto, tipo, id_amigo, emoji)
        self.id_publicacao = id_publicacao
        self.publicacao = publicacao
