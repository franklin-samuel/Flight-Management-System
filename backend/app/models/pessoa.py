# Pessoa, Passageiro, Funcionario

class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf
       
    @property
    def nome(self):
        return self._nome
        
    def __str__(self):
        return f"{self._nome} ({self._cpf})"
    
    
class Bagagem:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso  # kg

    def __str__(self):
        return f"{self.descricao} - {self.peso} kg"

    

class Passageiro(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
        self.bagagens = []

    def adicionar_bagagem(self, bagagem: Bagagem):
        self.bagagens.append(bagagem)
        
    def listar_bagagens(self):
        for bagagem in self.bagagens():
            print(bagagem)
        
        
