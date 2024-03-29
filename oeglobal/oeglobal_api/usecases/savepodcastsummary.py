import requests
from bs4 import BeautifulSoup
from oeglobal_api.usecases.podcast import get_podcast
from oeglobal_api.usecases.podcasturls import get_podcasturl
import json
import sqlite3
from pathlib import Path
import random
from multiprocessing import connection
import re


class OeglobalPodcastDetail:
    def __init__(self, url):
        self.url = url
        self.connection = sqlite3.connect(
            "/home/atwine/nickson/Work/OEDELETE/oegsearch/oeglobal/db.sqlite3"
        )
        self.cursor = self.connection.cursor()
        self.detail = {}

    def OeglobalData(self):
        podcasturls = get_podcasturl(self.url)
        for link in podcasturls:
            dictironaryData = get_podcast(link)
            self.SaveToDatabase(dictironaryData)

    def SaveToDatabase(self, dictironaryData):
        title = dictironaryData["Title"]
        audio = dictironaryData["AudioLink"]
        description = dictironaryData["Description"]
        date = dictironaryData["Date"]

        result = self.connection.execute(
            "select audio_link from oeglobal_api_singlepodcast where audio_link = ?",
            (audio,),
        )
        result = result.fetchall()
        print("result")
        print(result)
        print("result")
        if len(result) > 0:
            print("Podcast exists")
        else:
            self.connection.execute(
                "insert into oeglobal_api_singlepodcast values(?,?,?,?,?)",
                [None, title, audio, description, date],
            )
            self.connection.commit()


# OeglobalPodcastDetail("https://podcast.oeglobal.org/").OeglobalData()
