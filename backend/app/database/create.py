from database.base import Base, engine
from database import models

def create_database():
    print("Criando o banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Banco de dados criado com sucesso.")

if __name__ == "__main__":
    create_database()