from sqlalchemy.orm import Session
from app.database.models import Passageiro as PassageiroDB, Bagagem as BagagemDB
from app.services.mappers.passageiro_mapper import passageiro_to_db, bagagem_to_db, passageiro_from_db
from app.models.pessoa import Passageiro
from app.models.bagagem import Bagagem
class PassageiroService:
    def __init__(self, db: Session):
        self.db = db
    def criar_passageiro(self, nome: str, cpf: str):
        passageiro_db = PassageiroDB(nome=nome, cpf=cpf)
        self.db.add(passageiro_db)
        self.db.commit()
        self.db.refresh(passageiro_db)
        return passageiro_db

    def listar_passageiros(self):
        passageiros_db = self.db.query(PassageiroDB).all()
        return [passageiro for passageiro in passageiros_db]

    def buscar_passageiro_por_cpf(self, cpf: str):
        passageiro_db = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro_db:
            return None
        return passageiro_db
    
    def listar_bagagem_por_passageiro(self, cpf:str):
        passageiro = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro:
            raise ValueError ("Passageiro não encontrado")

        return passageiro.bagagens

    def deletar_passageiro(self, cpf:str):
        passageiro = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro:
            raise ValueError ("Passageiro não encontrado")
        
        self.db.delete(passageiro)
        self.db.commit()

    def adicionar_bagagem(self, cpf:str, descricao: str, peso: float):
            passageiro = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
            if not passageiro:
                raise ValueError("Passageiro não encontrado")

            nova_bagagem = BagagemDB(descricao=descricao, peso=peso, passageiro_id=passageiro.id)

            self.db.add(nova_bagagem)
            self.db.commit()
            self.db.refresh(nova_bagagem)

            return nova_bagagem

    def deletar_bagagem(self, cpf:str, bagagem_id: int):
        passageiro = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro:
            raise ValueError ("Passageiro não encontrado")
        bagagem = self.db.query(BagagemDB).filter_by(id=bagagem_id).first()
        if bagagem in passageiro.bagagens:
            self.db.remove(bagagem)
            self.db.commit()

        return