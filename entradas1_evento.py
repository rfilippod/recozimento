import xml.etree.ElementTree as ET
import entradas1_recurso as r

root = ET.parse('BrazilInstance1.xml')
#root = ET.parse('ItalyInstance1.xml')

idCourse = []
idEventGroup = []
idEvent = []
referenceResourceType = []

for xml in root.findall('./Instances/Instance/Events/EventGroups/Course'):
    idCourse.append(xml.attrib.get('Id'))

for xml in root.findall('./Instances/Instance/Events/EventGroups/EventGroup'):
    idEventGroup.append(xml.attrib.get('Id'))

duration = []
course = []
idDuration = {}
teste3 = {}
x = 0
resourceReference = []
for xml in root.findall('./Instances/Instance/Events/Event'):
    resourceRefrence = []
    #x = 0
    teste3 = {}
    course = []
    duration = []
    resourceReference = []
    idEvent.append(xml.attrib.get('Id'))
    keyIdEvent = xml.attrib.get('Id')
    #print(idEvent)
    duration.append(xml.find('Duration').text)
    course.append(xml.find('Course').attrib.get('Reference'))
    resourceReference.append(xml.find('Resources/Resource').attrib.get('Reference'))
    k = []
    k = [x.attrib for x in xml.findall('Resources/Resource')]
    teste3['duration'] = duration
    teste3['course'] = course
    teste3['resourceReference'] = k
    idDuration[keyIdEvent] = teste3

# print(f'\no duration é {duration}\n')
# print(f'\no course é {course}\n')
# print(f'\no idDuration é {idDuration}\n')
#
#
#
# print(f'id Course {idCourse}\n')
# print(f'id event group {idEventGroup}\n')
# print(f'id event {idEvent}\n')

# for i in range (len(idEvent)):
#     print(idDuration[idEvent[i]]['resourceReference'], end="")
#
# print(r.idResourceType[0])





