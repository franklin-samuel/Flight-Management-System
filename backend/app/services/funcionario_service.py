from sqlalchemy.orm import Session
from app.database.models import Funcionario as FuncionarioDB
from app.services.mappers.funcionario_mapper import funcionario_from_db
class FuncionarioService:
    def __init__(self, db: Session):
        self.db = db
    def criar_funcionario(self, nome: str, matricula: str):
        funcionario_db = FuncionarioDB(nome=nome, matricula=matricula)
        self.db.add(funcionario_db)
        self.db.commit()
        self.db.refresh(funcionario_db)
        return funcionario_from_db(funcionario_db)

    def buscar_funcionario_por_matricula(self, matricula: str):
        funcionario_db = self.db.query(FuncionarioDB).filter_by(matricula=matricula).first()
        if not funcionario_db:
            return None
        return funcionario_from_db(funcionario_db)

    def listar_funcionarios(self):
        funcionarios_db = self.db.query(FuncionarioDB).all()
        return [funcionario_from_db(funcionario) for funcionario in funcionarios_db]

    def deletar_funcionario(self, id: int) -> bool:
        funcionario = self.db.query(FuncionarioDB).filter_by(id=id).first()
        if not funcionario:
            return False
        self.db.delete(funcionario)
        self.db.commit()
        return True