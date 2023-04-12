
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

# Show decades and years
for decade in root.findall('./genre/decade'):
    print(decade.attrib)
    for year in decade.findall('./movie/year'):
        print(year.text)

# Show movies of 2000S

for movie in root.findall('./genre/decade/movie/[year="2000"]'):
    print(movie.attrib['title'])

# Add 2000 decade to genre action

action = root.find('./genre[@category="Action"]')
new_decade = ET.SubElement(action, 'decade', {'years': '2000s'})

# Add X-Men movie to 2000s decade and remove it from the 1990s
x_men = root.find("./genre/decade/movie[@title='X-Men']")
decade_2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
decade_2000s.append(x_men)

decade_1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
decade_1990s.remove(x_men)

tree.write('data.xml')
tree = ET.parse('data.xml')
root = tree.getroot()

# Results
print(ET.tostring(root, encoding='utf8').decode('utf8'))