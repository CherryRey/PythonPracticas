"""You have stumbled across the divine pleasure that is owning a dog and a garden. Now time to pick up all the cr@p! :D
Given a 2D array to represent your garden, you must find and collect all of the dog cr@p - represented by '@'.
You will also be given the number of bags you have access to (bags), and the capactity of a bag (cap). 
If there are no bags then you can't pick anything up, so you can ignore cap.
You need to find out if you have enough capacity to collect all the cr@p and make your garden clean again.
If you do, return 'Clean', else return 'Cr@p'.
Watch out though - if your dog is out there ('D'), he gets very touchy about being watched. If he is there you need to return 'Dog!!'.
For example:

bags = 2
cap = 2
x (or garden) =
[[ _ , _ , _ , _ , _ , _ ],
 [ _ , _ , _ , _ , @ , _ ],
 [ @ , _ , _ , _ , _ , _ ]]"""

def crap(garden, bags, cap):
    countCrap = 0 # Sólo necesito inicializar una variable que cuente "crap"
    
    #Como "garden" es una lista de listas debo recorrerlo con un for anidado
    for lista in garden:
        for element in lista:
            #Si encuentra una D, devuelve "Dog"
            if element == 'D':
                return "Dog!!"
             #Sino, añade al contador
            if element == '@':
                countCrap += 1
    

    if bags == 0 or countCrap > bags* cap:
            return "Cr@p!"
    else:
        return "Clean"

 #Pimer intento fallido
def crap1(garden, bags, cap):
    garden = [] # Garden es un array
    bags = 0
    cap = 0
    countCrap = 0

    for element in garden:
        if element == 'D':
            return "Dog!"
        if element == '@' and element != 'D':
            countCrap += 1 
    
        if (bags*cap) > 0:
            countCrap - (bags*cap)
            return "Crap!"
        else:
            return "Clean"


                
print(crap([['D','@','@','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 2))