

if __name__ == '__main__':

    from sys import argv
    from PyQt5 import QtWidgets, QtCore, QtGui
    from os.path import join

    from setting import CARPETA, RUTA_PRINCIPAL
    
    
    cmd = QtWidgets.QApplication(argv)
    
    ventana = QtWidgets.QSplashScreen(QtGui.QPixmap(join(RUTA_PRINCIPAL, CARPETA, "loanding.PNG")),
                                      QtCore.Qt.WindowStaysOnBottomHint)
    ventana.showMessage("Cargando...", QtCore.Qt.AlignBottom, QtCore.Qt.black)
    ventana.show()

    from sys import exit

    from modules import buscarActualizacion, App

    ventana.showMessage("Buscando Actualizaciones...", QtCore.Qt.AlignBottom, QtCore.Qt.black)
    actualizacion = buscarActualizacion()

    if not actualizacion:
        app = App()
        app.show()
        ventana.finish(app)
    else:
        from webbrowser import open
        
        open("https://github.com/javi20gu/Frases_IO_GUI")
        ventana.close()
        exit()
    exit(cmd.exec_())
