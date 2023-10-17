from bs4 import BeautifulSoup
file=open("index.html")
contents=file.read()
print(contents)
file.close()

soup=BeautifulSoup(contents,'html.parser')
print(soup.prettify())
print(soup.title.get_text())
print(soup.find(name='a').get('href'))
print(soup.h3)
print(soup.find_all(name='p'))
links=soup.find_all(name='a')
for i in links:
    print(i.get('href'))
paragraph=soup.find(class_='para')
print(paragraph.get_text())
