from sqlalchemy import column, char, time, ForeignKey
from .declarative_base import base

class asignatura(base):
    _tablename_ ='asignatura'
    NRC = column(char(8), primary_key=true)
    NombreAsg = column(char(100))
    Creditos = column(int)
    AsignaturaDocente = column(Integer, ForeignKey('Asignatura.NRC'))