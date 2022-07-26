import requests
from bs4 import BeautifulSoup
import re
import uuid


uuidOne = str(uuid.uuid4())
podcast_id = 'podcast-' + uuidOne
recent_podcast_id = 'recentpodcast-' + uuidOne


url = "https://podcast.oeglobal.org/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') 


def get_podcast():
    titles = []
    podcast_urls = []
    comments = []
    description_list = []
    dates = []
    post_container = soup.findAll('div', attrs={'class':'post-container'})

    for posts in post_container:
        headings = posts.findAll('h2', attrs={'class':'post-title'})


        for alink in headings:
            links = alink.findAll('a')
          

            for anchor in links:
                anchorlink = anchor.get('href')
                anchor_text = anchor.text
                podcast_urls.append(anchorlink)
                titles.append(anchor_text)

        descriptions = posts.findAll('p', attrs={'class':'post-excerpt'})
        


        for description in descriptions:
            desc = description.text
            description_list.append(desc)
       
        
        meta = posts.findAll('span', attrs={'class':'meta-text'})
        datelist = meta[0]
        commentlist = meta[1]

        for date in datelist:
            date = date
            dates.append(date)
        
        for comment in commentlist:
            comment = comment
            comments.append(comment)
        
        podcast = {
                'id':podcast_id,
                'title':anchor_text, 
            'podcast_url': anchorlink,
                    'comments':comment, 
                    'description':desc, 
                    'date':date}
    podcasts = [{'title': titles, 'podcast_url': podcast_urls,'comments': comments, 'description': description_list, 'date':dates} for titles,podcast_urls, comments,description_list, dates in zip(titles,podcast_urls,comments,description_list,dates )]

    return podcasts



def get_recent_podcast():
    titles = []
    podcast_urls = []
    dates = []
    
    recentcontainers = soup.findAll('div', attrs={'class':'widget widget_garfunkel_recent_posts'})

    for recentcontainer in recentcontainers:
        itemlist = recentcontainer.findAll('li')

        for item in itemlist:
            recentlink = recentcontainer.find('a')
            recentlink = recentlink.get('href')

            podcast_urls.append(recentlink)
            recentdiv = recentcontainer.findAll('div', attrs={'class':'inner'})
            for div in recentdiv:
                title = div.find('p', attrs={'class':'title'})
                date = div.find('p', attrs={'class':'meta'})
                title = title.text
                titles.append(title)
                date = date.text
                dates.append(date)

               
            recentpodcast = {
                    'id':recent_podcast_id,
                    'title':title, 
                'recent_podcast_url': recentlink,
                        'date':date}
                
    recentpodcasts = [{'title': titles, 'recent_podcast_url': podcast_urls, 'date':dates} for titles,podcast_urls, dates in zip(titles,podcast_urls,dates )]

    return recentpodcasts
