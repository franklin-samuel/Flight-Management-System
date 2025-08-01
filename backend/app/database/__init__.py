from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Voo(Base):
    __tablename__ = 'Voos'

    id = Column(Integer, primary_key=True)
    