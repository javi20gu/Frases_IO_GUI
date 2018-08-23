

import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMessageBox, QWidget

from .version import INFORMACION


URL = "https://github.com/javi20gu/Frases_IO_GUI/blob/master/modules/version.py"


def buscarActualizacion():
    # Obtenemos los datos, segun la palabra que introduzcamos.
    r = requests.get(URL)

    # Verificamos que va a responder con el codigo 200.
    if r.status_code == 200:
        # Extraemos todos los datos
        soup = BeautifulSoup(r.text, "html.parser")
        # Buscamos todas las definiciones.
        definiciones = soup.find_all("span", {"class": "pl-c1"})
        versiones = [definicion.getText() for definicion in definiciones]
        for version in versiones:
            if version > INFORMACION["Version"]:
                QMessageBox().information(QWidget(), "Actualización", "Nueva Actualización disponible v{}".format(version))
