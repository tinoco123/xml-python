import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')  # Parse a file
root = tree.getroot()
print(root.attrib)

for child in root:
    print(child.tag, child.attrib, child.text, child.tail)

list_elements = [elem.tag for elem in root.iter()]  # Print all tags

print(list_elements)

display_all_elements = ET.tostring(root)

print(display_all_elements)

for description in root.iter('description'):
    print(description.attrib)

for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    print(movie.attrib, movie.text)

for movie in root.findall('./genre/decade/movie/[year="2000"]'):
    print(movie.attrib['title'])