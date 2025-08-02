from sqlalchemy.orm import Session
from app.database.models import Passageiro as PassageiroDB
from app.services.mappers.passageiro_mapper import passageiro_from_db

def buscar_passageiro_por_cpf(db: Session, cpf: str):
    passageiro_db = db.query(PassageiroDB).filter_by(cpf=cpf).first()
    if not passageiro_db:
        return None
    return passageiro_from_db(passageiro_db)