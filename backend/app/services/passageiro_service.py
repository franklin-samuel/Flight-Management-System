from sqlalchemy.orm import Session
from app.database.models import Passageiro as PassageiroDB
from app.services.mappers.passageiro_mapper import passageiro_from_db

def criar_funcionario(db: Session, nome: str, cpf: str):
    passageiro_db = PassageiroDB(nome=nome, cpf=cpf)
    db.add(passageiro_db)
    db.commit()
    db.refresh(passageiro_db)
    return passageiro_from_db(passageiro_db)

def listar_passageiros(db: Session):
    passageiros_db = db.query(PassageiroDB).all()
    return [passageiro_from_db(passageiro) for passageiro in passageiros_db]

def buscar_passageiro_por_cpf(db: Session, cpf: str):
    passageiro_db = db.query(PassageiroDB).filter_by(cpf=cpf).first()
    if not passageiro_db:
        return None
    return passageiro_from_db(passageiro_db)