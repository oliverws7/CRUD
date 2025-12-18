from sqlalchemy.orm import Session
from models import Restaurante
from schemas import RestauranteCreate, RestauranteUpdate

def get_restaurante(db: Session, restaurante_id: int):
    return db.query(Restaurante).filter(Restaurante.id == restaurante_id).first()

def get_restaurantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Restaurante).offset(skip).limit(limit).all()

def create_restaurante(db: Session, restaurante: RestauranteCreate):
    db_restaurante = Restaurante(**restaurante.model_dump())
    db.add(db_restaurante)
    db.commit()
    db.refresh(db_restaurante)
    return db_restaurante

def update_restaurante(db: Session, restaurante_id: int, restaurante: RestauranteUpdate):
    db_restaurante = db.query(Restaurante).filter(Restaurante.id == restaurante_id).first()
    if db_restaurante:
        update_data = restaurante.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_restaurante, key, value)
        db.commit()
        db.refresh(db_restaurante)
    return db_restaurante

def delete_restaurante(db: Session, restaurante_id: int):
    db_restaurante = db.query(Restaurante).filter(Restaurante.id == restaurante_id).first()
    if db_restaurante:
        db.delete(db_restaurante)
        db.commit()
        return True
    return False