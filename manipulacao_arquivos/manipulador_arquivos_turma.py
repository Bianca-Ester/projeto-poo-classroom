import json
import os
from models.turma import Turma
import utils as ut

CAMINHO_ARQUIVO = "data/turma.json"


def carregar_turmas():
    lista_turmas = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_turmas
        with open(CAMINHO_ARQUIVO, "r") as f:
            turmas = json.load(f)
            for t in turmas:
                obj_turma = Turma(
                    nome=t['nome'],
                    senha=t['senha'],
                    admin=t['administrador'],
                    id=t['id']
                )
                lista_turmas.append(obj_turma)
        return lista_turmas
    except Exception as e:
        print(e)
        return []


def salvar_turmas(lista):
    try:
        dados = [turma.to_dict() for turma in lista]
        with open(CAMINHO_ARQUIVO, "w") as f:
            json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_turma(turma):
    try:
        turmas = carregar_turmas()
        proximo_id = ut.calcular_proximo_id(turmas)
        turma.id = proximo_id
        turmas.append(turma)
        return salvar_turmas(turmas), turma
    except Exception as e:
        print(e)
        return None


def buscar_turma_por_id(id):
    try:
        turmas = carregar_turmas()
        for t in turmas:
            if t.id == id:
                return t
    except Exception as e:
        print(e)
        return None


def buscar_turma_por_nome(nome):
    try:
        turmas = carregar_turmas()
        for turma in turmas:
            if turma.nome == nome:
                return turma
    except Exception as e:
        print(e)
        return None


def atualizar_turma(turma):
    try:
        turmas = carregar_turmas()
        for idx, t in enumerate(turmas):
            if t.id == turma.id:
                turmas[idx] = turma
                salvar_turmas(turmas)
                return True
    except Exception as e:
        print(e)
        return False


def remover_turma(id):
    try:
        turmas = carregar_turmas()
        novas_turmas = [t for t in turmas if t.id != id]
        return salvar_turmas(novas_turmas)
    except Exception as e:
        print(e)
        return False
