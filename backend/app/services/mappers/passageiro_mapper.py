from app.models.pessoa import Passageiro
from app.models.pessoa import Bagagem
from app.database.models import Passageiro as PassageiroDB
from app.database.models import Bagagem as BagagemDB

def passageiro_from_db(passageiro_db: PassageiroDB) -> Passageiro:
    return Passageiro(
        nome=passageiro_db.nome,
        cpf=passageiro_db.cpf
    )

def bagagem_from_db(bagagem_db: BagagemDB) -> Bagagem:
    return Bagagem(
        descricao=bagagem_db.descricao,
        peso=bagagem_db.peso
    )