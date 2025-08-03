from sqlalchemy.orm import Session
from app.database.models import MiniAeronave as MiniAeronaveDB
from app.services.mappers.aeronave_mapper import aeronave_from_db