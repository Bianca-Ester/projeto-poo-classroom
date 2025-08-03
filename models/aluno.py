#CORRIRGIR DIAGRAMA, APLICAR E VER UTILIDADE

from models.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, senha, matricula):
        super().__init__(senha, matricula)
        self.turmas = []
