from pydantic import BaseModel
from typing import Optional

class RestauranteBase(BaseModel):
    nome: str
    endereco: Optional[str] = None
    tipo_cozinha: Optional[str] = None
    capacidade: Optional[int] = None
    descricao: Optional[str] = None

class RestauranteCreate(RestauranteBase):
    pass

class RestauranteUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    tipo_cozinha: Optional[str] = None
    capacidade: Optional[int] = None
    descricao: Optional[str] = None

class Restaurante(RestauranteBase):
    id: int

    class Config:
        from_attributes = True