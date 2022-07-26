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
import re

class OeglobalNewsDetail:
    def __init__(self,url):
        self.url = url
        self.connection = sqlite3.connect('/home/atwine/nickson/Work/oeglobal/oeglobal/db.sqlite3')
        self.cursor = self.connection.cursor()
        self.detail={}

    def OeglobalData(self):
        pagelinks = get_urls(self.url)
        for link in pagelinks:
            dictironaryData = get_articles(link)[0]
            dictironaryTopics = get_articles(link)[1]
            dictironaryUrls = get_articles(link)[2]
            self.SaveToDatabase(dictironaryData, dictironaryTopics, dictironaryUrls)
        

    def SaveToDatabase(self,dictironaryData, dictironaryTopics, dictironaryUrls):
        randomNumber = random.randint(1,1000)
        topicurls = dictironaryUrls['topic_urls']
        topicurlid = dictironaryUrls['id']

        topic = dictironaryTopics['topics']
        topicid = dictironaryTopics['id']
        
        articleid = dictironaryData['id']
        title = dictironaryData['title']
        replies = dictironaryData['replies']
        views = dictironaryData['views']
        date = dictironaryData['date']
        articleurl = dictironaryData['article_url']

        result = self.connection.execute("select Articleurl from oeglobal_api_article where Articleurl = ?", (articleurl,))
        result=result.fetchall()
        print('result')
        print(result)
        print('result')
        if len(result) > 0:
            print('Article exists')
        else:
            self.connection.execute('insert into oeglobal_api_article values(?,?,?,?,?,?,?)',[None, articleid, title, articleurl, replies, views, date])
            self.connection.commit()

        for data in topic:
            result1 = self.connection.execute("select topic from oeglobal_api_topic where Topic = ?", [data])
            result1=result1.fetchall()
            if len(result1) > 0 :
                print('Topic Exists')
            else:
                self.connection.execute('insert into oeglobal_api_topic values(?,?,?,?)',[None, topicid , data, articleid])
                self.connection.commit()
        
        for topicurl in topicurls:
            result2 = self.connection.execute('select topicurl from oeglobal_api_topicurl where TopicUrl = ?', [topicurl])
            result2=result2.fetchall()
            if len(result2) > 0 :
                print('Topic URL exists')
            else:
                self.connection.execute('insert into oeglobal_api_topicurl values(?,?,?,?)',[None, topicurlid , topicurl, topicid])
                self.connection.commit()



OeglobalNewsDetail('https://connect.oeglobal.org/').OeglobalData()