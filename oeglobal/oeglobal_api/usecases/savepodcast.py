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
        print(dictironaryPodcast)
        self.SaveToDatabase(dictironaryPodcast, dictironaryPodcasturl)
            
        

    def SaveToDatabase(self,dictironaryPodcast, dictironaryPodcasturl):
        for recent_podcast in dictironaryPodcasturl:
            recent_podcast_title = recent_podcast['title']
            recent_podcast_url = recent_podcast['recent_podcast_url']
            recent_date = recent_podcast['date']
            result = self.connection.execute("select Title from oeglobal_api_recentpodcast where title = ?", (recent_podcast_title,))
            result=result.fetchall()
            if len(result) > 0:
                print('Recent Podcast exists')
            else:
                self.connection.execute('insert into oeglobal_api_recentpodcast values(?,?,?,?)',[None , recent_podcast_title, recent_podcast_url, recent_date])
            
            self.connection.commit()

        for podcast in dictironaryPodcast:
            title = podcast['title']
            podcast_url = podcast['podcast_url']
            comments = podcast['comments']
            description = podcast['description']
            date = podcast['date']

            result1 = self.connection.execute("select podcast_url from oeglobal_api_podcast where podcast_url = ?", (podcast_url,))
            result1=result1.fetchall()
            if len(result1) > 0:
                print('Podcast exists')
            else:
                self.connection.execute('insert into oeglobal_api_podcast values(?,?,?,?,?,?)',[None, title, podcast_url, comments, description, date])
            self.connection.commit()



OeglobalPodcast().OeglobalData()