from itertools import groupby
from entradas1_recurso import *
import random
import numpy as np
from entradas1_semana import *
from entradas1_evento import *


evento = dict.fromkeys(idResourceGroup)

print(evento)

# print(referenceResourceGroup)

final =[list(referenceResourceGroup) for q, referenceResourceGroup in groupby(referenceResourceGroup)]

y = 0
i = 0
j = 0
lista_teste = []
#
# print(f' final {final}')
for i in range(len(final)):
    for j in range(len(final[i])):
        lista_teste.append(idResource[y])
        if len(lista_teste) == len(final[i]):
            evento[final[i][0]] = lista_teste
            lista_teste = []
        y += 1

# print(evento)


#montando horario

qtd_classes = len(evento[idResourceGroup[1]])

# print(qtd_classes)

turma = []

matriz_horario = np.full((linha_semana, coluna_semana), 'aaaaaaaa')
dict_matriz = {}
str1 = []
duracao = []
for i in range(len(idEvent)):
    str1.append(''.join(idDuration[idEvent[i]]['duration']))
    duracao.append(int(str1[i]))

aulas = []
for i in range(len(idEvent)):
    for j in range(duracao[i]):
        aulas.append(idEvent[i])
x = 0
# print(f'aulas {aulas}\n')

listona = []

for z in range(qtd_classes):
    matriz_horario = np.full((linha_semana, coluna_semana), 'aaaaaaaa')
    listona = []
    for i in range(coluna_semana):
        for j in range(linha_semana):
            matriz_horario[j][i] = aulas[x]
            # print(matriz_horario)
            x += 1
    dict_matriz[z] = matriz_horario
    # print(dict_matriz)

# print(dict_matriz)
