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

    def OeglobalData(self):
        pagelinks = get_urls(self.url)
        for link in pagelinks:
            dictironaryData = get_articles(link)
            self.SaveToDatabase(dictironaryData)
        

    def SaveToDatabase(self,convertedData):
        randomNumber = random.randint(1,1000)
        id = int(datetime.now().microsecond)+randomNumber
        title = convertedData['Title']
        # create_table = "CREATE TABLE oeglobal_api_articles_18 (Title text)"
        # self.connection.execute(create_table)
        self.connection.execute('insert into oeglobal_api_articles_18 values(?)',[title])
        self.connection.commit()



OeglobalNewsDetail('https://connect.oeglobal.org/').OeglobalData()