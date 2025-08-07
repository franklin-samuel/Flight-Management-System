import pytest
from fastapi.testclient import TestClient
from app.api.app import app  # ou onde está seu FastAPI

@pytest.fixture
def client():
    return TestClient(app)