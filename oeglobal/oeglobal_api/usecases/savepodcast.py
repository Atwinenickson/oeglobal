import requests
from bs4 import BeautifulSoup
from podcasts import get_podcast, get_recent_podcast
import json
import sqlite3
from pathlib import Path
import random
from multiprocessing import connection
from datetime import datetime

class OeglobalPodcast:
    def __init__(self):
        self.connection = sqlite3.connect('/home/atwine/nickson/Work/oeglobal/oeglobal/db.sqlite3')
        self.cursor = self.connection.cursor()
        self.detail={}

    def OeglobalData(self):
        dictironaryPodcast = get_podcast()
        dictironaryPodcasturl = get_recent_podcast()
        self.SaveToDatabase(dictironaryPodcast, dictironaryPodcasturl)
            
        

    def SaveToDatabase(self,dictironaryPodcast, dictironaryPodcasturl):
        recentpodcastid = dictironaryPodcasturl['ID']
        recentpodcasttitle = dictironaryPodcasturl['Title']
        recentpodcasturl = dictironaryPodcasturl['RecentPodcasturl']
        recentdate = dictironaryPodcasturl['Date']

        podcastid = dictironaryPodcast['ID']
        title = dictironaryPodcast['Title']
        podcasturl = dictironaryPodcast['Podcasturl']
        comments = dictironaryPodcast['Comments']
        description = dictironaryPodcast['Description']
        date = dictironaryPodcast['Date']

        self.connection.execute('insert into oeglobal_api_podcast values(?,?,?,?,?,?,?)',[None, podcastid, title, podcasturl, comments, description, date])
       
        self.connection.execute('insert into oeglobal_api_recentpodcast values(?,?,?,?,?)',[None, recentpodcastid , recentpodcasttitle, recentpodcasturl, recentdate])
        
        self.connection.commit()



OeglobalPodcast().OeglobalData()