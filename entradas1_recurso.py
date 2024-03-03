import xml.etree.ElementTree as ET

# root = ET.parse('FinlandCollege.xml')
# root = ET.parse('ItalyInstance1.xml')
root = ET.parse('BrazilInstance1.xml')

idResourceType = []
idResourceGroup = []
idResource = []
referenceResourceType = []
referenceResourceGroup = []
time = {}
x = 0

for xml in root.findall('./Instances/Instance/Resources/ResourceTypes/ResourceType'):
    idResourceType.append(xml.attrib.get('Id'))

for xml in root.findall('./Instances/Instance/Resources/ResourceGroups/ResourceGroup'):
    idResourceGroup.append(xml.attrib.get('Id'))

for xml in root.findall('./Instances/Instance/Resources/Resource'):
    idResource.append(xml.attrib.get('Id'))

for xml in root.findall('./Instances/Instance/Resources/Resource/ResourceType'):
    referenceResourceType.append(xml.attrib.get('Reference'))

for xml in root.findall('./Instances/Instance/Resources/Resource/ResourceGroups/ResourceGroup'):
    referenceResourceGroup.append(xml.attrib.get('Reference'))


# print(f'id resource type: {idResourceType}\n')
# print(f'id resource group: {idResourceGroup}\n')
# print(f'id resource: {idResource}\n')
# print(f'reference resource type: {referenceResourceType}\n')
# print(f'reference resource group: {referenceResourceGroup}\n')

# for i in range (len(idResource)):
#     for j in range (len(idResourceType)):
#         if referenceResourceType[i] == idResourceType[j]:
#             print(f'o {idResource[i]} é um {idResourceType[j]}')
#         if referenceResourceGroup[i] == idResourceGroup[j]:
#             print(f'o {idResource[i]} pertence ao grupo {idResourceGroup[j]}')

