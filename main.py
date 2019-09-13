from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

def obtenerLinks(url):

    context = ssl._create_unverified_context()
    pagina = urlopen(url, context=context)
    soup = BeautifulSoup(pagina, features="html.parser")
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    return links

links = obtenerLinks("https://colegiomariareina.edu.ar/")
print(links)
