from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

links = ["http://guba.eastmoney.com/"]


def get_all_link(url):
    html = urlopen(url)
    bso = BeautifulSoup(html, "html.parser")
    for link in bso.findAll("a"):
        if "href" in link.attrs:
            # print("This is a newly appended URL"+ link.attrs["href"] )
            links.append(link.attrs["href"])


while len(links) > 0:
    links = [link for link in links if link is not None and "http" in link]
    new_page_url = links[random.randint(0,len(links)-1)]
    get_all_link(new_page_url)
    print("We start with a randomly choosen page to begin our next search" + new_page_url )

get_all_link("http://guba.eastmoney.com/")
