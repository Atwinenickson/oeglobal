import requests
from bs4 import BeautifulSoup
import re
import uuid


def get_podcasturl(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser') 
    podcast_urls = []
    post_container = soup.findAll('div', attrs={'class':'post-container'})


    for posts in post_container:
        headings = posts.findAll('h2', attrs={'class':'post-title'})

        for alink in headings:
            links = alink.findAll('a')

            for anchor in links:
                anchor_link = anchor.get('href')
                anchor_text = anchor.text
                podcast_urls.append(anchor_link)
    print(podcast_urls)
    return podcast_urls


get_podcasturl("https://podcast.oeglobal.org/")