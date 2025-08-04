from models.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, matricula, senha, id=None):
        super().__init__(matricula, senha, id)
        self.turmas = []

