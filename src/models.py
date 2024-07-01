import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    password =  Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    fecha_subscripcion = Column(DateTime, nullable=False)
    favoritos = relationship('Favorito', back_populates='usuario')
    # Usuario puede tener muchos favoritos, y c/ favorito pertenece a un usuario

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    clima = Column(String, nullable=True)
    terreno = Column(String, nullable=True)
    favoritos = relationship('Favorito', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    especie = Column(String, nullable=True)
    afiliacion = Column(String, nullable=True)
    favoritos = relationship('Favorito', back_populates='personaje')

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)

    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')


def to_dict(self):
    return {}

try:
    result = render_er(Base, 'diagram.png')
    print("El diagrama UML fue generado exitosamente")
except Exception as e:
    print("Hubo un error al generar el diagrama UML")
    print(str(e))