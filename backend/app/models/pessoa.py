from app.models.mixins import IdentificavelMixin
from app.models.interfaces import Logavel
from app.models.bagagem import Bagagem
from app.database.models import Passageiro as PassageiroDB

class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str, **kwargs):
        self._nome = nome
        self._cpf = cpf
       
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
        
    def __str__(self):
        return f"{self._nome} ({self._cpf})"
    

class Passageiro(Pessoa):
    def __init__(self, nome: str, cpf: str, db_session=None):
        super().__init__(nome, cpf)
        self.bagagens = []
        self._db_session = db_session

    def adicionar_bagagem(self, bagagem: Bagagem):
        self.bagagens.append(bagagem)
        if self._db_session:
            passageiro_db = self._db_session.query(PassageiroDB).filter_by(cpf=self.cpf).first()
            if passageiro_db:
                nova_bagagem_db = bagagem.to_db_model()
                nova_bagagem_db.dono = passageiro_db
                self._db_session.add(nova_bagagem_db)
                self._db_session.commit()

        
    def listar_bagagens(self):
        for bagagem in self.bagagens:
            print(bagagem)

class Funcionario(Pessoa, IdentificavelMixin, Logavel):
    def __init__(self, cargo: str, matricula: str, nome: str, cpf: str):
        super().__init__(nome=nome, cpf=cpf)
        self.cargo = cargo
        self.matricula = matricula

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Matrícula: {self.matricula}")
        print(f"ID: {self.get_id()}")

    def logar_entrada(self):
        print(f"Funcionário {self.nome} (matrícula: {self.matricula}) logou no sistema.")
    

        
