# Session Maker
from sqlalchemy.orm import sessionmaker
from app.database.base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)