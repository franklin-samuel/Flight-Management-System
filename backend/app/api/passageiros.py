from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.passageiro_service import PassageiroService
from app.database.session import get_db
from app.api.schemas import PassageiroRead, BagagemRead

router = APIRouter(prefix="/passageiros", tags=["Passageiros"])

@router.post("/", response_model=PassageiroRead, status_code=201)
def criar_passageiro(nome: str, cpf: str, db: Session = Depends(get_db)):
    service = PassageiroService(db)
    try:
        return service.criar_passageiro(nome, cpf)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[PassageiroRead])
def listar_passageiros(db: Session = Depends(get_db)):
    service = PassageiroService(db)
    return service.listar_passageiros()

@router.get("/{cpf}", response_model=PassageiroRead)
def buscar_passageiro_por_cpf(cpf: str, db: Session = Depends(get_db)):
    service = PassageiroService(db)
    passageiro = service.buscar_passageiro_por_cpf(cpf)
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    return passageiro

@router.delete("/{cpf}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_passageiro(cpf: str, db: Session = Depends(get_db)):
    service = PassageiroService(db)
    try:
        service.deletar_passageiro(cpf)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{cpf}/bagagem)", response_model=BagagemRead)
def adicionar_bagagem_ao_passageiro(cpf: str, descricao: str, peso: float, db: Session = Depends(get_db)):
    service = PassageiroService(db)
    try:
        return service.adicionar_bagagem(cpf, descricao, peso)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{cpf}/{id_bagagem})", status_code=status.HTTP_204_NO_CONTENT)
def deletar_bagagem_do_passageiro(cpf: str, id_bagagem: int, db: Session = Depends(get_db)):
    service = PassageiroService(db)
    try:
        service.deletar_bagagem(cpf, id_bagagem)
        return {"mensagem": "Funcionario removido do voo com sucesso."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))