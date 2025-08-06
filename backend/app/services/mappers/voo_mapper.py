from app.database.models import Voo as VooDB, MiniAeronave as MiniAeronaveDB, Passageiro as PassageiroDB, Funcionario as FuncionarioDB
from app.models.voo import Voo
from app.models.voo import MiniAeronave
from app.models.pessoa import Passageiro
from app.api.schemas import VooCreate

def voo_from_db(voo_db: VooDB) -> Voo:
    voo = Voo(
        numero_voo=voo_db.numero_voo,
        origem=voo_db.origem,
        destino=voo_db.destino,
        aeronave=MiniAeronave( 
            modelo=voo_db.aeronave_id.modelo,
            capacidade=voo_db.aeronave_id.capacidade
        ),
    )
    for p in voo_db.passageiros:
        voo.adicionar_passageiro(Passageiro(nome=p.nome, cpf=p.cpf))
    for f in voo_db.tripulacao:
        voo.adicionar_funcionario(f.nome)
    return voo

def voo_to_db(voo: VooCreate, aeronave: MiniAeronaveDB) -> VooDB:
    voo_db = VooDB(
        numero_voo=voo.numero_voo,
        origem=voo.origem,
        destino=voo.destino,
        aeronave=aeronave,
        passageiros=[
            PassageiroDB(nome=p.nome, cpf=p.cpf) for p in voo.passageiros
        ],
        funcionarios=[
            FuncionarioDB(nome=f.nome, cpf=f.cpf, cargo=f.cargo, matricula=f.matricula)
            for f in voo.funcionarios
        ]
    )
    return voo_db

def voo_create_to_db(voo_data: VooCreate, aeronave_id) -> VooDB:
    return VooDB(
        numero_voo=voo_data.numero_voo,
        origem=voo_data.origem,
        destino=voo_data.destino,
        aeronave_id=aeronave_id
    )