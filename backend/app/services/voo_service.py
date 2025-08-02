from sqlalchemy.orm import Session
from app.database.models import Voo as VooDB, Passageiro as PassageiroDB, Funcionario as FuncionarioDB, AeronaveDB
from app.models.pessoa import Passageiro, Funcionario
from app.services.mappers.voo_mapper import voo_from_db
import uuid

#Expor Função no método POST
def criar_voo(db: Session, numero_voo: str, origem: str, destino: str, aeronave_id: int):
    aeronave = db.query(AeronaveDB).filter_by(id=aeronave_id).first()
    if not aeronave:
        raise ValueError("Aeronave não encontrada.")

    voo_db = VooDB(
        numero_voo=numero_voo,
        origem=origem,
        destino=destino,
        aeronave_id=aeronave.id
    )
    db.add(voo_db)
    db.commit()
    db.refresh(voo_db)

    return voo_from_db(voo_db)
def buscar_voo(db: Session, numero_voo: str):
    voo_db = db.query(VooDB).filter_by(numero_voo=numero_voo).first()
    if voo_db:
        return voo_from_db(voo_db)
    return None
#Expor função no método GET
def listar_todos_voos(db: Session):
    voos_db = db.query(VooDB).all()
    return [voo_from_db(v) for v in voos_db]


def adicionar_passageiro_ao_voo(db: Session, numero_voo: str, nome: str, cpf: str):
    voo_db = db.query(VooDB).filter_by(numero_voo=numero_voo).first()
    if not voo_db:
        raise ValueError("Voo não encontrado.")

    passageiro_db = db.query(PassageiroDB).filter_by(cpf=cpf).first()
    if not passageiro_db:
        passageiro_db = PassageiroDB(nome=nome, cpf=cpf)
        db.add(passageiro_db)
        db.commit()
        db.refresh(passageiro_db)

    if passageiro_db not in voo_db.passageiros:
        voo_db.passageiros.append(passageiro_db)
        db.commit()

    return voo_from_db(voo_db, db)


def adicionar_tripulante_ao_voo(db: Session, numero_voo: str, funcionario_db: FuncionarioDB):
    voo_db = db.query(VooDB).filter_by(numero_voo=numero_voo).first()
    if not voo_db:
        raise ValueError("Voo não encontrado.")
    if funcionario_db in voo_db.tripulacao:
        raise ValueError("Tripulante já está na tripulação.")

    voo_db.tripulacao.append(funcionario_db)
    db.commit()
    db.refresh(voo_db)

    voo_db.tripulacao.append(funcionario_db)
    db.commit()
    db.refresh(voo_db)

    return voo_from_db(voo_db)
