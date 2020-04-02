from urllib.request import urlopen
from urllib.error import  HTTPError,URLError
from bs4 import  BeautifulSoup

def get_page_title(url):
    """
    各种的提前可能想到的错误
    :param url:
    :return:
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bso = BeautifulSoup(html.read())
        title = bso.title
    except AttributeError as e:
        return  None
    return title

title = get_page_title("https://bj.lianjia.com/")
#title = get_page_title("https://baidu.com/")
#title = get_page_title("https://163.com/")

if title is None:
    print("哈哈哈没爬到")
else:
    print(title)


