from PyQt5 import uic, QtWidgets
app = QtWidgets.QApplication([])

principal = uic.loadUi("D:\PROYECTOSCDS\Proyectos\Grupo04PFC\src\ista\menu_principal.ui")
agregar_Estudiante = uic.loadUi("D:\PROYECTOSCDS\Proyectos\Grupo04PFC\src\ista\hagregar_estudiante.ui")
ver_notas = uic.loadUi("D:\PROYECTOSCDS\Proyectos\Grupo04PFC\src\ista\hver_notas.ui")
editar_asignatura=uic.loadUi("D:\PROYECTOSCDS\Proyectos\Grupo04PFC\src\ista\editar_asignatura.ui")
agregar_asignatura=uic.loadUi("D:\PROYECTOSCDS\Proyectos\Grupo04PFC\src\ista\hagregar_asignatura.ui")
editar_estudiante=uic.loadUi("D:\PROYECTOSCDS\Proyectos\Grupo04PFC\src\ista\editar_estudiante.ui")
agregar_nota=uic.loadUi("D:\PROYECTOSCDS\Proyectos\Grupo04PFC\src\ista\hagregar_nota.ui")
def Entrar_asignatura():
    principal.hide()
    editar_asignatura.show()
def Entrar_ver_notas():
    principal.hide()
    ver_notas.show()
def Entrar_Agregar():
    principal.hide()
    agregar_Estudiante.show()

def entrar_editar_asignatura():
    principal.hide()
    editar_asignatura.show()

def regresar_editar_asignatura():
    editar_asignatura.hide()
    principal.show()

def entrar_agregar_nota():
    principal.hide()
    agregar_nota.show()

def regresar_agregar_nota():
    agregar_nota.hide()
    principal.show()


def entrar_editar_estudiante():
    principal.hide()
    editar_estudiante.show()

def regresar_editar_estudiante():
    editar_estudiante.hide()
    principal.show()


def entrar_agregar_asignatura():
    principal.hide()
    agregar_asignatura.show()

def regresar_agregar_asignatura():
    agregar_asignatura.hide()
    principal.show()



def Regresar_principal_Agregar():
    agregar_Estudiante.hide()
    principal.show()

def Regresar_principal_Ver_Notas():
    ver_notas.hide()
    principal.show()



principal.pushButton_6.clicked.connect(Entrar_ver_notas)
ver_notas.Regresar.clicked.connect(Regresar_principal_Ver_Notas)
principal.pushButton.clicked.connect(agregar_Estudiante.show)
agregar_Estudiante.Regresar.clicked.connect(Regresar_principal_Agregar)
principal.pushButton_4.clicked.connect(Entrar_asignatura)
principal.pushButton_3.clicked.connect(entrar_editar_asignatura)
editar_asignatura.pushButton_3.clicked.connect(regresar_editar_asignatura)
principal.pushButton_4.clicked.connect(entrar_agregar_asignatura)
agregar_asignatura.Regresar.clicked.connect(regresar_agregar_asignatura)
principal.pushButton_2.clicked.connect(entrar_editar_estudiante)
editar_estudiante.pushButton_6.clicked.connect(regresar_editar_estudiante)
principal.pushButton_5.clicked.connect(entrar_agregar_nota)
agregar_nota.pushButton_3.clicked.connect(regresar_agregar_nota)





principal.show()
app.exec()
