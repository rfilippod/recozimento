import numpy as np
import copy
import random
import math
import re
from entradas1_recurso import *


"""
        ----------------------------------------------------------------------------------------------------------------
        Aqui é realizada a leitura do arquivo XHSTT e, a partir dele, inserido na matriz de maneira aleatória os eventos
        (por exemplo T1-S1).
        A leitura é realizada a partir da função element tree.parse, onde é pegado o 'root' do arquivo, feito isso, 
        encontra-se todos as ocorrencias dentro da tag eventos no XHSTT, após isso, os eventos são inseridos nas 
        matrizes correspondentes. 
        ----------------------------------------------------------------------------------------------------------------
        Variáveis
        ----------------------------------------------------------------------------------------------------------------
        eventoGr: dicionario que recebe os eventos do XHSTT
        ----------------------------------------------------------------------------------------------------------------
        duracao: recebe a duração de cada evento
        ----------------------------------------------------------------------------------------------------------------
        lista e lista1 recebe a conversão para lista de eventoGr e duracao, respectivamente
        ----------------------------------------------------------------------------------------------------------------
        matriz_horarioS1, matriz_horarioS2 e matriz_horarioS3: inicilização das matrizes que irão receber os eventos,
        cada uma recebe a matriz correspondente ao seu horario
        ----------------------------------------------------------------------------------------------------------------
        dict_matriz é o dicionario final das matrizes
        ----------------------------------------------------------------------------------------------------------------
"""

import xml.etree.ElementTree as ET

def entrada():
    evento = dict.fromkeys(idResourceGroup)

    print(f' from keys {evento}')
    root = ET.parse('BrazilInstance1.xml')


    eventoGr = {}
    duracao = {}
    x = 0

    for xml in root.findall('./Instances/Instance/Events/Event'): #realizando a leitura do arquivo xhstt

        eventoGr[x] = xml.attrib.get('Id')
        duracao[x] = xml[1].text #lendo as tags e inserindo em variáveis para utilização no programa

        x += 1


    lista = list(eventoGr.values()) #convertendo esses valores, que são dados em dicionário, para lista
    lista1 = list(duracao.values()) #para melhorar o manuseio
    mylist = []
    y = 0

    for x in range(len(lista)):
        aux = []
        aux.append(lista[x])
        while y < int(lista1[x]): #inserindo no vetor todas as diciplinas, de acordo com a duração dela
            mylist.append(aux[0]) #se uma disciplina possui carga horaria de 5, são inseridas 5 disciplinas
            y += 1
        y = 0
    idDia = []
    idTime = []
    timetable_entrada = np.array(mylist) #conversão para um array de numpy

    for xml in root.findall('./Instances/Instance/Times/Time'):
        idDia.append(xml.attrib.get('Id'))

    for xml in root.findall('./Instances/Instance/Times/TimeGroups/Day'):
        idTime.append(xml.attrib.get('Id'))

    coluna_semana = len(idTime)
    linha_semana = len(idDia) // coluna_semana

    matriz_horarioS1 = np.full((linha_semana, coluna_semana), 'aaaaaaaa')
    matriz_horarioS2 = np.full((linha_semana, coluna_semana), 'aaaaaaaa')
    matriz_horarioS3 = np.full((linha_semana, coluna_semana), 'aaaaaaaa')
    matriz_horarioS4 = np.full((linha_semana, coluna_semana), 'aaaaaaaa')
    matriz_horarioS5 = np.full((linha_semana, coluna_semana), 'aaaaaaaa')
    matriz_horarioS6 = np.full((linha_semana, coluna_semana), 'aaaaaaaa')


    entrada1 = []
    entrada2 = []
    entrada3 = []
    entrada4 = []
    entrada5 = []
    entrada6 = []
    rand = random.sample(range(len(mylist)), (len(mylist))) #respeitando a semente, fazendo uma aleatoriedade mais controlada
    for x in range(len(mylist)):
        if re.search('\\bS1\\b', timetable_entrada[rand[x]], re.IGNORECASE): #verifica se a String possui S1, S2 OU S3 e
            entrada1.append(timetable_entrada[rand[x]])              #insere no devido entrada
        elif re.search('\\S2\\b', timetable_entrada[rand[x]], re.IGNORECASE):
            entrada2.append(timetable_entrada[rand[x]])
        elif re.search('\\S3\\b', timetable_entrada[rand[x]], re.IGNORECASE):
            entrada3.append(timetable_entrada[rand[x]])
        elif re.search('\\S4\\b', timetable_entrada[rand[x]], re.IGNORECASE):
            entrada4.append(timetable_entrada[rand[x]])

    entrada = entrada1 + entrada2 + entrada3 + entrada4
    # print(entrada1)
    # print(len(entrada2))
    # print(entrada2)
    # print(entrada3)
    # print(f' entrada 4 {entrada4}')
    o = 0
    for i in range(len(matriz_horarioS1)):
        for j in range(len(matriz_horarioS1)):
            matriz_horarioS1[j][i] = entrada[o]  #inserindo o cromossono na matriz de horario, matriz da turma 1
            o = o + 1


    o = 25
    for i in range(len(matriz_horarioS2)):
        for j in range(len(matriz_horarioS2)):
            matriz_horarioS2[j][i] = entrada[o]  #inserindo o cromossono na matriz de horario, matriz da turma 2
            o = o + 1

    #print(matriz_horarioS1)
    #print(matriz_horarioS2)
    o = 50
    for i in range(len(matriz_horarioS3)):
        for j in range(len(matriz_horarioS3)):
            matriz_horarioS3[j][i] = entrada[o]  #inserindo o cromossono na matriz de horario, matriz da turma 3
            o = o + 1

    if entrada4:
        o = 0
        for i in range(len(matriz_horarioS4)):
            for j in range(len(matriz_horarioS4)):
                matriz_horarioS4[j][i] = entrada4[o]  # inserindo o cromossono na matriz de horario, matriz da turma 4
                o = o + 1
                if o == 18:
                    o = 0

    dict_matriz = {}

    dict_matriz[0] = matriz_horarioS1
    dict_matriz[1] = matriz_horarioS2
    dict_matriz[2] = matriz_horarioS3
    if entrada4:
        dict_matriz[3] = matriz_horarioS4
    return dict_matriz




