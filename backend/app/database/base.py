#SQLalchemy base + engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

DATABASE_URL = "sqlink"

engine = create_engine(
    DATABASE_URL,
)