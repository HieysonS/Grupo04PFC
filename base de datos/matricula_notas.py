import enum
from sqlalchemy import column, Integer, String, enum, time, ForeignKey
from sqlalchemy.orm import relationship
from estudiante import CodigoE
from asignatura import NRC
from .declarative_base import Base

class AsignaturaEstudiante(Base):
    _tablename_ ='asignaturaEstudiante'
    Estuadiante = relationship(CodigoE)
    Asignatura = relationship(NRC)
    HorarioAE = column(time)
    Ex1C1 = column(init)
    Ex2C1 = column(init)
    Consolidado1 = column(init)
    Ex1C2 = column(init)
    Ex2C2 = column(init)
    Consolidado2 = column(init)
    Parcial = column(init)
    Final =column(init)