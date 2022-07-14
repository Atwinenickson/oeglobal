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
        print(dictironaryData)
        topicurls = dictironaryUrls['TopicUrls']
        topicurlid = dictironaryUrls['ID']

        topic = dictironaryTopics['Topics']
        topicid = dictironaryTopics['ID']
        
        articleid = dictironaryData['ID']
        title = dictironaryData['Title']
        replies = dictironaryData['Replies']
        views = dictironaryData['Views']
        date = dictironaryData['Date']
        articleurl = dictironaryData['ArticleUrl']
        # create_table1 = "CREATE TABLE oeglobal_api_articles_54 (ArticleID text y, Title text, ArticleUrl text, Replies text, Views text, Date numeric)"
        # create_table2 = "CREATE TABLE oeglobal_api_topics_54 (TopicID text , Topic text, ArticleID text,  FOREIGN KEY (ArticleID) REFERENCES oeglobal_api_articles_54 (ArticleID) )"
        # create_table3 = "CREATE TABLE oeglobal_api_topicurls_54 (TopicUrlID text , TopicUrl text, TopicID text,  FOREIGN KEY (TopicID) REFERENCES oeglobal_api_topics_54 (TopicID) )"
        # self.connection.execute(create_table1)
        # self.connection.execute(create_table2)
        # self.connection.execute(create_table3)
        self.connection.execute('insert into oeglobal_api_article values(?,?,?,?,?,?,?)',[None, articleid, title, articleurl, replies, views, date])
        for data in topic:
            print(data)
            self.connection.execute('insert into oeglobal_api_topic values(?,?,?,?)',[None, topicid , data, articleid])
        
        for topicurl in topicurls:
            print(topicurl)
            self.connection.execute('insert into oeglobal_api_topicurl values(?,?,?,?)',[None, topicurlid , data, topicid])
        self.connection.commit()



OeglobalNewsDetail('https://connect.oeglobal.org/').OeglobalData()