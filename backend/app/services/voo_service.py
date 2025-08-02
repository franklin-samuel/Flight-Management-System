from sqlalchemy.orm import Session
from app.database.models import Voo as VooDB, Passageiro as PassageiroDB, Funcionario as FuncionarioDB, AeronaveDB
from app.models.voo import Voo
from app.models.pessoa import Passageiro, Funcionario

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

    return Voo(voo_db)
def buscar_voo(db: Session, numero_voo: str):
    voo_db = db.query(VooDB).filter_by(numero_voo=numero_voo).first()
    if voo_db:
        return Voo(voo_db, db)
    return None
#Expor função no método GET
def listar_todos_voos(db: Session):
    voos_db = db.query(VooDB).all()
    voos = []
    for v in voos_db:
        voo = Voo(v, db)
        voos.append(voo)
    return voos

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

    voo = Voo(voo_db, db)
    passageiro_poo = Passageiro(nome=nome, cpf=cpf, db_session=db)
    voo.adicionar_passageiro(passageiro_poo)

    return voo

def buscar_passageiro_por_cpf(db: Session, cpf: str):
    passageiro_db = db.query(PassageiroDB).filter_by(cpf=cpf).first()
    if not passageiro_db:
        raise ValueError("Passageiro não encontrado.")

    passageiro_poo = Passageiro(passageiro_db.nome, passageiro_db.cpf, db_session=db)
    return passageiro_poo

def adicionar_tripulante_ao_voo(db: Session, numero_voo: str, nome: str, cpf: str, cargo: str, matricula: str):
    voo_db = db.query(VooDB).filter_by(numero_voo=numero_voo).first()
    if not voo_db:
        raise ValueError("Voo não encontrado.")

    funcionario_db = db.query(FuncionarioDB).filter_by(cpf=cpf).first()
    if not funcionario_db:
        funcionario_db = FuncionarioDB(nome=nome, cpf=cpf, cargo=cargo, matricula=matricula)
        db.add(funcionario_db)
        db.commit()
        db.refresh(funcionario_db)

    if funcionario_db in voo_db.tripulacao:
        raise ValueError("Tripulante já está na tripulação.")

    voo_db.tripulacao.append(funcionario_db)
    db.commit()
    db.refresh(voo_db)

    voo = Voo(voo_db, db)
    tripulante_poo = Funcionario(cargo=cargo, matricula=matricula, nome=nome, cpf=cpf)
    voo.adicionar_tripulante(tripulante_poo)

    return voo