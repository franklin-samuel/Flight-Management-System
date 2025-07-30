# Classes Abstratas com ABC, Logavel
from abc import ABC, abstractmethod

class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        print(f"Usuario {self.nome} fez login")
