import xml.etree.ElementTree as ET
import re
tree = ET.parse("data.xml")
root = tree.getroot()



movie_back_2_future = root.find("./genre/decade/movie/[@title='Back 2 the Future']")
movie_back_2_future.attrib['title'] = 'Back to the Future'
print(movie_back_2_future.attrib)


tree.write("data.xml")
tree = ET.parse("data.xml")
root = tree.getroot()

for movie in root.findall("./genre/decade/movie/format"):
    match = re.search(',', movie.text)
    if match:
        movie.set('multiple', 'Yes')
    else:
        movie.set('multiple', 'No')
    
    tree.write('data.xml')

tree = ET.parse("data.xml")
root = tree.getroot()

for movie in root.findall('./genre/decade/movie/format'):
    print(movie.attrib)




