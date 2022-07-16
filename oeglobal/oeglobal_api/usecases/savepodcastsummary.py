import requests
from bs4 import BeautifulSoup
from podcast import get_podcast
from podcasturls import get_podcasturl
import json
import sqlite3
from pathlib import Path
import random
from multiprocessing import connection
import re


class OeglobalPodcastDetail:
    def __init__(self,url):
        self.url = url
        self.connection = sqlite3.connect('/home/atwine/nickson/Work/oeglobal/oeglobal/db.sqlite3')
        self.cursor = self.connection.cursor()
        self.detail={}

    def OeglobalData(self):
        podcasturls = get_podcasturl(self.url)
        for link in podcasturls:
            dictironaryData = get_podcast(link)
            self.SaveToDatabase(dictironaryData)
        

    def SaveToDatabase(self,dictironaryData):
        podcastid = dictironaryData['ID']
        title = dictironaryData['Title']
        audio = dictironaryData['AudioLink']
        description = dictironaryData['Description']
        date = dictironaryData['Date']

        result = self.connection.execute("select AudioLink from oeglobal_api_singlepodcast where AudioLink = ?", (audio,))
        result=result.fetchall()
        print('result')
        print(result)
        print('result')
        if len(result) > 0:
            print('Podcast exists')
        else:
            self.connection.execute('insert into oeglobal_api_singlepodcast values(?,?,?,?,?,?)',[None, podcastid, title, audio, description, date])
            self.connection.commit()



OeglobalPodcastDetail('https://podcast.oeglobal.org/').OeglobalData()