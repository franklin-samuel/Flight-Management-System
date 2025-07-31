# Funções CRUD (adicionar_voo, buscar_passageiro, ...)
from sqlalchemy.orm import Session
from app.models.voo import Voo
from app.models.pessoa import Passageiro

def adicionar_voo(db: Session, numero_voo: str, origem: str, destino: str, aeronave: str):
    novo_voo = Voo(
        numero_voo=numero_voo,
        origem=origem,
        destino=destino,
        aeronave=aeronave
    )
    db.add(novo_voo)
    db.commit()
    db.refresh(novo_voo)
    return novo_voo

def buscar_voo(db: Session, numero_voo: str):
    return db.query(Voo).filter(Voo.numero_voo == numero_voo).first()

def listar_voos(db: Session):
    return db.query(Voo).all()

def buscar_passageiro(db: Session, cpf: str):
    return db.query(Passageiro).filter(Passageiro.cpf == cpf).first()

def adicionar_passageiro(db: Session, nome: str, cpf: str):
    novo_passageiro = Passageiro(
        nome=nome,
        cpf=cpf,
    )
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro