from src.modelo.Asignatura import Asignatura
from src.modelo.Estudiante import Estudiante
from src.modelo.declarative_base import session, Base, engine

class GestionNotas():
    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_notas(self, codestudiante, codasignatura, nota):
        if len(codestudiante)==0:
            return False
        busqueda = session.query(codestudiante,codasignatura).filter(Estudiante.DNIEstudiante == codestudiante,Asignatura.idAsignatura==codasignatura).all()
        if len(busqueda) == 0:
            notas = nota(asignatura=codasignatura, Estudiante=codestudiante)
            if (nota > 0 and nota <= 20):
                session.add(notas)
                session.commit()
            return True
        else:
            return False