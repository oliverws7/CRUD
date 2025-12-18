from sqlalchemy import Column, Integer, String, Text
from database import Base

class Restaurante(Base):
    __tablename__ = "restaurantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200))
    tipo_cozinha = Column(String(50))
    capacidade = Column(Integer)
    descricao = Column(Text)