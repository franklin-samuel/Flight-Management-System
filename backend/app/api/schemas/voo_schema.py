from pydantic import BaseModel
from typing import List, Optional

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
