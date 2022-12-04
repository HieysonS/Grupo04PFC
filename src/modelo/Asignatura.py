from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modelo.declarative_base import Base

class Asignatura(Base):
    __tablename__="asignatura"
    idAsignatura=Column(String,primary_key = True)
    nombreAsignatura = Column ( String )
    creditos = Column(Integer)
    asignaturaEstudiante = relationship('AsignaturaEstudiante', secondary='asignatura_estudiante')

class AsignaturaEstudiante(Base):
    __tablename__ = 'asignatura_estudiante'

    asignatura = Column(Integer, ForeignKey('Asignatura.idAsignatura'), primary_key=True)
    estudiante = Column(Integer, ForeignKey('Estudiante.DNIEstudiante'), primary_key=True)
    nota = Column(Integer)
