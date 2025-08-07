from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database.base import Base

def limpar_database(session: Session):
    session.execute(text("PRAGMA foreign_keys = OFF"))
    session.commit()

    for table in reversed(Base.metadata.sorted_tables):
        session.execute(text(f"DELETE FROM {table.name}"))

    session.commit()
    session.execute(text("PRAGMA foreign_keys = ON"))
    session.commit()