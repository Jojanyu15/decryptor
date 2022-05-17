monograms = {}
with open("ngrams/english_monograms.txt") as f:
    monograms = dict([line.split() for line in f])

bigrams = {}
with open("ngrams/english_bigrams.txt") as f:
    bigrams = dict([line.split() for line in f])

trigrams = {}
with open("ngrams/english_trigrams.txt") as f:
    trigrams = dict([line.split() for line in f])

quadgrams = {}
with open("ngrams/english_quadgrams.txt") as f:
    quadgrams = dict([line.split() for line in f])


def obtener_cantidad_monogramas(mensaje):
    letras_dic = dict()  # Guarda repetición de letras
    contador = 0  # Caracteres que se repiten
    for letra in mensaje:  # Por cada letra
        if letra in letras_dic:  # Si ya estaba en el dic() significa que se repite
            if letras_dic[letra] == 1:
                contador += 1  # Se agrega al contador
            letras_dic[letra] += 1  # Continua el conteo
        else:
            # Si la letra no esta en el diccionario, la ag
            letras_dic[letra] = 1
    return dict(sorted(letras_dic.items(), key=lambda x: x[1], reverse=True))


def obtener_cantidad_biagramas(mensaje):
    cantidad_bigramas = dict()  # Creo el diccionario
    # Uno el mensaje encriptado junto con el mismo mensaje con un string faltante para garantizar todas las combinaciones
    msg = mensaje
    msg_splitted = mensaje[1:]

    bigramas_del_mensaje = [msg[i:i+2] for i in range(0, len(msg), 2)]
    bigramas_del_mensaje.__add__([msg_splitted[i:i+2]
                                  for i in range(0, len(msg_splitted), 2)])

    for bigrama in bigramas_del_mensaje:
        if bigrama in cantidad_bigramas:  # Si ya estaba en el dic() significa que se repite
            cantidad_bigramas[bigrama] += 1  # Continua el conteo
        else:
            # Si la letra no esta en el diccionario, la agrega
            cantidad_bigramas[bigrama] = 1

    return dict(sorted(cantidad_bigramas.items(), key=lambda x: x[1], reverse=True))


def obtener_cantidad_trigramas(mensaje):
    cantidad_trigramas = dict()  # Creo el diccionario
    # Uno el mensaje encriptado junto con el mismo mensaje con un string faltante para garantizar todas las combinaciones
    msg = mensaje
    msg_splitted_1 = mensaje[1:]
    msg_splitted_2 = mensaje[2:]

    # Creamos un diccionario de trigramas con todas las posibles combinaciones de letras de a 3
    trigramas_del_mensaje = [msg[i:i+3] for i in range(0, len(msg), 3)]
    trigramas_del_mensaje_1 = [msg_splitted_1[i:i+3]
                               for i in range(0, len(msg_splitted_1), 3)]
    trigramas_del_mensaje_2 = [msg_splitted_2[i:i+3]
                               for i in range(0, len(msg_splitted_2), 3)]
    trigramas_del_mensaje = trigramas_del_mensaje.__add__(
        trigramas_del_mensaje_1)
    trigramas_del_mensaje = trigramas_del_mensaje.__add__(
        trigramas_del_mensaje_2)

    for trigrama in trigramas_del_mensaje:
        if trigrama in cantidad_trigramas:  # Si ya estaba en el dic() significa que se repite
            cantidad_trigramas[trigrama] += 1  # Continua el conteo
        else:
            # Si la letra no esta en el diccionario, la agrega
            cantidad_trigramas[trigrama] = 1

    return dict(sorted(cantidad_trigramas.items(), key=lambda x: x[1], reverse=True))


def obtener_cantidad_cuagramas(mensaje):
    cantidad_cuagramas = dict()  # Creo el diccionario
    # Uno el mensaje encriptado junto con el mismo mensaje con un string faltante para garantizar todas las combinaciones
    msg = mensaje + mensaje[:1]
    msg_splitted_1 = mensaje[1:] + mensaje[:2]
    msg_splitted_2 = mensaje[2:] + mensaje[:3]
    msg_splitted_3 = mensaje[3:]

    # Creamos un diccionario de cuagramas con todas las posibles combinaciones de letras de a 4
    cuagramas_del_mensaje = [msg[i:i+4] for i in range(0, len(msg), 4)]
    cuagramas_del_mensaje_1 = [msg_splitted_1[i:i+4]
                               for i in range(0, len(msg_splitted_1), 3)]
    cuagramas_del_mensaje_2 = [msg_splitted_2[i:i+4]
                               for i in range(0, len(msg_splitted_2), 4)]
    cuagramas_del_mensaje_3 = [msg_splitted_2[i:i+4]
                               for i in range(0, len(msg_splitted_3), 4)]

    cuagramas_del_mensaje = cuagramas_del_mensaje.__add__(
        cuagramas_del_mensaje_1)
    cuagramas_del_mensaje = cuagramas_del_mensaje.__add__(
        cuagramas_del_mensaje_2)
    cuagramas_del_mensaje = cuagramas_del_mensaje.__add__(
        cuagramas_del_mensaje_3)

    for cuagrama in cuagramas_del_mensaje:
        if cuagrama in cantidad_cuagramas:  # Si ya estaba en el dic() significa que se repite
            cantidad_cuagramas[cuagrama] += 1  # Continua el conteo
        else:
            # Si la letra no esta en el diccionario, la agrega
            cantidad_cuagramas[cuagrama] = 1

    return dict(sorted(cantidad_cuagramas.items(), key=lambda x: x[1], reverse=True))
