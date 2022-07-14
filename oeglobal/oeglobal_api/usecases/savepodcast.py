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
        for recentpodcast in dictironaryPodcasturl:
            # recentpodcastid = recentpodcast['ID']
            recentpodcasttitle = recentpodcast['Title']
            recentpodcasturl = recentpodcast['RecentPodcasturl']
            recentdate = recentpodcast['Date']
            self.connection.execute('insert into oeglobal_api_recentpodcast values(?,?,?,?)',[None , recentpodcasttitle, recentpodcasturl, recentdate])
            
            self.connection.commit()

        for podcast in dictironaryPodcast:
        # podcastid = dictironaryPodcast['ID']
            title = podcast['Title']
            podcasturl = podcast['Podcasturl']
            comments = podcast['Comments']
            description = podcast['Description']
            date = podcast['Date']

            self.connection.execute('insert into oeglobal_api_podcast values(?,?,?,?,?,?)',[None, title, podcasturl, comments, description, date])
            self.connection.commit()



OeglobalPodcast().OeglobalData()