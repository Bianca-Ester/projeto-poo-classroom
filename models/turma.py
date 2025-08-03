class Turma:
    def __init__(self, nome, senha, admin, id=None):
        self.nome = nome
        self.__senha = senha
        self.admin = admin
        self.id = id

    def to_dict(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'senha': self.__senha,
            'administrador': self.admin
        }
