from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.passageiro_service import buscar_passageiro_por_cpf, listar_passageiros, criar_passageiro
from app.database.session import get_db
from app.models.pessoa import Passageiro

router = APIRouter(prefix="/passageiros", tags=["Passageiros"])

@router.post("/", response_model=Passageiro, status_code=201)
def criar_passageiro(nome: str, cpf: str, db: Session = Depends(get_db)):
    try:
        return criar_passageiro(db, nome, cpf)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list(Passageiro))
def listar_passageiros(db: Session = Depends(get_db)):
    return listar_passageiros(db)

@router.get("/{cpf}", response_model=Passageiro)
def buscar_passageiro_por_cpf(cpf: str, db: Session = Depends(get_db)):
    passageiro = buscar_passageiro_por_cpf(db, cpf)
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    return passageiro