from sqlalchemy.orm import Session
from app.database.models import Funcionario as FuncionarioDB
from app.services.mappers.funcionario_mapper import funcionario_from_db

def criar_funcionario(db: Session, nome: str, matricula: str):
    funcionario_db = FuncionarioDB(nome=nome, matricula=matricula)
    db.add(funcionario_db)
    db.commit()
    db.refresh(funcionario_db)
    return funcionario_from_db(funcionario_db)

def buscar_funcionario_por_matricula(db: Session, matricula: str):
    funcionario_db = db.query(FuncionarioDB).filter_by(matricula=matricula).first()
    if not funcionario_db:
        return None
    return funcionario_from_db(funcionario_db)