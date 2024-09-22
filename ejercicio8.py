'''Escribe una función que pueda decirte si un año (número entero) es bisiesto o no'''
'''A year is considered a leap year if that year is exactly divisible by 4, except for years that end with 00(century year). 
A century year is a leap year if that is exactly divisible by 400. 
However, a year which not divisible by 400 and divisible by 100 is not a leap year.'''


annio = int(input("Escribe el año para saber si es bisiesto o no: "))

def annyo():
        if annio % 4 == 0 and annio % 400 ==0 or annio % 100 != 0:
            print(f"{annio} es un año bisiesto")
        else:
            print(f"{annio}  no es un año bisiesto")
            

annyo()