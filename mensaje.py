import math
import re
import diccionario as dict_l
import random

message = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34.48)4‡;161;:188;‡?;"

# Obtenemos los diccionarios de monogramas, bigramas, trigramas, cuagramas y palabras para descifrarlo.
monograms = dict_l.monograms
bigrams = dict_l.bigrams
trigrams = dict_l.trigrams
quadgrams = dict_l.quadgrams
words = dict_l.words

# Obtenemos bigramas trigramas cuagramas del mensaje
cantidades_de_caracteres = dict_l.obtener_cantidad_monogramas(message)
cantidad_bigramas = dict_l.obtener_cantidad_biagramas(message)
cantidad_trigramas = dict_l.obtener_cantidad_trigramas(message)
cantidad_cuagramas = dict_l.obtener_cantidad_cuagramas(message)

# Declaración de diccionario de probabiliades
probabilidad = dict()
# Declaración de diccionario de promedios
promedios = dict()

valor_maximo_monograma = 0
valor_maximo_mensaje = 0

#Reemplazamos los primeros bigrmaas en el texto con simbolos
def reemplazar_primeros_bigramas():
    global message
    # Obtenemos el primer bigrama más concurrente en inglés y reemplazamos
    # Cabe aclarar que es necesario limpiar la lista de caracteres del texto y monogramas
    # Debido a que ya han sido reemplazados en el texto

    primer_bigrama = (list(bigrams)[0][0], list(bigrams)[0][1])
    message = message.replace(list(cantidad_bigramas.keys())[0][0], primer_bigrama[0])
    message = message.replace(list(cantidad_bigramas.keys())[0][1], primer_bigrama[1])
    monograms.pop(primer_bigrama[0])
    monograms.pop(primer_bigrama[1])
    cantidades_de_caracteres.pop(next(iter(cantidad_bigramas))[0])
    cantidades_de_caracteres.pop(next(iter(cantidad_bigramas))[1])

    print("\n Obteniendo el primer bigrama (TH) \n Resultado: {}".format(message))
    # Obtenemos el segundo bigrama más concurrente en inglés y reemplazamos
    # Cabe aclarar que es necesario limpiar la lista de caracteres del texto y monogramas
    # Debido a que ya han sido reemplazados en el texto
    segundo_bigrama = (list(bigrams)[1][0], list(bigrams)[1][1])
    message = message.replace(list(cantidad_bigramas.keys())[4][0], segundo_bigrama[0])
    message = message.replace(list(cantidad_bigramas.keys())[4][1], segundo_bigrama[1])
    monograms.pop(segundo_bigrama[0])
    monograms.pop(segundo_bigrama[1])
    #print(cantidad_bigramas.keys())
    cantidades_de_caracteres.pop(list(cantidad_bigramas.keys())[2][0])
    cantidades_de_caracteres.pop(list(cantidad_bigramas.keys())[2][1])
    print("\n Obteniendo el segundo bigrama (IN) \n Resultado: {}".format(message))
    print("\n")


# Esta funcion calcula las probabilidades de un caracter de aparecer en el mensaje
def calcular_probabilidades():
    for key, value in cantidades_de_caracteres.items():
        probabilidad[key] = (value / len(message))*100

# Esta funcion asimila las probabilidades con los promedios de el listado de monogramas en ingles 
# (ver englis_monograms.txt) a partir de una regla de tres
def recalcular_promedios():
    global valor_maximo_monograma
    global valor_maximo_mensaje
    valor_maximo_monograma = max(list(monograms.values()), key=int)
    valor_maximo_mensaje = max(list(probabilidad.values()), key=int)

    for key, value in probabilidad.items():
        promedios[key] = (value * float(valor_maximo_monograma)) / \
            valor_maximo_mensaje

# Esta funcion reemplaza las letras en un rango de tolerancia
# Restando el diccionario de promedios con el score del diccionario de monogramas
# Si la resta entre estos dos es menor a la tolerancia se realiza el reemplazo de 
# Este caracter por el correspondinete, esta parte sería la sustitución por
# Análisis de frecuencias.
def reemplazar_letras(tolerancia):
    global message
    for key, value in promedios.copy().items():
        for k, v in monograms.copy().items():
            calculation = abs(float(v) - value)
            if(calculation < tolerancia):
                if(not k in message and key in promedios):
                    message = message.replace(key, k)
                    promedios.pop(key)
                    probabilidad.pop(key)
                    monograms.pop(k)


# Realizamos una iteración para reemplazar los huecos faltantes por palabras
# Teniendo en cuenta que una vez entendemos las palabras faltantes realizamos
# Una especie de ataque de fuerza bruta que reemplaza aleatoriamente los caracteres
# faltantes con los monogramas sobrantes y aumenta un score. Si el score es mayor o
# igual a 5 (la cantidad de palabras faltantes en este caso) terminará el ciclo y 
# nos retornará el mensaje.
def iterar_y_reemplazar():
    global message

    # declaración de score
    points = 0
    # Index usado para reemplazar
    index = 0
    # Copia del mensaje 
    message_copy = message
    # Cantidad de iteraciones
    iterations = 0
    found = False
    while (not found):
        key_base = list(monograms.keys())
        random.shuffle(key_base)
        key_base = key_base[:len(promedios)]
        index = 0
        iterations += 1
        points = 0

        for key in key_base:
            message_copy = message_copy.replace(list(promedios.keys())[index], key)
            index += 1
        for key, value in words.items():
            if(re.search(key, message_copy)):
                points += 1
        if(points >= 5):
            message = message_copy
            found = True

        message_copy = message
    print("\n\nEncontrado despues de {} iteraciones".format(iterations))


if __name__ == '__main__':

    reemplazar_primeros_bigramas()

    calcular_probabilidades()
    recalcular_promedios()


    reemplazar_letras(100)
    print("\n\nPrimer reemplazo de letras con una tolerancia de 100:\n {}".format(message))

    recalcular_promedios()
    reemplazar_letras(100)
    print("\n\nSegundo reemplazo de letras con una tolerancia de 100\n {}".format(message))


    recalcular_promedios()
    reemplazar_letras(300)
    print("\n\nTercer reemplazo de letras con una tolerancia de 300\n {}".format(message))


    recalcular_promedios()
    reemplazar_letras(100)
    print("\n\nCuarto reemplazo de letras con una tolerancia de 100\n {}".format(message))


    iterar_y_reemplazar()
    print("El mensaje descifrado es:\n" + message)