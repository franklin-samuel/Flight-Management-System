from app.database.models import Voo as VooDB
from app.models.voo import Voo
from app.models.voo import MiniAeronave
from app.models.pessoa import Passageiro
from app.models.voo import MiniAeronave
from app.database.models import Aeronave as AeronaveDB

def voo_from_db(voo_db: VooDB) -> Voo:
    voo = Voo(
        numero_voo=voo_db.numero_voo,
        origem=voo_db.origem,
        destino=voo_db.destino,
        aeronave=MiniAeronave(
            modelo=voo_db.aeronave.modelo,
            capacidade=voo_db.aeronave.capacidade
        )
    )
    for p in voo_db.passageiros:
        voo.adicionar_passageiro(Passageiro(nome=p.nome, cpf=p.cpf))
    for f in voo_db.funcionarios:
        voo.adicionar_funcionario(f.nome)
    return voo

def aeronave_from_db(aeronave_db: AeronaveDB) -> MiniAeronave:
    return MiniAeronave(
        modelo=aeronave_db.modelo,
        capacidade=aeronave_db.capacidade
    )