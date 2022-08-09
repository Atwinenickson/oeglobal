import requests
from bs4 import BeautifulSoup
import re
import uuid


def get_podcasturl(url):
    # get page text
    page = requests.get(url)
    # parse with BFS
    soup = BeautifulSoup(page.text, "html.parser")

    # print(soup.prettify())
    podcasturls = []
    postcontainer = soup.findAll("div", attrs={"class": "post-container"})

    # print(postcontainer)

    for posts in postcontainer:
        # print(posts)
        headings = posts.findAll("h2", attrs={"class": "post-title"})

        # print(headings)

        for alink in headings:
            links = alink.findAll("a")
            # print(links)

            for anchor in links:
                anchorlink = anchor.get("href")
                anchortext = anchor.text
                # print(anchorlink)
                # print(anchortext)
                podcasturls.append(anchorlink)
    print(podcasturls)
    return podcasturls


get_podcasturl("https://podcast.oeglobal.org/")
