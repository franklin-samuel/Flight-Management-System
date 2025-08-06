import pytest
from fastapi.testclient import TestClient
from app.api.app import app
from app.database.session import get_db, SessionLocal
from app.database.base import Base, engine

# Opcional: garante que as tabelas existem
@pytest.fixture(scope="session", autouse=True)
def create_tables():
    Base.metadata.create_all(bind=engine)

# Cliente de testes usando o banco real
@pytest.fixture
def client():
    def override_get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c