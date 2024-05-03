from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    Float,
    Boolean
)
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UNIDADE_PRODUCAO(Base):

    __tablename__ = "UNIDADE_PRODUCAO"
    numero = Column(Integer, primary_key=True, autoincrement=False)
    peca_hora_nominal =  Column(Float, nullable=False)

class REGISTRO_FALHA(Base):
    
    __tablename__ = "REGISTRO_FALHA"
    id = Column(Integer, primary_key=True, autoincrement=False)
    severidade =  Column(Boolean, nullable=False)
    inicio =  Column(Date, nullable=False)
    fim =  Column(Date, nullable=False)
    numero_unidade_producao = Column(Integer, ForeignKey("UNIDADE_PRODUCAO.numero"), nullable=False, autoincrement=False)

class PECA(Base):
    __tablename__ = "PECA"
    numero = Column(Integer, primary_key=True, autoincrement=False)
    status = Column(String, nullable=False)
    inicio_fabricacao = Column(Date,nullable=False)
    fim_fabricacao = Column(Date,nullable=False)
    numero_unidade_producao = Column(Integer, ForeignKey ("UNIDADE_PRODUCAO.numero") ,nullable=False,autoincrement=False)

class SOPRADORA(Base):
    __tablename__ = "SOPRADORA"
    numero = Column(Integer, primary_key=True, autoincrement=False)
    vazao_sopro = Column(Float, nullable=False)
    pressao_sopro = Column(Float, nullable=False)

class FRESADORA(Base):
    __tablename__ = "FRESADORA"
    numero = Column(Integer, primary_key=True, autoincrement=False)
    velocidade_rotacao = Column(Float, nullable=False)
    profundidade_corte = Column(Float, nullable=False)


class TORNO_CNC(Base):
    __tablename__ = "TORNO_CNC"
    numero = Column(Integer, primary_key=True, autoincrement=False)
    velocidade_rotacao = Column(Float, nullable=False)
    tolerancia = Column(Float, nullable=False)
    
class IMPRESSORA_3D(Base):
    __tablename__ = "IMPRESSORA_3D"
    numero = Column(Integer, primary_key=True, autoincrement=False)
    espessura_camada = Column(Float, nullable=False)
    tipo_material = Column(String, nullable=False)




 
