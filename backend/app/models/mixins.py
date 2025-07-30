# Identificável Mixin, Auditavel Mixin
import uuid

class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self, **kwargs):
        # TODO: gerar e armazenar um ID (use uuid.uuid4())
        self.id = uuid.uuid4()
    def get_id(self):
        # TODO: retornar o ID
        return self.id