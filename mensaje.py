import math
import diccionario as dict_l
import random

message = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485)8)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"

# https://www.youtube.com/watch?v=iPymNpwwjtk

monograms = dict_l.monograms
bigrams = dict_l.bigrams
trigrams = dict_l.trigrams
quadgrams = dict_l.quadgrams

cantidades_de_caracteres = dict_l.obtener_cantidad_monogramas(message)
cantidad_bigramas = dict_l.obtener_cantidad_biagramas(message)
cantidad_trigramas = dict_l.obtener_cantidad_trigramas(message)
cantidad_cuagramas = dict_l.obtener_cantidad_cuagramas(message)

# print(cantidad_bigramas)


primer_bigrama = (list(bigrams)[0][0], list(bigrams)[0][1])
message = message.replace(list(cantidad_bigramas.keys())[
                          0][0], primer_bigrama[0])
message = message.replace(list(cantidad_bigramas.keys())[
                          0][1], primer_bigrama[1])
monograms.pop(primer_bigrama[0])
monograms.pop(primer_bigrama[1])
cantidades_de_caracteres.pop(next(iter(cantidad_bigramas))[0])
cantidades_de_caracteres.pop(next(iter(cantidad_bigramas))[1])


segundo_bigrama = (list(bigrams)[1][0], list(bigrams)[1][1])
message = message.replace(list(cantidad_bigramas.keys())[
                          4][0], segundo_bigrama[0])
message = message.replace(list(cantidad_bigramas.keys())[
                          4][1], segundo_bigrama[1])
monograms.pop(segundo_bigrama[0])
monograms.pop(segundo_bigrama[1])
cantidades_de_caracteres.pop(list(cantidad_bigramas.keys())[4][0])
cantidades_de_caracteres.pop(list(cantidad_bigramas.keys())[4][1])


probabilidad = dict()
for key, value in cantidades_de_caracteres.items():
    probabilidad[key] = (value / len(message))*100


valor_maximo_monograma = max(list(monograms.values()), key=int)
valor_maximo_mensaje = max(list(probabilidad.values()), key=int)


promedios = dict()

for key, value in probabilidad.items():
    promedios[key] = (value * float(valor_maximo_monograma)) / \
        valor_maximo_mensaje


index = 0

# print("\n\n")
# print(promedios)
# print("\n\n")
# print(monograms)
# print("\n\n")

for key, value in promedios.copy().items():
    for k, v in monograms.copy().items():
        calculation = abs(float(v) - value)
        if(calculation < 100):
            if(not k in message and key in promedios):
                message = message.replace(key, k)
                promedios.pop(key)
                probabilidad.pop(key)
                monograms.pop(k)


valor_maximo_monograma = max(list(monograms.values()), key=int)
valor_maximo_mensaje = max(list(probabilidad.values()), key=int)

for key, value in probabilidad.items():
    promedios[key] = (value * float(valor_maximo_monograma)) / \
        valor_maximo_mensaje

for key, value in promedios.copy().items():
    for k, v in monograms.copy().items():
        calculation = abs(float(v) - value)
        if(calculation < 100):
            if(not k in message and key in promedios):
                message = message.replace(key, k)
                promedios.pop(key)
                probabilidad.pop(key)
                monograms.pop(k)

valor_maximo_monograma = max(list(monograms.values()), key=int)
valor_maximo_mensaje = max(list(probabilidad.values()), key=int)

for key, value in probabilidad.items():
    promedios[key] = (value * float(valor_maximo_monograma)) / \
        valor_maximo_mensaje

for key, value in promedios.copy().items():
    for k, v in monograms.copy().items():
        calculation = abs(float(v) - value)
        if(calculation < 300):
            if(not k in message and key in promedios):
                message = message.replace(key, k)
                promedios.pop(key)
                probabilidad.pop(key)
                monograms.pop(k)


valor_maximo_monograma = max(list(monograms.values()), key=int)
valor_maximo_mensaje = max(list(probabilidad.values()), key=int)

for key, value in probabilidad.items():
    promedios[key] = (value * float(valor_maximo_monograma)) / \
        valor_maximo_mensaje

for key, value in promedios.copy().items():
    for k, v in monograms.copy().items():
        calculation = abs(float(v) - value)
        if(calculation < 100):
            if(not k in message and key in promedios):
                message = message.replace(key, k)
                promedios.pop(key)
                probabilidad.pop(key)
                monograms.pop(k)

points = 0
index = 0
message_copy = message

for iteration in range(0, 100):
    key_base = list(monograms.keys())
    random.shuffle(key_base)
    key_base = key_base[:len(promedios)]
    print(key_base)
    index = 0
    for key in key_base:
        message_copy = message_copy.replace(list(promedios.keys())[index], key)
        index += 1
    print(message_copy)
    message_copy = message
   # for key, value in trigrams.items():


print("\n\n")
print(promedios)
print("\n\n")
print(monograms)
print("\n\n")

# res_key, res_val = min(monograms.items(), key=lambda x: abs(math.floor(value) - x[1]))
# res_key = list(monograms.keys())[index]
# index += 1
# monograms.pop(res_key)

# print(monograms)
# print(promedios)
print(message)
