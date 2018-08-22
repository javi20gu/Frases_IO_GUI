import requests
from bs4 import BeautifulSoup


class Extractor:
    """Extractor
    Permite extraer un el tipo y la definicion de una palabra realizando
    web scrapping al sitio web http://www.wordreference.com/
    """

    def __init__(self, url):
        self._url = url

    def _extraer(self, palabra: str):
        # Obtenemos los datos, segun la palabra que introduzcamos.
        r = requests.get(self._url + palabra)
        definiciones = {}
        # Verificamos que va a responder con el codigo 200.
        if r.status_code == 200:
            # Extraemos todos los datos
            soup = BeautifulSoup(r.text, "html.parser")
            # Buscamos todas las definiciones.
            definiciones = soup.find_all("ol", {"class": "entry"})

        return definiciones

    def tipos(self, palabra: str):
        definiciones = self._extraer(palabra)
        # Comprobamos que la palabra exista.
        if definiciones:
            # Retornamos los tipos de la palabra.
            return [definicion.getText()[:definicion.getText()[:17]
                                         .rfind(".")] for definicion in definiciones]

    def definiciones(self, palabra: str):
        definiciones = self._extraer(palabra)
        # Comprobamos que la palabra exista.
        if definiciones:
            # Retornamos los tipos de la palabra.
            return [definicion.getText() for definicion in definiciones]
