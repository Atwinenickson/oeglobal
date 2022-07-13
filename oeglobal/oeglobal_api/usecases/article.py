import requests
from bs4 import BeautifulSoup

paragraphtext = []    
    # get url
url = 'https://connect.oeglobal.org/c/oeg-plaza/12'
    # get page text
page = requests.get(url)
    # parse with BFS
soup = BeautifulSoup(page.text, 'html.parser')    




# topics = []
# anchorlinks = []
# posts = []
# views = []
# for tr in soup.find_all('span',attrs={'class':'link-top-line'}):
#     topics.append(tr.findAll('a')[0]['href'])
#     anchors = tr.findAll('a')
#     for anchor in anchors:
#         anchorlinks.append(anchor.text)

# print(topics)
# print(anchorlinks)




# for post in soup.find_all('span',attrs={'class':'posts'}):
#     posts.append(post.text)

# print(posts)

# for view in soup.find_all('span',attrs={'class':'views'}):
#     views.append(view.text)

# print(views)



data = []
table = soup.find('table')
table_body = table.find('tbody')

print(table_body)

rows = table_body.find_all('tr')

print(rows)
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    description = cols[0]
    replies = cols[2]
    views = cols[3]
    date_posted = cols[4]
    print('...................')
    data.append([ele for ele in cols if ele])

# print(data)


article = {'Title':description, 
        'Replies':replies, 
        'Views':views, 
        'Topics':topics, 
        'TopicLinks':anchorlinks,
        'Date':date_posted}

print(article)