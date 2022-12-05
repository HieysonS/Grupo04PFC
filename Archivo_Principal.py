from src.modelo.Estudiante import Estudiante
from src.modelo.Asignatura import Asignatura
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
   #Crear la BD
   Base.metadata.create_all(engine)

   #Abre la sesion
   session = Session()

   # crear estudiantes
   estudiante_1 = Estudiante ( apellidoPaterno = "Rios" , apellidoMaterno = "Ortega" , nombres = "Juan Carlos" ,
                              Candbeca = 1 )
   estudiante_2 = Estudiante ( apellidoPaterno = "Chavez" , apellidoMaterno = "Matos" , nombres = "Pedro" ,
                              Candbeca = 0 )
   estudiante_3 = Estudiante ( apellidoPaterno =  "Veliz" , apellidoMaterno = "Torres" , nombres = "Luis Alberto" ,
                              Candbeca = 1 )
   estudiante_4 = Estudiante ( apellidoPaterno =  "Garcia" , apellidoMaterno = "Mateo" , nombres = "Miguel Angel" ,
                              Candbeca = 1 )
   estudiante_5 = Estudiante( apellidoPaterno = "Mendoza", apellidoMaterno = "marin", nombres = "Maria",
                             Candbeca = 0 )

   session.add ( estudiante_1 )
   session.add ( estudiante_2 )
   session.add ( estudiante_3 )
   session.add ( estudiante_4 )
   session.add ( estudiante_5 )

   # crear asignatura
   asignatura1 = Asignatura ( nombreAsignatura="Diseño de Sistemas", Creditos = 4 )
   asignatura2 = Asignatura ( nombreAsignatura="Analisis de Requerimientos de Software", Creditos = 4 )
   asignatura3 = Asignatura ( nombreAsignatura="Redes de Informacion", Creditos = 2 )
   asignatura4 = Asignatura ( nombreAsignatura="Programacion", Creditos = 3 )
   asignatura5 = Asignatura ( nombreAsignatura="Conmutacion de Redes" ,Creditos = 3 )

   session.add ( asignatura1 )
   session.add ( asignatura2 )
   session.add ( asignatura3 )
   session.add ( asignatura4 )
   session.add ( asignatura5 )

   # Relacionar Asignatura con estudiantes
   asignatura1.estudiantes = [ estudiante_1 , estudiante_4 ]
   asignatura2.estudiantes = [ estudiante_2 , estudiante_3 ]
   asignatura3.estudiantes = [ estudiante_3 , estudiante_4 ]
   asignatura4.estudiantes = [ estudiante_4 , estudiante_2 ]
   asignatura5.estudiantes = [ estudiante_5 , estudiante_1 ]
   session.commit()
   session.close()