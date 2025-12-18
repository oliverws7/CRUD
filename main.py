from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

# Criar tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Restaurantes",
    description="CRUD completo de restaurantes com FastAPI",
    version="1.0.0"
)

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Restaurantes"}

# CREATE
@app.post("/restaurantes/", response_model=schemas.Restaurante, status_code=status.HTTP_201_CREATED)
def criar_restaurante(restaurante: schemas.RestauranteCreate, db: Session = Depends(get_db)):
    return crud.create_restaurante(db=db, restaurante=restaurante)

# READ ALL
@app.get("/restaurantes/", response_model=list[schemas.Restaurante])
def listar_restaurantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    restaurantes = crud.get_restaurantes(db, skip=skip, limit=limit)
    return restaurantes

# READ ONE
@app.get("/restaurantes/{restaurante_id}", response_model=schemas.Restaurante)
def buscar_restaurante(restaurante_id: int, db: Session = Depends(get_db)):
    db_restaurante = crud.get_restaurante(db, restaurante_id=restaurante_id)
    if db_restaurante is None:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")
    return db_restaurante

# UPDATE
@app.put("/restaurantes/{restaurante_id}", response_model=schemas.Restaurante)
def atualizar_restaurante(restaurante_id: int, restaurante: schemas.RestauranteUpdate, db: Session = Depends(get_db)):
    db_restaurante = crud.update_restaurante(db, restaurante_id=restaurante_id, restaurante=restaurante)
    if db_restaurante is None:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")
    return db_restaurante

# DELETE
@app.delete("/restaurantes/{restaurante_id}")
def remover_restaurante(restaurante_id: int, db: Session = Depends(get_db)):
    sucesso = crud.delete_restaurante(db, restaurante_id=restaurante_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")
    return {"message": "Restaurante deletado com sucesso"}