import pytest
import logging
from sistema_voos import (
    criar_companhias_e_voos,
    listar_companhias,
    criar_passageiro,
    criar_funcionario,
    adicionar_bagagem,
    listar_passageiros_do_voo,
    auditar_voo
)
import sistema_voos
# Ativa logs para pytest
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FakeObj:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def test_criar_passageiro():
    logger.info("🧪 Testando criação de passageiro...")

    class FakePassageiroService:
        def criar_passageiro(self, nome, cpf):
            return FakeObj(nome=nome)

    service = FakePassageiroService()
    msg = criar_passageiro(service, "João", "12345678900")

    logger.info(f"Resultado: {msg}")
    assert msg == "Passageiro João cadastrado com sucesso!"


def test_criar_funcionario():
    logger.info("🧪 Testando criação de funcionário...")

    class FakeFuncionarioService:
        def criar_funcionario(self, nome, matricula, cargo, cpf):
            return FakeObj(nome=nome)

    service = FakeFuncionarioService()
    msg = criar_funcionario(service, "Maria", "2023001", "Piloto", "98765432100")

    logger.info(f"Resultado: {msg}")
    assert msg == "Funcionário Maria cadastrado com sucesso!"


def test_adicionar_bagagem():
    logger.info("🧪 Testando adição de bagagem...")

    class FakePassageiroService:
        def adicionar_bagagem(self, cpf, descricao, peso):
            logger.info(f"Bagagem registrada para CPF: {cpf}, Peso: {peso}kg")

    service = FakePassageiroService()
    msg = adicionar_bagagem(service, "123", "Mochila", 8.5)

    logger.info(f"Resultado: {msg}")
    assert msg == "Bagagem adicionada com sucesso."


def test_listar_companhias():
    logger.info("🧪 Testando listagem de companhias...")

    class FakeCompanhiaService:
        def listar_todas_companhias(self):
            return [
                FakeObj(id=1, nome="Azul"),
                FakeObj(id=2, nome="Gol"),
            ]

    service = FakeCompanhiaService()
    resultado = listar_companhias(service)

    logger.info(f"Resultado: {resultado}")
    assert resultado == [
        "ID: 1 | Nome: Azul",
        "ID: 2 | Nome: Gol"
    ]


def test_listar_passageiros_do_voo():
    logger.info("🧪 Testando listagem de passageiros do voo...")

    class FakeVooService:
        def listar_passageiros_por_voo(self, numero_voo):
            return [
                FakeObj(nome="João", cpf="123"),
                FakeObj(nome="Maria", cpf="456"),
            ]

    service = FakeVooService()
    resultado = listar_passageiros_do_voo(service, "AZ123")

    logger.info(f"Resultado: {resultado}")
    assert resultado == [
        "- João (123)",
        "- Maria (456)"
    ]


def test_auditar_voo(monkeypatch):
    logger.info("🧪 Testando auditoria de voo...")

    chamado = {}

    def fake_executar_auditoria(numero_voo):
        logger.info(f"Auditoria executada para o voo {numero_voo}")
        print('SOU EEXECUTADO')
        chamado['numero_voo'] = numero_voo


    monkeypatch.setattr(sistema_voos, "executar_auditoria", fake_executar_auditoria)
    msg = sistema_voos.auditar_voo("AZ123")

    logger.info(f"Resultado: {msg}")
    assert msg == "Auditoria concluída."
    assert chamado['numero_voo'] == "AZ123"


def test_criar_companhias_e_voos():
    logger.info("🧪 Testando criação de companhias e voos...")

    class FakeCompanhiaService:
        def criar_companhia(self, nome):
            logger.info(f"Companhia criada: {nome}")
            return FakeObj(nome=nome)

    class FakeAeronaveService:
        def __init__(self):
            self.id_counter = 1

        def criar_aeronave(self, modelo, capacidade):
            logger.info(f"Aeronave criada: {modelo}, capacidade: {capacidade}")
            aeronave = FakeObj(id=self.id_counter)
            self.id_counter += 1
            return aeronave

    class FakeVooService:
        def __init__(self):
            self.voos = []

        def criar_voo(self, codigo, origem, destino, aeronave_id):
            logger.info(f"Voo criado: {codigo} - {origem} -> {destino} (Aeronave ID: {aeronave_id})")
            self.voos.append((codigo, origem, destino, aeronave_id))

    companhia_service = FakeCompanhiaService()
    aeronave_service = FakeAeronaveService()
    voo_service = FakeVooService()

    msg = criar_companhias_e_voos(companhia_service, aeronave_service, voo_service)

    logger.info(f"Resultado: {msg}")
    assert msg == "Companhias, aeronaves e voos criados com sucesso."
    assert len(voo_service.voos) == 4
