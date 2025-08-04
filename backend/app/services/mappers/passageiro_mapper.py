from app.models.pessoa import Passageiro
from app.models.pessoa import Bagagem
from app.database.models import Passageiro as PassageiroDB
from app.database.models import Bagagem as BagagemDB

def passageiro_from_db(passageiro_db: PassageiroDB) -> Passageiro:
    bagagens = [bagagem for bagagem in passageiro_db.bagagens]
    return Passageiro(
        nome=passageiro_db.nome,
        cpf=passageiro_db.cpf,
        bagagens=bagagens
    )

def bagagem_from_db(bagagem_db: BagagemDB) -> Bagagem:
    return Bagagem(
        descricao=bagagem_db.descricao,
        peso=bagagem_db.peso
    )

def passageiro_to_db(passageiro_db: Passageiro) -> PassageiroDB:
        return PassageiroDB(
        nome=passageiro_db.nome,
        cpf=passageiro_db.cpf,
        bagagens=[bagagem for bagagem in passageiro_db.bagagens]

    )

def bagagem_to_db(bagagem_db: Bagagem) -> BagagemDB:
    return BagagemDB(
        descricao=bagagem_db.descricao,
        peso=bagagem_db.peso
    )