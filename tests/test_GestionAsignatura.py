import unittest

from src.modelo.Asignatura import Asignatura
from src.logica.gestionAsignatura import GestionAsignatura
from src.modelo.declarative_base import Session


class test_gestionAsignatura(unittest.TestCase):
    def setUp(self):
        '''gestion de asignatura'''
        self.gestionAsignatura = GestionAsignatura
        '''abrimos sesion'''
        self.session = Session()
        '''Creamos los objetos'''
        self.Asignatura1 = Asignatura(idAsignatura="AS001", nombre="Diseño de Sistemas", creditos=4, Asignatura=())
        self.Asignatura2 = Asignatura(idAsignatura="AS002", nombre="Analisis de Requerimientos de Software", creditos=4,
                                      Asignatura=())
        self.Asignatura3 = Asignatura(idAsignatura="AS003", nombre="Redes de Informacion", creditos=4, Asignatura=())

        '''Adiciona los objetos a la session'''
        self.session.add(self.Asignatura1)
        self.session.add(self.Asignatura2)
        self.session.add(self.Asignatura3)

        '''presiste los objetos y cerramos session'''
        self.session.commit()
        self.session.close()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()
        '''Consulta todos los álbumes'''
        busqueda = self.session.query(Asignatura).all()
        '''Borra todos los álbumes'''
        for Asignatura in busqueda:
            self.session.delete(Asignatura)
        self.session.commit()
        self.session.close()

    def test_agregar_asignatura(self):
        '''Prueba la adición de una asignatura'''
        resultado = self.gestionAsignatura.agregar_asignatura(idAsignatura="AS004", nombre="Diseño de Redes", creditos=3)
        self.assertEqual(resultado, True)

    def test_agregar_asignatura_repetido(self):
        '''Prueba la adición de una asignatura'''
        resultado = self.gestionAsignatura.agregar_asignatura(idAsignatura="AS001", nombre="Diseño de Sistemas", creditos=4)
        self.assertNotEqual(resultado, True)

    def test_editar_album(self):
        '''Prueba la edición de dos álbumes'''
        # Se cambia el nombre de la primera asignatura creada por uno que no existe
        resultado1 = self.gestionAsignatura.agregar_asignatura(idAsignatura="AS004",
                                                               nombre="Diseño de Redes e Implementacion", creditos=3)
        # Se cambia el nombre de la segunda asignatura creada por uno que ya existe
        resultado2 = self.gestionAsignatura.agregar_asignatura(idAsignatura="AS001", nombre="Diseño de Sistemas",
                                                               creditos=4)
        self.assertTrue(resultado1)
        self.assertFalse(resultado2)


if __name__ == '__main__':
    unittest.main()
