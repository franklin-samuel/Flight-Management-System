# Classe auditor
from mixins import AuditavelMixin
from interfaces import Logavel

class Auditor(AuditavelMixin, Logavel):
    def __init__(self, nome: str):
        super().__init__()
        self.nome = nome
    
    def logar_entrada(self):
        print(f'Auditor {self.nome} fez login no sistema')
    
    def auditar_voo(voo):
        if voo.passageiros <= voo.capacidade and voo.passageiros >= 1:
            print("Relatorio deve ser feito aqui")
        
    def __str__(self):
        return str(f"Auditor: {self.nome} com ID: {self.id}")
    

