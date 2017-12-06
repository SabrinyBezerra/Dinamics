from model.Mensagem import Mensagem
class Chat(Mensagem):
    def __init__(self, id_usuario, texto, tipo, emoji, id_amigo, conversa):
        super(Chat, self).__init__(texto, tipo, id_amigo, emoji)
        self.id_usuario = id_usuario
        self.conversa = conversa
