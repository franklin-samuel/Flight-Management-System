from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.funcionario_service import FuncionarioService
from app.api.schemas import FuncionarioRead

router = APIRouter(prefix="/tripulacao", tags=["Tripulacao"])

@router.get("/", response_model=list[FuncionarioRead])
def listar_funcionarios(db: Session = Depends(get_db)):
    service = FuncionarioService(db)
    return service.listar_funcionarios()

@router.post("/", response_model=FuncionarioRead, status_code=201)
def criar_funcionario(nome: str, matricula: str, db: Session = Depends(get_db)):
    service = FuncionarioService(db)
    try:
        return service.criar_funcionario(nome, matricula)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=FuncionarioRead)
def buscar_funcionario(matricula: str, db: Session = Depends(get_db)):
    service = FuncionarioService(db)
    passageiro = service.buscar_funcionario(matricula)
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    return passageiro

@router.delete("/{id}", status_code=204)
def deletar_funcionario(id: int, db: Session = Depends(get_db)):
    service = FuncionarioService(db)
    sucesso = service.deletar_funcionario(id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")