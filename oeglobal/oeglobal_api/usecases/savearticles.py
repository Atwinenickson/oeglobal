import requests
from bs4 import BeautifulSoup
from oeglobal_api.usecases.article import get_articles
from oeglobal_api.usecases.posturls import get_urls
import json
import sqlite3
from pathlib import Path
import random
from multiprocessing import connection
from datetime import datetime
import re


class OeglobalNewsDetail:
    def __init__(self, url):
        self.url = url
        self.connection = sqlite3.connect(
            "/home/atwine/nickson/Work/oeglobal/oeglobal/db.sqlite3"
        )
        self.connection.row_factory = lambda cursor, row: row[0]
        self.cursor = self.connection.cursor()
        self.detail = {}

    def OeglobalData(self):
        pagelinks = get_urls(self.url)
        for link in pagelinks:
            dictironaryData = get_articles(link)[0]
            dictironaryTopics = get_articles(link)[1]
            dictironaryUrls = get_articles(link)[2]
            self.SaveToDatabase(dictironaryData, dictironaryTopics, dictironaryUrls)

    def SaveToDatabase(self, dictironaryData, dictironaryTopics, dictironaryUrls):
        randomNumber = random.randint(1, 1000)
        topicurls = dictironaryUrls["TopicUrls"]

        topic = dictironaryTopics["Topics"]

        title = dictironaryData["Title"]
        replies = dictironaryData["Replies"]
        views = dictironaryData["Views"]
        date = dictironaryData["Date"]
        articleurl = dictironaryData["ArticleUrl"]

        result = self.connection.execute(
            "select url from oeglobal_api_article where url = ?",
            (articleurl,),
        )
        result = result.fetchall()
        print("result")
        print(result)
        print("result")
        if len(result) > 0:
            print("Article exists")
        else:
            self.connection.execute(
                "insert into oeglobal_api_article values(?,?,?,?,?,?)",
                [None, title, articleurl, replies, views, date],
            )
            self.connection.commit()

        for data in topic:
            result1 = self.connection.execute(
                "select topic from oeglobal_api_topic where topic = ?", [data]
            )
            result1 = result1.fetchall()

            result3 = self.connection.execute(
            "select id from oeglobal_api_article where url = ?",
            (articleurl,),)
            result3 = result3.fetchall()

            # print('result3id')
            # print(result3[0])

            if len(result1) > 0:
                print("Topic Exists")
            else:
                self.connection.execute(
                    "insert into oeglobal_api_topic values(?,?,?)",
                    [None, data,result3[0] ],
                )
                self.connection.commit()

        for topicurl in topicurls:
            result2 = self.connection.execute(
                "select url from oeglobal_api_topicurl where url = ?",
                [topicurl],
            )
            result2 = result2.fetchall()

            result4 = self.connection.execute(
                "select id from oeglobal_api_topic where topic = ?",
                [data],
            )
            result4 = result4.fetchall()

            print('result4id')
            print(result4)

            if len(result2) > 0:
                print("Topic URL exists")
            else:
                self.connection.execute(
                    "insert into oeglobal_api_topicurl values(?,?,?)",
                    [None, topicurl, result4[0]],
                )
                self.connection.commit()


# OeglobalNewsDetail("https://connect.oeglobal.org/").OeglobalData()
