#Voo, Miniaeronave, Companhia Aérea

class Voo:
    def __init__(self, numero_voo, origem, destino, aeronave):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.aeronave = aeronave
        self.passageiros = {}
        self.tripulação = {}
        # implementar database nas listas 

    def adicionar_passageiro(self, passageiro, numero_voo):

