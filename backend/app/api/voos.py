from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.voo_service import criar_voo, buscar_voo, listar_todos_voos, adicionar_tripulante_ao_voo
from app.services.funcionario_service import buscar_funcionario
from app.database.session import get_db

router = APIRouter(prefix="/voos")

@router.post("")
def criar(dados_voo: dict, db: Session = Depends(get_db)):
    try:
        return criar_voo(
            db,
            numero_voo=dados_voo["numero_voo"],
            origem=dados_voo["origem"],
            destino=dados_voo["destino"],
            aeronave_id=dados_voo["aeronave_id"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


    