# app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import passageiros, voos, funcionarios
app = FastAPI(
    title="API de Gestão de Voos",
    version="1.0.0",
    description="Backend para controle de voos, passageiros e tripulação"
)

# Configurar CORS para permitir acesso do frontend (React, por exemplo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Samuel coloca o endereço frontend aqui cria
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(passageiros.router)
app.include_router(voos.router)
app.include_router(funcionarios.router)