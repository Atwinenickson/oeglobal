import requests
from bs4 import BeautifulSoup
import re
import uuid


def get_podcast(url):
    # get url
    # get page text
    page = requests.get(url)
    # parse with BFS
    soup = BeautifulSoup(page.text, "html.parser")

    # print(soup.prettify())

    uuidOne = str(uuid.uuid4())
    podcastid = "pocast-" + uuidOne

    postcontainer = soup.find("div", attrs={"class": "post-content entry-content"})

    article_text = ""
    article = soup.find("div", {"class": "post-content entry-content"}).findAll("p")
    for element in article:
        article_text += "\n" + "".join(element.findAll(text=True))

    # print(article_text)

    productDivs = soup.findAll(
        "p", attrs={"class": "powerpress_links powerpress_links_mp3"}
    )
    # print(productDivs)
    for div in productDivs:
        # print (div.find('a')['href'])
        articleaudio = div.find("a")["href"]

    heading = soup.find("h1", attrs={"class": "post-title"}).text
    date = soup.find("p", attrs={"class": "post-date"}).text

    article_text = article_text.replace("\r", "").replace("\n", "")
    podcast = {
     
        "Title": heading,
        "Date": date,
        "AudioLink": articleaudio,
        "Description": article_text,
    }

    print(podcast)
    return podcast


get_podcast("https://podcast.oeglobal.org/2022/04/08/voices-34/")
