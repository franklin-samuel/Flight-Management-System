from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.companhia_service import CompanhiaService
from app.database.session import get_db
from app.api.schemas import CompanhiaCreate, CompanhiaRead, VooRead

router = APIRouter(prefix="/companhias")

@router.post("", response_model=CompanhiaRead, status_code=201)
def criar_companhia(dados: CompanhiaCreate, db: Session = Depends(get_db)):
    service = CompanhiaService(db)
    try:
        return service.criar_companhia(dados.nome)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[CompanhiaRead])
def listar_companhias(db: Session = Depends(get_db)):
    service = CompanhiaService(db)
    return service.listar_todas()

@router.get("/{companhia_id}", response_model=CompanhiaRead)
def buscar_companhia(companhia_id: int, db: Session = Depends(get_db)):
    service = CompanhiaService(db)
    companhia = service.buscar_por_id(companhia_id)
    if not companhia:
        raise HTTPException(status_code=404, detail="Companhia não encontrada")
    return companhia

@router.get("/{companhia_id}/voos", response_model=list[VooRead])
def listar_voos_da_companhia(companhia_id: int, db: Session = Depends(get_db)):
    service = CompanhiaService(db)
    voos = service.listar_voos_por_companhia(companhia_id)
    if voos is None:
        raise HTTPException(status_code=404, detail="Companhia não encontrada ou sem voos")
    return voos

@router.delete("/{companhia_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_companhia(companhia_id: int, db: Session = Depends(get_db)):
    service = CompanhiaService(db)
    try:
        service.deletar_companhia(companhia_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
