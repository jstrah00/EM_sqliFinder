from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

context = ssl._create_unverified_context()  # Para que no tire error el urlopen
allLinks = []  # Array donde guardo el resultado de todos los links


def obtenerLinks(url):
    # Traigo el html de la pagina
    print("Analizando: " + url)
    pagina = urlopen(url, context=context)
    soup = BeautifulSoup(pagina, features="html.parser")

    links = []
    # Busco todos los links a los que redirecciona
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        x = link.get('href')

        if x in allLinks:  # Si el link que encontro ya esta en la lista no hago nada
            print("Se encontro un link redundante")

        else:  # Si el link no esta en la lista lo agrego
            print("Se encontro un nuevo link: " + x)
            allLinks.append(x)

            obtenerLinks(x)  # Corro esta funcion, con el nuevo link

    return allLinks  # Devuelve la lista de todos los links


print(obtenerLinks("https://colegiomariareina.edu.ar/"))

