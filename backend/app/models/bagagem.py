class Bagagem:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso  # kg

    def __str__(self):
        return f"{self.descricao} - {self.peso} kg"