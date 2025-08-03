#CHECAR UTILIDADE

import json
import os
from models.professor import Professor
import utils as ut


CAMINHO_ARQUIVO = "data/professor.json"


def carregar_professores():
    lista_professores = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_professores
        f = open(CAMINHO_ARQUIVO, "r")
        professores = json.load(f)
        for p in professores:
            obj_professor = Professor(**p)
            lista_professores.append(obj_professor)
        return lista_professores
    except Exception as e:
        print(e)
        
        
def salvar_professores(lista):
    try:
        dados = [professor.to_dict() for professor in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_professor(professor):
    try:
        # le arquivo em formato de adicao (append)
        professores = carregar_professores()
        
        # gera novo id
        proximo_id = ut.calcular_proximo_id(professores)
        
        # atribui novo id a editora que quer inserir
        professor.id = proximo_id
            
        # adiciona a nova editora na lista
        professores.append(professor)
                
        # salva a nova lista no arquivo
        return salvar_professores(professores), professor
    except Exception as e:
        print(e)
        return None
    
def buscar_professor_por_matricula(matricula):  
    try:  
        professores = carregar_professores()
        for p in professores:
            if p.matricula == matricula:
                return p
    except Exception as e:
        print(e)
        return None
