import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')  # Parse a file
root = tree.getroot()
# Add an attrib 
root.set('key', 'value') 

# Del an attrib
del(root.attrib['key'])

# Save changes 
tree.write('data.xml')
print(root.attrib)

# Loop every tag in the file

for element in root:
    print(element.tag, element.attrib)

lista = [(element.tag, element.attrib) for element in root.iter() ]  # List of all elements and their attribs
print(lista)

# List all movies

for movie in root.iter('movie'):
    print(movie.attrib)

# Covert all to string

xml_string = str(ET.tostring(root))
# print(xml_string)

with open('string.txt', 'w') as file:
    file.write(xml_string)
    file.close()

