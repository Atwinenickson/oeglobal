import requests
from bs4 import BeautifulSoup
from article import get_articles
from posturls import get_urls
import json
import sqlite3
from pathlib import Path
import random
from multiprocessing import connection
from datetime import datetime

class OeglobalNewsDetail:
    def __init__(self,url):
        self.url = url
        self.connection = sqlite3.connect(Path(__file__).resolve().parent.parent / 'db.sqlite3')
        self.cursor = self.connection.cursor()
        self.detail={}

    def OeglobalData(self, url):
        pagelinks = get_urls(url)
        for link in pagelinks:
            dictironaryData = get_articles(link)
            # convertedData=json.dumps(dictironaryData)
            print(dictironaryData)


    def ConvertToJson(self,dictironaryData):
        convertedData=json.dumps(dictironaryData)

        self.SaveToDatabase(convertedData)
        

    def SaveToDatabase(self,convertedData):
        randomNumber = random.randint(1,1000)
        id = int(datetime.now().microsecond)+randomNumber
        self.connection.execute('insert into oeglobal_api_article values(?,?)',[id,convertedData])
        self.connection.commit()



dictironaryData = OeglobalNewsDetail('https://connect.oeglobal.org/').OeglobalData('https://connect.oeglobal.org/')
OeglobalNewsDetail('https://connect.oeglobal.org/').ConvertToJson(dictironaryData)