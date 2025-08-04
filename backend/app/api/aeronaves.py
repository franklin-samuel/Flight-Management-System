from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.aeronave_services import AeronaveService
from app.database.session import get_db
from app.api.schemas import AeronaveCreate, AeronaveRead, VooRead

router = APIRouter(prefix="/aeronaves", tags=["Aeronaves"])

@router.post("", response_model = AeronaveRead)
def criar(dados_aeronave: AeronaveCreate, db: Session = Depends(get_db)):
    service = AeronaveService(db)
    try:
        return service.criar_aeronave(
            modelo = dados_aeronave.modelo,
            capacidade = dados_aeronave.capacidade
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[AeronaveRead])
def listar(db: Session = Depends(get_db)):
    service = AeronaveService(db)
    return service.listar_aeronaves

@router.get("{modelo}", response_model=AeronaveRead)
def buscar(modelo: str, db: Session = Depends(get_db)):
    service = AeronaveService(db)
    aeronave = service.buscar_aeronave(modelo)
    if not aeronave:
        raise HTTPException(status_code=404, detail="Aeronave não encontrada")
    return aeronave

@router.delete("{modelo}", status_code=status.HTTP_204_NO_CONTENT)
def deletar(modelo: str, db: Session = Depends(get_db)):
    service = AeronaveService(db)
    try:
        service.deletar_aeronave(modelo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("{modelo}/voos", response_model=list[AeronaveRead])
def listar_voos_da_aeronave(modelo: str, db: Session = Depends(get_db)):
    service = AeronaveService(db)
    passageiros = service.listar_voos_da_aeronave(modelo)
    if not passageiros:
        raise HTTPException(status_code=404, detail="Voos não encontrados")
    return passageiros