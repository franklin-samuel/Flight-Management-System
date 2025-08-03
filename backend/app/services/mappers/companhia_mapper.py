from app.database.models import CompanhiaAerea as CompanhiaDB
from app.models.voo import CompanhiaAerea

def companhia_from_db(db_model: CompanhiaDB) -> CompanhiaAerea:
    return CompanhiaAerea(
        nome=db_model.nome
    )