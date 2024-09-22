def sumador(**kwargs):
    inicial = kwargs['inicial']if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else inicial #denominador ternario
    resultado = 0
    for x in range(inicial, final +1):
        resultado += x
    return resultado



print(sumador(final=15))