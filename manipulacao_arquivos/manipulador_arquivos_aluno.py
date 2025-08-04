import json
import os
from models.aluno import Aluno
import utils as ut


CAMINHO_ARQUIVO = "data/aluno.json"


def carregar_alunos():
    lista_alunos = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_alunos
        f = open(CAMINHO_ARQUIVO, "r")
        alunos = json.load(f)
        for a in alunos:
            obj_aluno = Aluno(**a)
            lista_alunos.append(obj_aluno)
        return lista_alunos
    except Exception as e:
        print(e)
        
        
def salvar_alunos(lista):
    try:
        dados = [aluno.to_dict() for aluno in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_aluno(aluno):
    try:
        alunos = carregar_alunos()
        
        proximo_id = ut.calcular_proximo_id(alunos)
        
        aluno.id = proximo_id
            
        alunos.append(aluno)
                
        return salvar_alunos(alunos), aluno
    except Exception as e:
        print(e)
        return None
    
def buscar_aluno_por_matricula(matricula):  
    try:  
        alunos = carregar_alunos()
        for a in alunos:
            if a.matricula == matricula:
                return a
    except Exception as e:
        print(e)
        return None
