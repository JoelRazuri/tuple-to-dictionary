"""
    Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los 
    primeros elementos de las tuplas, y los valores una lista con los segundos.
    Por ejemplo:
        >>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
        ('Buenos', 'días') ]
        >>> print(tuplas_a_diccionario(l))
        { 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

"""

def tuplas_a_diccionario(lista_tuplas):

    diccionario = {}
    lista = []

    for i in range(0,len(lista_tuplas)):
        
        if not diccionario:
            lista.append(lista_tuplas[i][1])
        
        if lista_tuplas[i][0] in diccionario:
            lista = diccionario[lista_tuplas[i][0]]
            lista.append(lista_tuplas[i][1])
        else:
            lista = []
            lista.append(lista_tuplas[i][1])
        
        diccionario[lista_tuplas[i][0]] = lista

    return(diccionario)


print(tuplas_a_diccionario([('Buenos', 'momentos'), ('Hola', 'don Pepito'), ('Buenos', 'días'), ('Buenas', 'noches'), ('Hola', 'don Jose')]))
