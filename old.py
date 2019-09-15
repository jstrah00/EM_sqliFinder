from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

context = ssl._create_unverified_context()

url = "https://colegiomariareina.edu.ar/"
pagina = urlopen(url, context=context)
soup = BeautifulSoup(pagina, features="html.parser")
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

print("Busqueda inicial: ")
print(len(links))
print(links)

allLinks = []
allLinks = links

for esteLink in links:

    print("Analizando: ")
    print(esteLink)

    pag = urlopen(esteLink, context=context)
    soup = BeautifulSoup(pag, features="html.parser")

    for lonk in soup.findAll('a', attrs={'href': re.compile("^http://")}):

        esto = lonk.get('href')
        if esto in allLinks:
            print("El link ya esta en la lista")
        else:
            allLinks.append(esto)
            print("Se encontro un nuevo link")
            print(esto)

print("Todos los links: ")
print(len(allLinks))
print(allLinks)