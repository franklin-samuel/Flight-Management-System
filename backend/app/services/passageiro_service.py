from sqlalchemy.orm import Session
from app.database.models import Passageiro as PassageiroDB
from app.services.mappers.passageiro_mapper import passageiro_from_db, bagagem_from_db
class PassageiroService:
    def __init__(self, db: Session):
        self.db = db
    def criar_funcionario(self, nome: str, cpf: str):
        passageiro_db = PassageiroDB(nome=nome, cpf=cpf)
        self.db.add(passageiro_db)
        self.db.commit()
        self.db.refresh(passageiro_db)
        return passageiro_from_db(passageiro_db)

    def listar_passageiros(self):
        passageiros_db = self.db.query(PassageiroDB).all()
        return [passageiro_from_db(passageiro) for passageiro in passageiros_db]

    def buscar_passageiro_por_cpf(self, cpf: str):
        passageiro_db = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro_db:
            return None
        return passageiro_from_db(passageiro_db)
    
    def listar_bagagem_por_passageiro(self, cpf:str):
        passageiro = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro:
            raise ValueError ("Passageiro não encontrado")
        
        return [bagagem_from_db(bagagem) for bagagem in passageiro.bagagens]