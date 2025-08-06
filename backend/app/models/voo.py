#Voo, Miniaeronave, Companhia Aérea
from app.models.pessoa import Passageiro

class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int, voos=None):
        self.modelo = modelo 
        self.capacidade = capacidade 
        self.voos = voos or []

    def __eq__(self, other):
        if not isinstance(other, MiniAeronave):
            return NotImplemented
        return (self.modelo == other.modelo) and (self.capacidade == other.capacidade)

    def __lt__(self, other):
        if not isinstance(other, MiniAeronave):
            return NotImplemented
        return self.capacidade < other.capacidade
    
    def resumo_voo(self):
        return f"{self.modelo} com capacidade para {self.capacidade} passageiros. "

class Voo:
    def __init__(self, numero_voo, origem, destino, aeronave_id):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.aeronave = aeronave
        self.passageiros = []
        self.funcionarios = []


    def __eq__(self, other):
        if not isinstance(other, Voo):
            return NotImplemented
        return self.numero_voo == other.numero_voo
    
    def __lt__(self, other):
        if not isinstance(other, Voo):
            return NotImplemented
        return len(self.passageiros) < len(other.passageiros)

    def adicionar_passageiro(self, passageiro):
        if len(self.passageiros) >= self.aeronave.capacidade:
            return
        if passageiro not in self.passageiros:
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
    def __init__(self, nome: str, voos=None):
        nome = nome.strip()
        
        if len(nome) < 3:
            raise ValueError("o nome da companhia deve ter pelo menos 3 letras.")
        
        self._nome = nome
        self._voos = voos or []
    
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


