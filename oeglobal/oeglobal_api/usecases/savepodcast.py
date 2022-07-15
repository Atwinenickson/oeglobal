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
        self.connection = sqlite3.connect('/mnt/d/Work/Others/Oreg/oeglobal/oeglobal/db.sqlite3')
        self.cursor = self.connection.cursor()
        self.detail={}

    def OeglobalData(self):
        dictironaryPodcast = get_podcast()
        dictironaryPodcasturl = get_recent_podcast()
        print(dictironaryPodcast)
        self.SaveToDatabase(dictironaryPodcast, dictironaryPodcasturl)
            
        

    def SaveToDatabase(self,dictironaryPodcast, dictironaryPodcasturl):
        for recentpodcast in dictironaryPodcasturl:
            recentpodcasttitle = recentpodcast['Title']
            recentpodcasturl = recentpodcast['RecentPodcasturl']
            recentdate = recentpodcast['Date']
            result = self.connection.execute("select recentpodcasturl from oeglobal_api_recentpodcast where RecentPodcasturl = ?", (recentpodcasturl,))
            result=result.fetchall()
            if len(result) > 0:
                print('Article exists')
            else:
                self.connection.execute('insert into oeglobal_api_recentpodcast values(?,?,?,?)',[None , recentpodcasttitle, recentpodcasturl, recentdate])
            
            self.connection.commit()

        for podcast in dictironaryPodcast:
            title = podcast['Title']
            podcasturl = podcast['Podcasturl']
            comments = podcast['Comments']
            description = podcast['Description']
            date = podcast['Date']

            result1 = self.connection.execute("select podcasturl from oeglobal_api_podcast where Podcasturl = ?", (podcasturl,))
            result1=result1.fetchall()
            if len(result1) > 0:
                print('Article exists')
            else:
                self.connection.execute('insert into oeglobal_api_podcast values(?,?,?,?,?,?)',[None, title, podcasturl, comments, description, date])
            self.connection.commit()



OeglobalPodcast().OeglobalData()