import requests
from bs4 import BeautifulSoup
import re
import uuid


def get_podcasturl(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser') 
    podcasturls = []
    postcontainer = soup.findAll('div', attrs={'class':'post-container'})


    for posts in postcontainer:
        headings = posts.findAll('h2', attrs={'class':'post-title'})

        for alink in headings:
            links = alink.findAll('a')

            for anchor in links:
                anchorlink = anchor.get('href')
                anchortext = anchor.text
                podcasturls.append(anchorlink)
    print(podcasturls)
    return podcasturls


get_podcasturl("https://podcast.oeglobal.org/")