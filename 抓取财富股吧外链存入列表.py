from urllib.request import  urlopen
from bs4 import  BeautifulSoup
import random

links = ["http://guba.eastmoney.com/"]

def get_all_link(url):

    html = urlopen(url)
    bso = BeautifulSoup(html,"html.parser")
    for link in bso.findAll("a"):
        if "href" in link.attrs:
            print("This is a newly appended URL"+ link.attrs["href"] )
            links.append(link.attrs["href"])



get_all_link("http://guba.eastmoney.com/")