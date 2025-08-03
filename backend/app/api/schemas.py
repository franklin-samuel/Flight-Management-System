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
    id: int

    class Config:
        orm_mode = True

class FuncionarioRead(BaseModel):
    id: int
    nome: str
    matricula: str

    class Config:
        orm_mode = True

class PassageiroRead(BaseModel):
    id: int
    nome: str
    cpf: str

    class Config:
        orm_mode = True

class BagagemRead(BaseModel):
    id: int
    peso: float
    descricao: Optional[str]

    class Config:
        orm_mode = True

class CompanhiaBase(BaseModel):
    nome: str

class CompanhiaCreate(CompanhiaBase):
    pass

class CompanhiaRead(CompanhiaBase):
    id: int

    class Config:
        orm_mode = True

class AeronaveBase(BaseModel):
    modelo: str
    capacidade: int

class AeronaveCreate(AeronaveBase):
    pass

class AeronaveRead(AeronaveBase):
    id: int
    
    class Config:
        orm_mode = True