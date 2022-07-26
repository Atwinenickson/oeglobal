import requests
from bs4 import BeautifulSoup
import re
import uuid



def get_podcast(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser') 


    uuidOne = str(uuid.uuid4())
    podcast_id = 'pocast-' + uuidOne



    post_container = soup.find('div', attrs={'class':'post-content entry-content'})

    article_text = ''
    article = soup.find("div", {"class":"post-content entry-content"}).findAll('p')
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text = True))

    productDivs = soup.findAll('p', attrs={'class' : 'powerpress_links powerpress_links_mp3'})
    for div in productDivs:
        article_audio = div.find('a')['href']

    
    heading = soup.find('h1', attrs={'class' : 'post-title'}).text
    date = soup.find('p', attrs={'class' : 'post-date'}).text

    article_text = article_text.replace('\r', '').replace('\n', '')
    podcast = {
            'id':podcast_id,
            'title': heading,
            'date': date,
            'audio_link':article_audio,
            'description':article_text,
            }

    print(podcast)
    return podcast

get_podcast("https://podcast.oeglobal.org/2022/04/08/voices-34/")