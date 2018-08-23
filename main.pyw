from sys import argv, exit
from PyQt5.Qt import Qt
from os import getcwd
from threading import Thread

from modules import buscarActualizacion
from modules import extractTipos 
from modules import extractDefiniciones
from modules import ABREVIACIONES
from UI.UI_main import QtWidgets, QtCore, Ui_Principal, QtGui


class App(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.salir.setIcon(QtGui.QIcon("{}/asserts/salir.png".format(getcwd())))
        self.ui.salir.clicked.connect(self.salir)
        self.ui.inputTexto.returnPressed.connect(self.entrada)

    def salir(self):
        self.close()
        del self
        exit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def entrada(self):
        palabras = self.ui.inputTexto.text().split(" ")
        self.process = SecondProcess()
        self.process.setPalabras(palabras)
        self.process.setVentanaPadre(self.ui)
        self.process.start()

        
class SecondProcess(QtCore.QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        
        if self.ventana.modoTipo.isChecked():
            for palabra in self.palabras:
                tipos = extractTipos(palabra)
            
                if tipos:
                    try:
                        tipos = [ABREVIACIONES[tipo] for tipo in tipos]
                        resultado = " o ".join(tipos)
                        self.ventana.inputResultado.addItem("La palabra |-{}-| es de tipo:  {}"
                            .format(palabra, resultado))
                    except KeyError as a:
                        self.ventana.inputResultado.addItem("Error ({}): Abreviatura no incluida en el diccionario ({}), si quiere informar utilize el email -> javierhidalgo_c@hotmail.com".format(palabra, a))
    
                else:
                    self.ventana.inputResultado.addItem(
                        "La palabra |-{}-| aún no está"
                        " en el diccionario".format(palabra))
        else: 
            for palabra in self.palabras:
                tipos = extractDefiniciones(palabra)
            
                if tipos:
                    resultado = "\n -->".join(tipos)
                    self.ventana.inputResultado.addItem("La palabra |-{}-| se usa para:  \n --> {}"
                        .format(palabra, resultado))
                else:
                    self.ventana.inputResultado.addItem(
                        "La palabra |-{}-| aún no está"
                        " en el diccionario".format(palabra))

    def setPalabras(self, palabras: list):
        self.palabras = palabras

    def setVentanaPadre(self, ventanaPadre): 
        self.ventana = ventanaPadre


if __name__ == '__main__':
    cmd = QtWidgets.QApplication(argv)
    ventana = QtWidgets.QSplashScreen(QtGui.QPixmap("{}/asserts/loanding.PNG".format(getcwd())), Qt.WindowStaysOnBottomHint)
    ventana.show()
    ventana.showMessage("Cargando...", Qt.AlignBottom, Qt.black)
    app = App()
    app.show()
    ventana.finish(app)
    Thread(target=buscarActualizacion)
    exit(cmd.exec_())
