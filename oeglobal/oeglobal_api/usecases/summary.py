import requests
from bs4 import BeautifulSoup
from article import get_articles
from posturls import get_urls
import json



    



class OeglobalNewsDetail:
    def __init__(self,url):
        self.url = 'https://connect.oeglobal.org/'
        self.connection = sqlite3.connect('/home/atwine/nickson/Work/oeglobal/oeglobal/db.sqlite3')
        self.cursor = self.connection.cursor()
        self.detail={}

    def OeglobalData(self):
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
        self.connection.execute('insert into oeglobal_newsdetail values(?,?)',[id,convertedData])
        self.connection.commit()



dictironaryData = NewsDetail().OeglobalData()
NewsDetail().ConvertToJson(dictironaryData)