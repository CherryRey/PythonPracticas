lista =["azul", "verde", "amarillo", "rojo", "azul", "azul", "amarillo", "rojo", "rosa", "verde", "azul", "rosa","rojo","rojo", "magenta"]

def contador(lista):
    contar = dict()
    for i in lista:
        if i in contar:
            contar[i] +=1
        else:
            contar[i] = 1
    print(contar)

contador()