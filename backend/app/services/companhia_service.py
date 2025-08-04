from sqlalchemy.orm import Session
from app.database.models import CompanhiaAerea as CompanhiaDB
from app.services.mappers.companhia_mapper import companhia_from_db, companhia_to_db
from app.models.voo import CompanhiaAerea, Voo
from app.services.mappers.voo_mapper import voo_to_db
class CompanhiaService:
    def __init__(self, db: Session):
        self.db = db
    def criar_companhia(self, nome: str):
        companhia = CompanhiaAerea(nome=nome)
        companhia_db = companhia_to_db(companhia)

        self.db.add(companhia_db)
        self.db.commit()
        self.db.refresh(companhia_db)

        return companhia_db
    def listar_todas_companhias(self):
        companhias = self.db.query(CompanhiaDB).all()
        return companhias

    def buscar_companhia_por_id(self, companhia_id: int):
        companhia = self.db.query(CompanhiaDB).filter_by(id=companhia_id).first()
        if companhia:
            return companhia
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

        return [voo for voo in companhia.voos]
    

    def adicionar_voo_a_companhia(self, companhia_id: int, voo: Voo):
        companhia_db = self.db.query(CompanhiaDB).filter_by(id=companhia_id).first()
        if not companhia_db:
            raise ValueError("Companhia não encontrada")

        companhia_poo = companhia_from_db(companhia_db)
        companhia_poo.adicionar_voo(voo)

        voos_db = [voo_to_db(v) for v in companhia_poo._voos]
        companhia_db.voos = voos_db

        self.db.commit()
        self.db.refresh(companhia_db)

        return companhia_db

    def buscar_voo(self, companhia_id: int, numero_voo: str):
        companhia = self.db.query(CompanhiaDB).filter_by(id=companhia_id).first()
        companhia_poo = companhia_from_db(companhia)
        voo = companhia_poo.buscar_voo(numero_voo)
        return voo_to_db(voo)
    
    