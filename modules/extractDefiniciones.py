import requests
from bs4 import BeautifulSoup

URL = "http://www.wordreference.com/definicion/"


def extractDefiniciones(palabra: str):
    # Obtenemos los datos, segun la palabra que introduzcamos.
    r = requests.get(URL + palabra)

    # Verificamos que va a responder con el codigo 200.
    if r.status_code == 200:
        # Extraemos todos los datos
        soup = BeautifulSoup(r.text, "html.parser")
        # Buscamos todas las definiciones.
        definiciones = soup.find_all("ol", {"class": "entry"})
        
        # Comprobamos que la palabra exista.
        if definiciones:
            # Retornamos los tipos de la palabra.
            return [definicion.getText() for definicion in definiciones]
