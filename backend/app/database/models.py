from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.base import Base
import uuid

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
    __tablename__ = 'voos'

    id = Column(Integer, primary_key=True)
    numero_voo = Column(String(10), nullable=False)
    origem = Column(String(50), nullable=False)
    destino = Column(String(50), nullable=False)

    aeronave_id = Column(Integer, ForeignKey("aeronaves.id"))
    aeronave = relationship("MiniAeronave", back_populates="voos")

    companhia_id = Column(Integer, ForeignKey("companhias.id"))
    companhia = relationship("CompanhiaAerea", back_populates="voos")

    passageiros = relationship("Passageiro", secondary="voo_passageiro", back_populates="voos")
    tripulacao = relationship("Funcionario", secondary="tripulantes_voo", back_populates="voos")

class MiniAeronave(Base):
    __tablename__ = 'aeronaves'

    id = Column(Integer, primary_key=True)
    modelo = Column(String, nullable=False)
    capacidade = Column(Integer, nullable=False)

    voos = relationship("Voo", back_populates="aeronave")

class CompanhiaAerea(Base):
    __tablename__ = 'companhias'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    voos = relationship("Voo", back_populates="companhia")

class Passageiro(Base):
    __tablename__ = "passageiros"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)

    voos = relationship("Voo", back_populates="passageiros")
    bagagens = relationship("Bagagem", back_populates="dono")

class Bagagem(Base):
    __tablename__ = 'bagagens'

    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    peso = Column(Integer, nullable=False)

    passageiro_id = Column(Integer, ForeignKey('passageiros.id'))
    dono = relationship("Passageiro", back_populates="bagagens")

class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    cargo = Column(String, nullable=False)
    matricula = Column(String, unique=True,  nullable=False)

    voos = relationship("Voo", secondary=tripulantes_voo, back_populates="tripulacao")

