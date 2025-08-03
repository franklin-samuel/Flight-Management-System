from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.voo_service import VooService
from app.services.funcionario_service import FuncionarioService
from app.services.passageiro_service import PassageiroService
from app.database.session import get_db
from app.models.voo import Voo
from pydantic import BaseModel

router = APIRouter(prefix="/voos")

class VooCreate(BaseModel):
    numero_voo: str
    origem: str
    destino: str
    aeronave_id: int

@router.post("", response_model=Voo, status_code=201)
def criar(dados_voo: VooCreate, db: Session = Depends(get_db)):
    service = VooService(db)
    try:
        return service.criar_voo(
            numero_voo=dados_voo["numero_voo"],
            origem=dados_voo["origem"],
            destino=dados_voo["destino"],
            aeronave_id=dados_voo["aeronave_id"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[Voo])
def listar(db: Session = Depends(get_db)):
    service = VooService(db)
    return service.listar_todos_voos()

@router.get("/{numero_voo}", response_model=Voo)
def buscar(numero_voo: str, db: Session = Depends(get_db)):
    service = VooService(db)
    voo = service.buscar_voo( numero_voo)
    if not voo:
        raise HTTPException(status_code=404, detail="Voo não encontrado")
    return voo

@router.post("/{numero_voo}/{matricula}")
def adicionar_tripulante(numero_voo: str, matricula: str, db: Session = Depends(get_db)):
    service = VooService(db)
    fservice = FuncionarioService(db)
    funcionario = fservice.buscar_funcionario_por_matricula(matricula)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    try:
        return service.adicionar_tripulante_ao_voo(numero_voo, funcionario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{numero_voo}/{cpf}")
def adicionar_passageiro(numero_voo: str, cpf: str, db: Session = Depends(get_db)):
    service = VooService(db)
    pservice = PassageiroService(db)
    passageiro = pservice.buscar_passageiro_por_cpf(cpf)
    if not passageiro:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    try:
        return service.adicionar_passageiro_ao_voo(numero_voo, passageiro)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{numero_voo}/tripulacao")
def listar_tripulacao(numero_voo: str, db: Session = Depends(get_db)):
    service = VooService(db)
    tripulacao = service.listar_funcionarios_por_voo(numero_voo)
    if not tripulacao:
        raise HTTPException(status_code=404, detail="Tripulacao não encontrada")
    return tripulacao

@router.get("/{numero_voo}/passageiros")
def listar_passageiros(numero_voo: str, db: Session = Depends(get_db)):
    service = VooService(db)
    passageiros = service.listar_passageiros_por_voo(numero_voo)
    if not passageiros:
        raise HTTPException(status_code=404, detail="Passageiros não encontrados")
    return passageiros

@router.get("/{numero_voo}/{cpf}/bagagens")
def listar_bagagens(numero_voo: str, cpf: str, db: Session = Depends(get_db)):
    service = PassageiroService(db)
    bagagens = service.listar_bagagem_por_passageiro(cpf)
    if not bagagens:
        raise HTTPException(status_code=404, detail="Bagagens não encontradas")
    return bagagens