from bs4 import BeautifulSoup
import requests

response=requests.get('https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/')
contents=response.text

soup=BeautifulSoup(contents,'html.parser')
print(soup.title)
