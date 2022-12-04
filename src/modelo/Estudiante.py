from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class Estudiante(Base):
    __tablename__="estudiante"
    DNIEstudiante=Column(String,primary_key = True)
    ApellidoPaterno = Column ( String )
    ApellidoMaterno = Column ( String )
    NombreEstudiante = Column ( String )
    CandidatoBeca = Column ( Boolean )
    asignaturaEstudiante = relationship('AsignaturaEstudiante', secondary='asignatura_estudiante')
