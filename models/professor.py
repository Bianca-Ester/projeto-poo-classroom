#CORRIRGIR DIAGRAMA, APLICAR E VER UTILIDADE

from models.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, senha, matricula, turma=None):
        super().__init__( senha, matricula)
        self.turma = turma
