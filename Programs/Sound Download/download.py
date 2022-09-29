import requests
import urllib3.request
import re
from bs4 import BeautifulSoup as bs
import time

links =  open("/Users/alexjshepler/Desktop/Epoch Industry/Programs/Sound Download/links.txt", 'r')

for line in links.readlines():
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
    headers = {'User-Agent': user_agent}
    r = requests.get(requests.get(line, headers=headers).url, headers=headers)

    download = re.search("http.*(.+?)\.mp3", r.text)

    print(download.group(1))
    break;