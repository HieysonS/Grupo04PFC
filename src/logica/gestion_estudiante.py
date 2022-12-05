from src.modelo.Estudiante import Estudiante
from src.modelo.declarative_base import engine, Base, session

class GestionEstudiante():

    def init(self):
        Base.metadata.create_all(engine)

    def agregar_estudiante(self, DNIEstudiante, ApellidoPaterno,ApellidoMaterno,NombreEstudiante,CandidatoBeca):
        if len(NombreEstudiante)==0:
            return False
        busqueda = session.query(Estudiante).filter(Estudiante.DNIEstudiante == DNIEstudiante).all()
        if len(busqueda) == 0:
            estudiante = Estudiante(NombreEstudiante=NombreEstudiante, ApellidoPaterno=ApellidoPaterno, ApellidoMaterno=ApellidoMaterno, CandidatoBeca=CandidatoBeca)
            session.add(estudiante)
            session.commit()
            return True
        else:
            return False