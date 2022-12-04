from src.modelo.Asignatura import Asignatura
from src.modelo.declarative_base import engine, Base, session

class GestionAsignatura():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, nombreAsignatura, Creditos):
        if len(nombreAsignatura)==0:
            return False
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura, credito = Creditos)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False
        |

    def editar_asignatura(self, idAsignatura, nombreAsignatura, Creditos):
        if len(nombreAsignatura) == 0:
           return False
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            Asignatura = session.query(Asignatura).filter(Asignatura.idAsignatura == idAsignatura).first()
            Asignatura.nombreAsignatura = nombreAsignatura
            Asignatura.creditos = Creditos
            session.commit()
            return True
        else:
            return False