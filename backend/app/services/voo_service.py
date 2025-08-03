from sqlalchemy.orm import Session
from app.database.models import Voo as VooDB, Passageiro as PassageiroDB, Funcionario as FuncionarioDB, MiniAeronave as AeronaveDB
from app.services.mappers.voo_mapper import voo_from_db
from app.services.mappers.passageiro_mapper import passageiro_from_db
from app.services.mappers.funcionario_mapper import funcionario_from_db

#Expor Função no método POST
class VooService:
    def __init__(self, db: Session):
        self.db = db
    def criar_voo(self, numero_voo: str, origem: str, destino: str, aeronave_id: int):
        aeronave = self.db.query(AeronaveDB).filter_by(id=aeronave_id).first()
        if not aeronave:
            raise ValueError("Aeronave não encontrada.")

        voo_db = VooDB(
            numero_voo=numero_voo,
            origem=origem,
            destino=destino,
            aeronave_id=aeronave.id
        )
        self.db.add(voo_db)
        self.db.commit()
        self.db.refresh(voo_db)

        return voo_from_db(voo_db)

    def buscar_voo(self, numero_voo: str):
        voo_db = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if voo_db:
            return voo_from_db(voo_db)
        return None

    #Expor função no método GET
    def listar_todos_voos(self):
        voos_db = self.db.query(VooDB).all()
        return [voo_from_db(v) for v in voos_db]


    def adicionar_passageiro_ao_voo(self, numero_voo: str, nome: str, cpf: str):
        voo_db = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if not voo_db:
            raise ValueError("Voo não encontrado.")

        passageiro_db = self.db.query(PassageiroDB).filter_by(cpf=cpf).first()
        if not passageiro_db:
            passageiro_db = PassageiroDB(nome=nome, cpf=cpf)
            self.db.add(passageiro_db)
            self.db.commit()
            self.db.refresh(passageiro_db)

        if passageiro_db not in voo_db.passageiros:
            voo_db.passageiros.append(passageiro_db)
            self.db.commit()

        return voo_from_db(voo_db, self.db)


    def adicionar_tripulante_ao_voo(self, numero_voo: str, funcionario_db: FuncionarioDB):
        voo_db = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if not voo_db:
            raise ValueError("Voo não encontrado.")
        if funcionario_db in voo_db.tripulacao:
            raise ValueError("Tripulante já está na tripulação.")

        voo_db.tripulacao.append(funcionario_db)
        self.db.commit()
        self.db.refresh(voo_db)

        return voo_from_db(voo_db)
    def adicionar_passageiro_ao_voo(self, numero_voo: str, passageiro_db: PassageiroDB):
        voo_db = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if not voo_db:
            raise ValueError("Voo não encontrado.")
        if passageiro_db in voo_db.passageiros:
            raise ValueError("Passageiro já está na tripulação.")

        voo_db.tripulacao.append(passageiro_db)
        self.db.commit()
        self.db.refresh(voo_db)

        return voo_from_db(voo_db)
    def listar_passageiros_por_voo(self, numero_voo: str):
        voos = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if not voos:
            raise ValueError("Voo não encontrado.")

        return [passageiro_from_db(passageiro) for passageiro in voos.passageiros]

    def listar_funcionarios_por_voo(self, numero_voo: str):
        voos = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if not voos:
            raise ValueError("Voo não encontrado.")
        
        return [funcionario_from_db(funcionario) for funcionario in voos.tripulacao]
    
    def deletar_voo(self, numero_voo: str):
        voo = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if not voo:
            raise ValueError("Voo não encontrado.")

        self.db.delete(voo)
        self.db.commit()