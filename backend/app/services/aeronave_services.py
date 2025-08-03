from sqlalchemy.orm import Session
from app.database.models import MiniAeronave as MiniAeronaveDB
from app.services.mappers.voo_mapper import aeronave_from_db

class AeronaveService:
    def __init__(self, db: Session):
        self.db = db

    def criar_aeronave(self, modelo: str, capacidade: int):
        nova = MiniAeronaveDB(modelo, capacidade)
        self.db.add(nova)
        self.db.commit()
        self.db.refresh(nova)
        return aeronave_from_db(nova)    
    
    def listar_aeronaves(self):
        Aeronaves = self.db.query(MiniAeronaveDB).all()
        return [aeronave_from_db(aeronave)for aeronave in Aeronaves]
    
    def buscar_aeronave(self, modelo: str):
        aeronave = self.db.query(MiniAeronaveDB).filter_by(modelo=modelo).first()
        if aeronave:
            return aeronave_from_db(aeronave)
        return None
    
    def deletar_aeronave(self, modelo: str):
        aeronave = self.db.query(MiniAeronaveDB).filter_by(modelo=modelo).first()
        if not aeronave:
            raise ValueError("Aeronave não encontrada.")
        self.db.delete(aeronave)
        self.db.commit()