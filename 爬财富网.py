from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.eastmoney.com/')
bso = BeautifulSoup(html , "html.parser")

for child in bso.find("div",{"class":"nlist"}).descendants:
    print(child)
