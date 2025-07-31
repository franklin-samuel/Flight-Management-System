# Lógica de negócio de auditoria
from app.models.auditor import Auditor
from app.database.crud import buscar_voo
from database.session import SessionLocal

def executar_auditoria(numero_voo: str):
    db = SessionLocal() 
    try:
        voo = buscar_voo(db, numero_voo)
        auditor = Auditor(nome="Demetrios")

        if voo:
            auditor.auditar_voo(voo)
        else:
            print("Voo nao encontrado")
    finally:
        db.close()