class Turma:
    def __init__(self, nome, senha, admin, id=None):
        self.nome = nome
        self.senha = senha
        self.admin = admin
        self.id = id

    def to_dict(self):
        return{
            'nome': self.nome,
            'senha': self.senha,
            'administrador': self.admin,
            'id': self.id
        }

