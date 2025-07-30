# Session Maker
from sqlalchemy.orm import sessionmaker
from base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)