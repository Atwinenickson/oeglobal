import requests
from bs4 import BeautifulSoup



def get_articles(articleurl):
        # get url
    url = articleurl
        # get page text
    page = requests.get(url)
        # parse with BFS
    soup = BeautifulSoup(page.text, 'html.parser')    

    topics = []
    anchorlinks = []
    posts = []
    views = []
    for tr in soup.find_all('span',attrs={'class':'link-top-line'}):
        topics.append(tr.findAll('a')[0]['href'])
        anchors = tr.findAll('a')
        for anchor in anchors:
            anchorlinks.append(anchor.text)




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


    article = {'Title':description, 
            'Replies':replies, 
            'Views':views, 
            'Topics':topics, 
            'TopicLinks':anchorlinks,
            'Date':date_posted}

    print('...............article............')
    print(article)
    print('...............article............')

    return article
