from app.models.pessoa import Funcionario
from app.database.models import Funcionario as FuncionarioDB

def funcionario_from_db(funcionario_db: FuncionarioDB) -> Funcionario:
    return Funcionario(
        nome=funcionario_db.nome,
        matricula=funcionario_db.matricula
    )

def funcionario_to_db(funcionario: Funcionario) -> FuncionarioDB:
    return FuncionarioDB(nome=funcionario.nome, matricula=funcionario.matricula)