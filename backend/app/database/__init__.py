from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

tripulantes_voo = Table(
    'tripulantes_voo',
    Base.metadata,
    Column('voo_id', Integer, ForeignKey('voos.id')),
    Column('funcionario_id', Integer, ForeignKey('funcionarios.id'))
)

voo_passageiro = Table(
    'voo_passageiro', Base.metadata,
    Column('voo_id', ForeignKey('voos.id'), primary_key=True),
    Column('passageiro_id', ForeignKey('passageiros.id'), primary_key=True)
)

class Voo(Base):
    __tablename__ = 'Voos'

    id = Column(Integer, primary_key=True)
    numero_voo = Column(String(10), nullable=False)
    origem = Column(String(50), nullable=False)
    destino = Column(String(50), nullable=False)

    aeronave_id = Column(Integer, ForeignKey("aeronaves.id"))
    aeronave = relationship("MiniAeronave")

    passageiros = relationship("Passageiro", secondary="voo_passageiro")
    tripulacao = relationship("Funcionario", secondary="voo_tripulante")
