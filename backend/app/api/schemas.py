from pydantic import BaseModel
from typing import Optional
from enum import Enum
class VooBase(BaseModel):
    numero_voo: str
    origem: str
    destino: str
    aeronave_id: int

class VooCreate(VooBase):
    pass

class VooRead(VooBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class FuncionarioRead(BaseModel):
    id: str
    nome: str
    matricula: str

    model_config = {
        "from_attributes": True
    }

class VooNumero(BaseModel):
    numero_voo: str

class CargoEnum(str, Enum):
    PILOTO = "Piloto"
    COPILOTO = "Copiloto"
    COMISSARIO = "Comissário"

class FuncionarioCreate(BaseModel):
    nome: str
    cpf: str
    cargo: CargoEnum
    matricula: str

class PassageiroRead(BaseModel):
    id: int
    nome: str
    cpf: str

    model_config = {
        "from_attributes": True
    }

class BagagemRead(BaseModel):
    id: int
    peso: float
    descricao: Optional[str]

    model_config = {
        "from_attributes": True
    }

class CompanhiaBase(BaseModel):
    nome: str

class CompanhiaCreate(CompanhiaBase):
    pass

class CompanhiaRead(CompanhiaBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class AeronaveBase(BaseModel):
    modelo: str
    capacidade: int

class AeronaveCreate(AeronaveBase):
    pass

class AeronaveRead(AeronaveBase):
    id: int
    
    model_config = {
        "from_attributes": True
    }

