from sqlalchemy.orm import Session
from app.database.models import Passageiro as PassageiroDB
from app.services.mappers.passageiro_mapper import passageiro_to_db, bagagem_to_db, passageiro_from_db
from app.models.pessoa import Passageiro
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
        passageiro_poo = Passageiro(nome=passageiro.nome, cpf=passageiro.cpf,
                                    bagagens=[bagagem for bagagem in passageiro.bagagens])
        bagagens = passageiro_poo.listar_bagagens()

        return [bagagem_to_db(bagagem)for bagagem in bagagens]

    def deletar_passageiro(self, cpf:str):
        passageiro = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro:
            raise ValueError ("Passageiro não encontrado")
        
        self.db.delete(passageiro)
        self.db.commit()

    def adicionar_bagagem(self, cpf:str, bagagem):
        passageiro = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro:
            raise ValueError ("Passageiro não encontrado")
        passageiro_poo = passageiro_from_db(passageiro)
        passageiro_poo.adicionar_bagagem(bagagem)

        passageiro.bagagens = passageiro_poo.bagagens

        self.db.commit()
        self.db.refresh(passageiro)
        return passageiro