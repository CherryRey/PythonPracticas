strPrecio =    input("Precio...: ")
strProvincia = input("Provincia: ")

total = float(strPrecio)
strTotal = ""

if strProvincia == 'VA':
  tasa = total * 0.055
  strTotal = "El subtotal es {:.2f}€\nLa tasa es {:.2f}€\n".format(total, tasa)
  total = total + tasa

strTotal = strTotal + "El total es {:.2f}€".format(total)
print(strTotal)