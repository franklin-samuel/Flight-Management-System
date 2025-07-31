from app.database.crud import adicionar_voo, buscar_voo, listar_voos, buscar_passageiro, adicionar_passageiro
from sqlalchemy.orm import Session
from flask import request
from app.models.voo import MiniAeronave

#Expor Função no método POST
def criar_voo(db: Session, data):
    numero_voo = data.get("numero_voo")
    origem = data.get("origem")
    destino = data.get("destino")
    modelo = data.get("modelo")
    capacidade = data.get("capacidade")

    if not all([numero_voo, origem, destino, modelo, capacidade]):
        raise Exception("Campos obrigatórios ausentes")
    
    voo_existente = buscar_voo(db, numero_voo)
    if voo_existente:
        raise Exception(f"Voo {numero_voo} já existe.")
    
    aeronave = MiniAeronave(modelo=modelo, capacidade=int(capacidade))

    novo_voo = adicionar_voo(db, numero_voo, origem, destino, aeronave)

    return novo_voo

#Expor função no método GET
def listar_todos_voos(db: Session):
    return listar_voos(db)

def adicionar_passageiro_ao_voo(db: Session, voo, passageiro):
    if passageiro in voo.passageiros:
        raise Exception("Passageiro já está no voo.")
    
    if len(voo.passageiros) >= voo.aeronave.capacidade:
        raise Exception("Capacidade da aeronave atingida. Não é possível adicionar mais passageiros.")
    
    novo_passageiro = adicionar_passageiro(db, passageiro.nome, passageiro.cpf)
    voo.passageiros.append(novo_passageiro)
    
    db.commit()
    db.refresh(voo)
    return voo

def buscar_passageiro_por_cpf(db: Session, cpf: str):
    passageiro = buscar_passageiro(db, cpf)
    if not passageiro:
        raise Exception("Passageiro não encontrado.")
    return passageiro