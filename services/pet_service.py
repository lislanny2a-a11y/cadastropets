from models.pet_model import pet
from sqlalchemy.orm import Session

def criar_pet(db: Session, nome: str, especie: str, idade: int):

    novo_pet = pet(nome=nome, especie=especie, idade=idade)
    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)
    return novo_pet

def listar_pets(db: Session):
    return db.query(pet).all()

