import os
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from sqlalchemy.orm import Session

from app.database.models import Voo as VooDB
from app.services.mappers.voo_mapper import voo_from_db

class RelatorioService:
    def __init__(self, db: Session):
        self.db = db

    def gerar_pdf_por_numero_voo(self, numero_voo: str) -> BytesIO:
        # Buscar voo no banco de dados
        voo_db = self.db.query(VooDB).filter_by(numero_voo=numero_voo).first()
        if not voo_db:
            raise ValueError(f"Voo '{numero_voo}' não encontrado.")

        # Mapear para objeto de domínio
        voo = voo_from_db(voo_db)

        print(f"[LOG] Gerando relatório para voo {voo.numero_voo}...")

        # Criar PDF em memória
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer)
        elementos = []
        estilo = getSampleStyleSheet()

        # Informações do voo
        elementos.append(Paragraph(f"Voo: {voo.numero_voo}", estilo["Heading2"]))
        elementos.append(Paragraph(f"Origem: {voo.origem} - Destino: {voo.destino}", estilo["Normal"]))
        elementos.append(Paragraph(
            f"Aeronave: {voo.aeronave.modelo} (Capacidade: {voo.aeronave.capacidade})",
            estilo["Normal"]
        ))

        # Passageiros
        elementos.append(Paragraph("Passageiros:", estilo["Heading4"]))
        if voo.passageiros:
            for passageiro in voo.passageiros:
                elementos.append(Paragraph(
                    f" - {passageiro.nome} | CPF: {passageiro._cpf}",
                    estilo["Normal"]
                ))
                for bagagem in getattr(passageiro, "bagagens", []):
                    elementos.append(Paragraph(
                        f"    • Bagagem: {bagagem.descricao or 'Sem descrição'} ({bagagem.peso} kg)",
                        estilo["Normal"]
                    ))
        else:
            elementos.append(Paragraph(" - Nenhum passageiro registrado.", estilo["Normal"]))

        # Tripulação
        elementos.append(Paragraph("Tripulação:", estilo["Heading4"]))
        if voo.tripulacao:
            for f in voo.tripulacao:
                elementos.append(Paragraph(
                    f" - {f.cargo}: {f.nome} ({getattr(f, 'matricula', 'N/A')})",
                    estilo["Normal"]
                ))
        else:
            elementos.append(Paragraph(" - Tripulação não registrada.", estilo["Normal"]))

        # Status
        completo = bool(voo.passageiros) and bool(voo.tripulacao)
        status = "COMPLETO" if completo else "INCOMPLETO"
        elementos.append(Spacer(1, 10))
        elementos.append(Paragraph(f"<b>Status do Voo:</b> {status}", estilo["Normal"]))
        elementos.append(Spacer(1, 20))

        # Construir PDF
        doc.build(elementos)
        buffer.seek(0)
        print(f"[LOG] Relatório gerado em memória com sucesso para voo {voo.numero_voo}.")

        # Salvar em disco
        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        file_path = os.path.join(reports_dir, f"relatorio_{voo.numero_voo}.pdf")
        with open(file_path, "wb") as f:
            f.write(buffer.getvalue())

        print(f"[LOG] Relatório salvo em disco: {file_path}")

        return buffer
