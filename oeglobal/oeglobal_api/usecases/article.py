import requests
from bs4 import BeautifulSoup
import re
import uuid

def get_articles(articleurl):
        # get url
    url = articleurl
        # get page text
    page = requests.get(url)
        # parse with BFS
    soup = BeautifulSoup(page.text, 'html.parser')    

    topics = []
    anchor_links = []
    posts = []
    views = []
    for tr in soup.find_all('span',attrs={'class':'link-top-line'}):
        anchor_links.append(tr.findAll('a')[0]['href'])
        anchors = tr.findAll('a')
        for anchor in anchors:
            topics.append(anchor.text)




    for post in soup.find_all('span',attrs={'class':'posts'}):
        posts.append(post.text)


    for view in soup.find_all('span',attrs={'class':'views'}):
        views.append(view.text)



    data = []
    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        description = cols[0]
        replies = cols[2]
        views = cols[3]
        date_posted = cols[4]
        data.append([ele for ele in cols if ele])

    new_description = re.sub('\s{2,}', ' ', description)
    uuidOne = str(uuid.uuid4())
    article_id = 'article-' + uuidOne
    topic_id = 'topic-' + uuidOne
    topic_url_id = 'topic_url-' + uuidOne
    article = {
        'id':article_id,
        'title':new_description, 
    'article_url': url,
            'replies':replies, 
            'views':views, 
            'date':date_posted}
    topic =  {
        "topics":topics,
        "id":topic_id
    }

    topiclinks =  {
        "TopicUrls":anchor_links,
        "ID":topic_url_id
    }
    # print('...............article............')
    # print(topiclinks)
    # print('...............article............')

    return article, topic, topiclinks
