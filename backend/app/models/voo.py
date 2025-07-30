#Voo, Miniaeronave, Companhia Aérea

            
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo 
        self.capacidade = capacidade 
    
    def resumo_voo(self):
        return f"{self.modelo} com capacidade para {self.capacidade} passageiros. "

class Voo:
    def __init__(self, numero_voo, origem, destino, aeronave: MiniAeronave):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.aeronave = aeronave
        self.passageiros = []
        self.tripulação = []
        # implementar database nas listas 

    def adicionar_passageiro(self, passageiro, capacidade):
        if len(self.passageiros) >= capacidade:
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
            if voo.numero == numero:
                return voo
        return None
        
    def listar_voos(self):
        for voo in self._voos:
            print(voo)


