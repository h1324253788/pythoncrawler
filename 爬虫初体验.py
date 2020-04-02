from urllib.request import urlopen
from urllib.error import  HTTPError,URLError
from bs4 import  BeautifulSoup
try:
    html = urlopen("https://bj.lianjia.com/")
    bso = BeautifulSoup(html.read())
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    print("It worked!!! NO Error!!!OMG~")
    print(bso.h1)