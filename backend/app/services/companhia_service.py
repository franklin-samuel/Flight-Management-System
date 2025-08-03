from sqlalchemy.orm import Session
from app.database.models import CompanhiaAerea as CompanhiaDB
from app.services.mappers.companhia_mapper import companhia_from_db
from app.services.mappers.voo_mapper import voo_from_db
class CompanhiaService:
    def __init__(self, db: Session):
        self.db = db
    def criar_companhia(self, nome: str):
        nova = CompanhiaDB(nome=nome)
        self.db.add(nova)
        self.db.commit()
        self.db.refresh(nova)
        return companhia_from_db(nova)

    def listar_todas_companhias(self):
        companhias = self.db.query(CompanhiaDB).all()
        return [companhia_from_db(c) for c in companhias]

    def buscar_companhia_por_id(self, companhia_id: int):
        companhia = self.db.query(CompanhiaDB).filter_by(id=companhia_id).first()
        if companhia:
            return companhia_from_db(companhia)
        return None

    def deletar_companhia(self, companhia_id: int):
        companhia = self.db.query(CompanhiaDB).filter_by(id=companhia_id).first()
        if not companhia:
            raise ValueError("Companhia não encontrada.")
        self.db.delete(companhia)
        self.db.commit()


    def listar_voos_por_companhia(self, companhia_id: int):
        companhia = self.db.query(CompanhiaDB).filter_by(id=companhia_id).first()
        if not companhia:
            raise ValueError("Companhia não encontrada.")

        return [voo_from_db(voo) for voo in companhia.voos]
    
    