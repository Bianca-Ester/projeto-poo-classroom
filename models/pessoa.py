class Pessoa:
    def __init__(self, matricula, senha, id=None):
        self.matricula = matricula
        self.senha = senha
        self.id = id

    def to_dict(self):
        return{
            'id': self.id,
            'matricula': self.matricula,
            'senha': self.senha
        }


