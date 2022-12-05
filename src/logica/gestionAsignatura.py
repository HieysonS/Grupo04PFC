from src.modelo.Asignatura import Asignatura
from src.modelo.declarative_base import engine, Base, session

class GestionAsignatura():

    def _init_(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, idAsignatura, nombreAsignatura, creditos):
        busqueda = session.query(Asignatura).filter(Asignatura.idAsignatura == idAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(idAsignatura = idAsignatura, nombreAsignatura=nombreAsignatura, credito = creditos)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False


    def editar_asignatura(self, idAsignatura, nombreAsignatura,creditos):
        busqueda = session.query(Asignatura).filter(Asignatura.idAsignatura == idAsignatura).all()
        if len(busqueda) == 0:
            Asignatura = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).first()
            Asignatura.idAsignatura = idAsignatura
            Asignatura.nombreAsignatura = nombreAsignatura
            Asignatura.creditos = creditos
            session.commit()
            return True
        else:
            return False