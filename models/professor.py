from models.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, matricula, senha, id=None, turma=None):
        super().__init__(matricula, senha, id)
        self.turma = turma


