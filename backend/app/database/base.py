#SQLalchemy base + engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

DATABASE_URL = "sqlite:///app/flight.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


