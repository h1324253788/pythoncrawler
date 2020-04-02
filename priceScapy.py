import requests
from bs4 import  BeautifulSoup

URL = "https://item.jd.com/100007693298.html?dist=jd"


headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 "
                        # "Safari/537.36",
                        # 'Host':'example.com',
                        # 'Connection': 'keep-alive',
                        # 'Cache-Control': 'max-age=0',
                        # 'Accept': 'text/html, */*; q=0.01',
                        # 'X-Requested-With': 'XMLHttpRequest',
                        # 'DNT': '1',
                        # 'Referer': 'http://example.com/',
                        # 'Accept-Encoding': 'gzip, deflate, sdch',
                        # 'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
                        # 'Accept-Language' : 'en-US,en;q=0.5',
                        # 'DNT' : '1' ,
                        # 'Connection' : 'close'

}

page = requests.get(URL, headers = headers)
soup_obj = BeautifulSoup(page.content,'html.parser')


product_name = soup_obj

print(product_name)
##会出现bug，确认机器人情况