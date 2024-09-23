"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it."""

import string

def stringposition(cadena):
    alphabet = list(string.ascii_lowercase)
    cadena = cadena.lower()

    for i in cadena:
        if i in alphabet:
            print(alphabet.index(i)+1)



def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.lower()
    
    result = ""
    for i in text:
        if i in alphabet:
            result += str(alphabet.index(i)+1) + " "
    return result.strip()
        

print(alphabet_position("hola!"))
