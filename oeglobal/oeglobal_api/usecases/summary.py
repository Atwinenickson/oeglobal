import requests
from bs4 import BeautifulSoup
from article import get_articles
from posturls import get_urls
import json


baseUrl = 'https://connect.oeglobal.org/'
pagelinks = get_urls(baseUrl)
for link in pagelinks:
    dictironaryData = get_articles(link)
    convertedData=json.dumps(dictironaryData)
    print(convertedData)
    