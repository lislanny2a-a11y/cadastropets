from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import pet_service

router = APIRouter(prefix="/pets", tags=["Pets"])

@router.post("/")
def criar_pet(nome: str, especie: str, idade: int, db: Session = Depends(get_db)):
    try:
        pet_criado = pet_service.criar_pet(db, nome, especie, idade)
        return pet_criado
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/")
def listar_pets(db: Session = Depends(get_db)):
    return pet_service.listar_pets(db)