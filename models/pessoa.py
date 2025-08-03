#CORRIRGIR DIAGRAMA, APLICAR E VER UTILIDADE

class Pessoa:
    def __init__(self, senha, matricula):
        self.__senha = senha
        self.matricula = matricula

    def to_dict(self):
        return{
            'id': self.id,
            'senha': self.__senha,
            'matricula': self.matricula
        }
