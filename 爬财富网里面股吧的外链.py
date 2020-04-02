from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://guba.eastmoney.com/')
bso = BeautifulSoup(html , "html.parser")

for link in bso.findAll("a"):
     print(link)
     if "href" in link.attrs:
         print(link.attrs)


