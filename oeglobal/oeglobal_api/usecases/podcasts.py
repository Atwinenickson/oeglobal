import requests
from bs4 import BeautifulSoup
import re
import uuid


uuidOne = str(uuid.uuid4())
podcastid = 'podcast-' + uuidOne
recent_podcastid = 'recentpodcast-' + uuidOne

# get url
url = "https://podcast.oeglobal.org/"
# get page text
page = requests.get(url)
# parse with BFS
soup = BeautifulSoup(page.text, 'html.parser') 

# print(soup.prettify())

def get_podcast():
    titles = []
    podcasturls = []
    comments = []
    descriptionlist = []
    dates = []
    postcontainer = soup.findAll('div', attrs={'class':'post-container'})



    # print(postcontainer)

    for posts in postcontainer:
        # print(posts)
        headings = posts.findAll('h2', attrs={'class':'post-title'})

        # print(headings)

        for alink in headings:
            links = alink.findAll('a')
            # print(links)

            for anchor in links:
                anchorlink = anchor.get('href')
                anchortext = anchor.text
                # print(anchorlink)
                # print(anchortext)
                podcasturls.append(anchorlink)
                titles.append(anchortext)

        descriptions = posts.findAll('p', attrs={'class':'post-excerpt'})
        

        # print(descriptions)

        for description in descriptions:
            desc = description.text
            descriptionlist.append(desc)
            # print(desc)
        
        meta = posts.findAll('span', attrs={'class':'meta-text'})
        datelist = meta[0]
        commentlist = meta[1]

        for date in datelist:
            date = date
            # print(date)
            dates.append(date)
        
        for comment in commentlist:
            comment = comment
            # print(comment)
            comments.append(comment)
        
        podcast = {
                'ID':podcastid,
                'Title':anchortext, 
            'Podcasturl': anchorlink,
                    'Comments':comment, 
                    'Description':desc, 
                    'Date':date}
    podcasts = [{'Title': titles, 'Podcasturl': podcasturls,'Comments': comments, 'Description': descriptionlist, 'Date':dates} for titles,podcasturls, comments,descriptionlist, dates in zip(titles,podcasturls,comments,descriptionlist,dates )]
    # print("Podcasts:",podcasts)

    return podcasts


# get_podcast()

# print('....................|||||.....................\n')

def get_recent_podcast():
    titles = []
    podcasturls = []
    dates = []
    
    recentcontainers = soup.findAll('div', attrs={'class':'widget widget_garfunkel_recent_posts'})
    # print(recentcontainer)

    for recentcontainer in recentcontainers:
        # print(recentcontainer)
        itemlist = recentcontainer.findAll('li')
        # print(itemlist)
        for item in itemlist:
            recentlink = recentcontainer.find('a')
            recentlink = recentlink.get('href')
            # print(recentlink)
            podcasturls.append(recentlink)
            recentdiv = recentcontainer.findAll('div', attrs={'class':'inner'})
            for div in recentdiv:
                title = div.find('p', attrs={'class':'title'})
                date = div.find('p', attrs={'class':'meta'})
                title = title.text
                titles.append(title)
                date = date.text
                dates.append(date)

                # print(title)
                # print(date)
            recentpodcast = {
                    'ID':recent_podcastid,
                    'Title':title, 
                'RecentPodcasturl': recentlink,
                        'Date':date}
                
            # print(recentpodcast)
            # return recentpodcast
    recentpodcasts = [{'Title': titles, 'RecentPodcasturl': podcasturls, 'Date':dates} for titles,podcasturls, dates in zip(titles,podcasturls,dates )]
    # print("Recent Podcasts:",recentpodcasts)

    return recentpodcasts


# get_recent_podcast()