def cuckoo_clock(initial_time, n):
    #Separo el parametro "initial_time" en dos variables con el método split() de str.
    #Usamos map, para indicar que lo obtenido sea "int"
    hora, minutos = map(int, (initial_time.split(sep=":")))
    
    #Iniciamos un contador para los chimes
    contador = 0

    #Antes indicamos que si la hora está en punto, cuente los chimes de la hora.
    if minutos == 00:
        contador =+ hora
            #También, si los minutos dado en la entrada  están en {15, 30, 45} agregue al contador un "chime"
    if minutos in {15,30,45}:
        contador +=1

    #Empezamos bucle si en el contador tenemos menos "chimes" que en "n" el nucle se activa
    while contador < n:
        #Indicamos que si la hora en punto tiene más "chimes" de los pedidos, salga del bucle (ej. "10:00", 1, se quedaría en 10:00 ya que hay diez campanadas)
        if hora >= n and minutos == 00:
            contador = hora 
            break
              
        #Si no está en los casos anteriores, entonces avancemos 15 minutos para el siguiente "chime"
        #pero antes guardaremos los minutos antes de avanzar en una variable
        minutos_previos = minutos
        minutos += 15

        #Si los minutos pasan de 60, aumentaremos la hora y reinciaremos los minutps
        if minutos >= 60:
            minutos -= 60
            hora += 1
            #Si la hora es mayor de 12, se reinicia a 1. Formato de 12 hrs.            
            if hora > 12:
                hora = 1
            #Como el cuckoo da campanadas segun el numero de hora (ej. a las 5 da 5 campanadas), al contador le agregamos el n. de hora
            contador += hora
  
        
        # Verificamos si en el avance de 15 minutos hemos pasado por los minutos 15, 30 o 45
        for minuto_campana in [15, 30, 45]:
            if minutos_previos < minuto_campana <= minutos:
                contador += 1
                
        
        # Si en algún momento el contador alcanza o supera el número de campanadas requeridas, salimos
        if contador >= n:
            break
  
    

    if contador >= n and minutos < 15:
        minutos = 00
    #Normalizamos las salidas de los minutos para que solo indique los cuarto de hora 
    if minutos  > 00 and minutos < 30:
        minutos = 15
    if minutos >= 30 and minutos < 45:
        minutos = 30
    if minutos >= 45 and minutos <= 59:
        minutos = 45
        
        
    return f"{hora:02d}:{minutos:02d}"

# Casos de prueba
print(cuckoo_clock("04:00", 5))#04:15
print(cuckoo_clock("12:20", 1))#12:30
print(cuckoo_clock("01:30", 2))#'01:45' 
print(cuckoo_clock("10:00", 1)) #10:00
print(cuckoo_clock("12:30", 3))#1:00
print(cuckoo_clock("12:36", 59))#'08:15'
print(cuckoo_clock("04:01", 10))#05:30
print(cuckoo_clock("03:38", 19))#06:00
print(cuckoo_clock("08:17", 113)) # 08:00
print(cuckoo_clock("10:00", 13)) # 10:45 and it's 10:30


