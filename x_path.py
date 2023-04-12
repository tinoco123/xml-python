import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

print("Get movies with ratin PG")
for movie in root.findall("./genre/decade/movie/[rating='PG']"):  # XPATH For tags
    print(movie.attrib)

print("Get movies with multiple format")
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib, movie.tag)