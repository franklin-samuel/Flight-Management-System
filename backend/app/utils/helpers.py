# scripts/gerar_relatorio_manual.py

from app.database.session import SessionLocal
from app.services.relatorio_service import gerar_relatorio_pdf
from app.database.models import Voo

def main():
    db = SessionLocal()
    try:
        print("[LOG] Consultando voos no banco de dados...")
        voos = db.query(Voo).all()

        # Força o carregamento das relações (evita problemas fora da sessão)
        for voo in voos:
            _ = voo.companhia
            _ = voo.aeronave
            _ = voo.tripulacao
            _ = voo.passageiros
            for p in voo.passageiros:
                _ = p.bagagens

        print("[LOG] Gerando PDF...")
        buffer = gerar_relatorio_pdf(voos)

        caminho_arquivo = r"D:\Samuel Franklin\Programação\Python\PROJETOS\Flight-Management-System\backend\reports\voos.pdf"
        with open(caminho_arquivo, "wb") as f:
            f.write(buffer.getvalue())

        print(f"[LOG] Relatório salvo em: {caminho_arquivo}")
    except Exception as e:
        print(f"[LOG] Erro ao gerar relatório: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
