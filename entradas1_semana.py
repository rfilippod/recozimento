
"""two_split = np.array_split(idTimeGroup, len(idTimeGroup))
for array in two_split:
    print(list(array))"""


import xml.etree.ElementTree as ET
import json
import numpy as np

# tree = ET.parse('ItalyInstance1.xml')
tree = ET.parse('BrazilInstance1.xml')
root = tree.getroot()
idTime = []
referenceTimeGroup = []
idDia = []
referenceDay = []
idTimeGroup = []
x = 0

for xml in root.findall('./Instances/Instance/Times/TimeGroups/Day'):
    idTime.append(xml.attrib.get('Id'))


for xml in root.findall('./Instances/Instance/Times/TimeGroups/TimeGroup'):
    idTimeGroup.append(xml.attrib.get('Id'))

# print(idTimeGroup)

idTimeGroup_dict = {}

for i in idTimeGroup:
    idTimeGroup_dict[i] = i



for xml in root.findall('./Instances/Instance/Times/Time'):
    idDia.append(xml.attrib.get('Id'))

for xml in root.findall('./Instances/Instance/Times/Time/Day'):
    referenceDay.append(xml.attrib.get('Reference'))


for xml in root.findall('./Instances/Instance/Times/Time/TimeGroups/TimeGroup'):
    referenceTimeGroup.append(xml.attrib.get('Reference'))

dict_keys = dict.fromkeys(idTime)

# print(dict_keys)

my_dict = {i:referenceDay.count(i) for i in referenceDay}

lista = []
y = 0
# print(my_dict[idTime[0]])
for j in range(len(dict_keys)):
    lista = []
    for i in range(my_dict[idTime[j]]):
        lista.append(idDia[y])
        y += 1
    dict_keys[idTime[j]] = lista

# print(dict_keys)

# print(f'referencia time group {referenceTimeGroup}\n')
# print(f'id dia {idDia}\n')
# print(f'referenceDay {referenceDay}\n')
# print(f'idtime {idTime}\n')
# print(f'id time group {idTimeGroup}\n')
# print(f'id time group dict{idTimeGroup_dict}\n')

coluna_semana = len(idTime)
linha_semana = len(idDia)//coluna_semana


matriz_horarioS1 = np.full((linha_semana, coluna_semana), 'aaaaaaaa')


for i in range(coluna_semana):
    for j in range(linha_semana):
        if (idTime[i] == referenceDay[x]):
            matriz_horarioS1[j][i] = idDia[x]
            x += 1


# print(matriz_horarioS1)
