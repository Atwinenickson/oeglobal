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
            dictironaryData = get_articles(link)[0]
            dictironaryTopics = get_articles(link)[1]
            self.SaveToDatabase(dictironaryData, dictironaryTopics)
        

    def SaveToDatabase(self,dictironaryData, dictironaryTopics):
        randomNumber = random.randint(1,1000)
        print(dictironaryData)
        topic = dictironaryTopics['Topics']
        topicid = dictironaryTopics['ID']
        
        articleid = dictironaryData['ID']
        title = dictironaryData['Title']
        replies = dictironaryData['Replies']
        views = dictironaryData['Views']
        date = dictironaryData['Date']
        articleurl = dictironaryData['ArticleUrl']
        # create_table1 = "CREATE TABLE oeglobal_api_articles_52 (ArticleID text y, Title text, ArticleUrl text, Replies text, Views text, Date numeric)"
        # create_table2 = "CREATE TABLE oeglobal_api_topics_52 (TopicID text , Topic text, ArticleID integer,  FOREIGN KEY (ArticleID) REFERENCES oeglobal_api_articles_51 (ArticleID) )"
        # self.connection.execute(create_table1)
        # self.connection.execute(create_table2)
        self.connection.execute('insert into oeglobal_api_articles_52 values(?,?,?,?,?,?)',[articleid, title, articleurl, replies, views, date])
        for data in topic:
            print(data)
            self.connection.execute('insert into oeglobal_api_topics_52 values(?,?,?)',[topicid , data, articleid])

        # create_table2 = "CREATE TABLE oeglobal_api_topics_8 (TopicID integer primary key AUTOINCREMENT, Topic text ArticleID integer,  FOREIGN KEY (ArticleID) REFERENCES oeglobal_api_articles_30 (ArticleID) )"
        # self.connection.execute(create_table2)
        
        
        # for data in topic:
        #     print(data)
        #     self.connection.execute('insert into oeglobal_api_topics_8 values(?,?)',[None , data])
        self.connection.commit()



OeglobalNewsDetail('https://connect.oeglobal.org/').OeglobalData()