'''''
x = "http://colegiomariareina.edu.ar/onu/?page_id=155"
y = ["http://colegiomariareina.edu.ar/aa/?page_id=154","http://colegiomariareina.edu.ar/otro/?page_id=15","http://colegiomariareina.edu.ar/otro/?page_id=15","http://colegiomariareina.edu.ar/a/?page_id=15"]

esto = x[:len(x) - 5]
print(esto)
esta = False

for wachin in y:
    if esto in wachin:
        esta = True
        print("Ya esta")
    else:
        print("no esta")

if esta:
    print("El wachin esta")
    esta = False
    pass
else:
    print("Lo agregamos")
    
    
'''''


link = "http://colegiomariareina.edu.ar/onu/?page_id=16"
principio = link.split("?")
print(principio)
principio = str(principio[0]) + str(principio[1][:2])
print("Primera parte de la url: ", principio)