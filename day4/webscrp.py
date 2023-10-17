from bs4 import BeautifulSoup
import requests
responses=requests.get('https://news.ycombinator.com/')
contents=responses.text

soup=BeautifulSoup(contents,'html.parser')
heading_list=[]
headings=soup.find_all(class_='titleline')
for heading in headings:
    heading_list.append(heading.text)
print('All headings:')
for i in heading_list:
    print(i)
print('\n')
scores=soup.find_all(class_='score')
score_list=[]
for score in scores:
    score_list.append(score.text)
print("All scores:")
for i in score_list:
    print(i)
print('\n')
link_list=[]
alllinks=soup.find_all('span',class_='titleline')
for links in alllinks:
    link=links.find_all('a')
    for l in link:
        url=l.get('href')
        link_list.append(url)
print("All links:")
for i in link_list:
    print(i)