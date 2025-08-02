from app.models.pessoa import Passageiro
from app.database.models import Passageiro as PassageiroDB

def passageiro_from_db(passageiro_db: PassageiroDB) -> Passageiro:
    return Passageiro(
        nome=passageiro_db.nome,
        cpf=passageiro_db.cpf
    )