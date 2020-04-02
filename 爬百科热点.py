from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://baike.sogou.com')
bso = BeautifulSoup(html,"html.parser")

a_list = bso.findAll("")
for i in a_list:
    print(i)
