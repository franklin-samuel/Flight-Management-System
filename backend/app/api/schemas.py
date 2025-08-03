from pydantic import BaseModel
from typing import Optional

class VooBase(BaseModel):
    numero_voo: str
    origem: str
    destino: str
    aeronave_id: int

class VooCreate(VooBase):
    pass

class VooRead(VooBase):
    pass

    model_config = {
        "from_attributes": True
    }

class FuncionarioRead(BaseModel):
    nome: str
    matricula: str

    model_config = {
        "from_attributes": True
    }

class PassageiroRead(BaseModel):
    nome: str
    cpf: str

    model_config = {
        "from_attributes": True
    }

class BagagemRead(BaseModel):
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
    pass

    model_config = {
        "from_attributes": True
    }

class AeronaveBase(BaseModel):
    modelo: str
    capacidade: int

class AeronaveCreate(AeronaveBase):
    pass

class AeronaveRead(AeronaveBase):
    pass
    
    model_config = {
        "from_attributes": True
    }