from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.passageiro_service import buscar_passageiro_por_cpf
from app.services.funcionario_service import buscar_funcionario
from app.database.session import get_db