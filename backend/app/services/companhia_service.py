from sqlalchemy.orm import Session
from app.database.models import CompanhiaAerea as CompanhiaDB
from app.services.mappers.companhia_mapper import companhia_from_db
def criar_companhia(db: Session, nome: str):
    nova = CompanhiaDB(nome=nome)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return companhia_from_db(nova)

