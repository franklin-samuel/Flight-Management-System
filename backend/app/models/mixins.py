# Identificável Mixin, Auditavel Mixin
import uuid

class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self, **kwargs):
        # TODO: gerar e armazenar um ID (use uuid.uuid4())
        self.id = str(uuid.uuid4())
    def get_id(self):
        # TODO: retornar o ID
        return self.id

class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        print(f"[LOG] {evento}")