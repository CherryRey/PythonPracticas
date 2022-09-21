'''contador = 0

while contador < 11:
    print(contador, end= ' ')
    contador += 1'''


'''cuenta = 0
while cuenta < 5:
    print(cuenta)
    cuenta +=2'''


'''cuenta = 0
numero = 180

while numero > 10:
    numero = numero / 3
    cuenta += 1
print (cuenta, end='\n')'''


name = "wombat010len"
size = len(name)

i = -1
while i < size -1:
    i = i + 1
    if not name[i].isalpha():
        continue
    print(name[i], end='')

