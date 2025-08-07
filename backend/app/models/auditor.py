# Classe auditor
from app.models.mixins import AuditavelMixin
from app.models.interfaces import Logavel

class Auditor(AuditavelMixin, Logavel):
    def __init__(self, nome: str):
        super().__init__()
        self.nome = nome
    
    def logar_entrada(self):
        print(f'Auditor {self.nome} fez login no sistema')
    
    def auditar_voo(self, voo):
        if len(voo.passageiros) <= voo.aeronave.capacidade and len(voo.passageiros) >= 1:
            print("Relatorio deve ser feito aqui") # chamar uma função de gerar relatório
        
    def __str__(self):
        return str(f"Auditor: {self.nome} com ID: {self.id}")
    

