from fastapi import APIRouter, Depends, HTTPException
from app.database.session import SessionLocal
from app.services.voo_service import criar_voo, buscar_voo, listar_todos_voos, adicionar_tripulante_ao_voo
from app.services.funcionario_service import buscar_funcionario
from app.database.session import get_db

router = APIRouter(prefix="/voos")

