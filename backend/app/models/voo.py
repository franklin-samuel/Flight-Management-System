#Voo, Miniaeronave, Companhia Aérea
from app.database.models import Voo as VooDB
from app.database.models import Passageiro, Funcionario
            
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo 
        self.capacidade = capacidade 
    
    def resumo_voo(self):
        return f"{self.modelo} com capacidade para {self.capacidade} passageiros. "

class Voo:
    def __init__(self, voo_db):
        self._db = voo_db
        self.numero_voo = voo_db.numero_voo
        self.origem = voo_db.origem
        self.destino = voo_db.destino
        self.aeronave = MiniAeronave(voo_db.aeronave.modelo, voo_db.aeronave.capacidade)
        self.passageiros = [Passageiro(p.nome, p.cpf) for p in voo_db.passageiros]
        self.tripulacao = [Funcionario(f.cargo, f.matricula, f.nome, f.cpf) for f in voo_db.tripulacao]

        # implementar database nas listas 

    def adicionar_passageiro(self, passageiro):
        if len(self.passageiros) >= self.aeronave.capacidade:
            return
        if any(p.cpf == passageiro.cpf for p in self.passageiros):
            return
        self.passageiros.append(passageiro)

    def adicionar_tripulante(self, tripulante):
        self.tripulação.append(tripulante)

    def listar_passageiros(self):
        for passageiro in self.passageiros:
            print(passageiro)
    
    def listar_tripulantes(self):
        for tripulante in self.tripulação:
            print(tripulante)    

class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        nome = nome.strip()
        
        if len(nome) < 3:
            raise ValueError("o nome da companhia deve ter pelo menos 3 letras.")
        
        self._nome = nome
        self._voos = []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        novo_nome = novo_nome.strip()

        if len(novo_nome) < 3:
            raise ValueError ("o nome da companhia deve ter pelo menos 3 letras.")
        
        self._nome = novo_nome
       
    def adicionar_voo(self, voo):
        self._voos.append(voo)
        
    def buscar_voo(self, numero: str):
        for voo in self._voos:
            if voo.numero_voo == numero:
                return voo
        return None
        
    def listar_voos(self):
        for voo in self._voos:
            print(voo)


