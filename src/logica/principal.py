from PyQt5 import uic, QtWidgets
app = QtWidgets.QApplication([])

principal = uic.loadUi("D:\construccion\proyectos\Grupo04PFC\src\ista\menu_principal.ui")
agregar_Estudiante = uic.loadUi("D:\construccion\proyectos\Grupo04PFC\src\ista\hagregar_estudiante.ui")

def Entrar_Agregar():
    principal.hide()
    agregar_Estudiante.show()
def Regresar_principal_Agregar():
    agregar_Estudiante.hide()
    principal.show()

principal.pushButton.clicked.connect(agregar_Estudiante.show)
agregar_Estudiante.Regresar.clicked.connect(Regresar_principal_Agregar)

principal.show()
app.exec()
