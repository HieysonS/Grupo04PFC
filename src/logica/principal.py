from PyQt5 import uic, QtWidgets
app = QtWidgets.QApplication([])

principal = uic.loadUi("D:\construccion\proyectos\Grupo04PFC\src\ista\menu_principal.ui")
agregar_Estudiante = uic.loadUi("D:\construccion\proyectos\Grupo04PFC\src\ista\hagregar_estudiante.ui")
ver_notas = uic.loadUi("D:\construccion\proyectos\Grupo04PFC\src\ista\hver_notas.ui")
edit_asignatura = uic.loadUi("D:\construccion\proyectos\Grupo04PFC\src\ista\editar_asignatura.ui")


def Entrar_asignatura():
    principal.hide()
    edit_asignatura()
def Entrar_ver_notas():
    principal.hide()
    ver_notas.show()
def Entrar_Agregar():
    principal.hide()
    agregar_Estudiante.show()

def Regresar_principal_edit_asignatura():
    edit_asignatura.hide()
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
edit_asignatura.pushButton_3.clicked.connect(Regresar_principal_edit_asignatura)

principal.show()
app.exec()
