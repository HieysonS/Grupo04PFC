from sqlalchemy import column, char, date, ForeignKey
from .declarative_base import Base

class estudiante(Base):
    _tablename_ = 'estudante'
    CodigoE = Column(char(8), primary_key=True)
    ContrasenaE = Column(char(15))
    Nombre = Column((30))
    AplellidoPaternoE = column(char(30))
    AplellidoMaternoE = column(char(30))
    FechaNacimientoE = column(date)
    AsignaturaEstudiante = column(Integer, ForeignKey('Estudiante.CodigoE'))