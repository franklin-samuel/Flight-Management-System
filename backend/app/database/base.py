#SQLalchemy base + engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
import os
Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "flight.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


