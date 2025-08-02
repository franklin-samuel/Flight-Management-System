from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.funcionario_service import criar_funcionario, listar_funcionarios, buscar_funcionario_por_matricula, deletar_funcionario
from app.models.pessoa import Funcionario

router = APIRouter()

@router.get("/", response_model=list[Funcionario])
def listar_funcionarios(db: Session = Depends(get_db)):
    return listar_funcionarios(db)

@router.post("/", response_model=Funcionario, status_code=201)
def criar_funcionario(nome: str, matricula: str, db: Session = Depends(get_db)):
    try:
        return criar_funcionario(db, nome, matricula)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=Funcionario)
def buscar_funcionario(matricula: str, db: Session = Depends(get_db)):
    passageiro = buscar_funcionario(db, matricula)
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    return passageiro

@router.delete("/{id}", status_code=204)
def deletar_funcionario(id: int, db: Session = Depends(get_db)):
    sucesso = deletar_funcionario(id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")