from app.models.mixins import IdentificavelMixin
from app.models.interfaces import Logavel
from app.models.bagagem import Bagagem

class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str, **kwargs):
        self._nome = nome
        self._cpf = cpf
       
    @property
    def nome(self):
        return self._nome
        
    def __str__(self):
        return f"{self._nome} ({self._cpf})"
    

class Passageiro(Pessoa):
    def __init__(self, nome: str, cpf: str, bagagens=None):
        super().__init__(nome, cpf)
        self.bagagens = bagagens or []

    def adicionar_bagagem(self, bagagem: Bagagem):
        self.bagagens.append(bagagem)
        
    def listar_bagagens(self):
        bagagens = []
        for bagagem in self.bagagens:
            bagagens.append(bagagem)
            return bagagens

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
    

        
