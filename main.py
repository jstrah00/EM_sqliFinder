from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

context = ssl._create_unverified_context()  # Para que no tire error el urlopen
allLinks = []  # Array donde guardo el resultado de todos los links
linksGet = []   #Links que hacen get
nombreWeb = ""


def obtenerLinks(url):
    # Traigo el html de la pagina
    #print("Link: " + url)
    pagina = urlopen(url, context=context)
    soup = BeautifulSoup(pagina, features="html.parser")

    links = []

    #Busco todos los links a los que redirecciona
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        x = link.get('href')
        #print("Nombre web: ", nombreWeb)
        if nombreWeb in x: #Si el link tiene algo que ver con la url inicial
            #print("Se encontro un link relacionado")

            if x in allLinks:  # Si el link que encontro ya esta en la lista no hago nada
                #print("link redundante")
                pass

            else:  # Si el link no esta en la lista lo agrego
                #print("Nuevo link: " + x)
                allLinks.append(x)

                ults = x[len(x) - 4 :len(x)]
                if ults != ".pdf" and ults != ".jpg" and ults != "docx" and ults != "jpeg":
                    try:
                        obtenerLinks(x)  # Corro esta funcion, con el nuevo link

                    except:

                        #print("Hubo un error con el link")
                        allLinks.remove(x)
                else:
                    #print("Tipo de archivo no valido (pdf, jpg, docx, jpeg)")
                    pass
        else:
            #print("El link es de otra pagina")
            pass




    return allLinks  # Devuelve la lista de todos los links

def obtenerGet(links):

    for link in links:
        if "=" in link:
            #print("TIENE ID: ")
            #print(link)

            #Revisamos si ya esta esa url, pero con otro id
            principio = link.split("?")
            principio = str(principio[0]) + "?" +str(principio[1][:2])
            #print("Primera parte de la url: ", principio)
            esta = False

            for cadaUrl in linksGet:
                if principio in cadaUrl:
                    esta = True
                    #print("Esta")
                else:
                    #print("No esta")
                    pass

            if esta:
                #print("El link ya esta")
                esta = False
                pass
            else:
                #print("El link no esta, Lo agregamos")
                linksGet.append(link)




    return linksGet

def selecionarLinks(url):
    final = {"get": [], "post": []}
    global nombreWeb
    x = url.split("/")
    nombreWeb = x[2]
    links = obtenerLinks(url)

    print("Array de todos los links:")
    print(links)

    final["get"] = obtenerGet(links)
    print("Array con links GET: ")
    print(final["get"])
    return final


selecionarLinks("https://colegiomariareina.edu.ar/")

