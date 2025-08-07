# Lógica de negócio de auditoria
from app.models.auditor import Auditor
from app.database.crud import buscar_voo
from app.database.session import SessionLocal
from app.services.relatorio_service import RelatorioService

def executar_auditoria(numero_voo: str): #GET /auditoria/{numero_voo}/
    db = SessionLocal() 
    try:
        RelatorioService(db).gerar_pdf_por_numero_voo(numero_voo)
    finally:
        db.close()