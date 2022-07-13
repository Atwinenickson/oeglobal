import requests
from bs4 import BeautifulSoup

paragraphtext = []    
    # get url
url = 'https://connect.oeglobal.org/c/oeg-plaza/12'
    # get page text
page = requests.get(url)
    # parse with BFS
soup = BeautifulSoup(page.text, 'html.parser')    

para = soup.findAll("div")


topics = []
anchorlinks = []
for tr in soup.find_all('span',attrs={'class':'link-top-line'}):
    topics.append(tr.findAll('a')[0]['href'])
    anchors = tr.findAll('a')
    for anchor in anchors:
        anchorlinks.append(anchor.text)

print(topics)
print(anchorlinks)
    # print(tr.findAll('a')[0].text)
    # for td in tr.find_all('span',attrs={'class':'link-top-line'}):    
    #     # data = td.find_all('span',attrs={'class':'link-top-line'})
    #     print(td)

        # for alink in data:
        #     link = alink.findAll('a')[0]['href']
        #     text = alink.find_all('a')[0].text
        #     print(link, text)
# try:
#     abody = soup.find(class_='d3284 africa').find('a')
#     aname = abody.get_text() 
# except:
#         aname = 'Anonymous'    

#     # get article title
# atitle = soup.find(class_="_21349 africa none _4ca8e")
# thetitle = atitle.get_text() 
#     # get main article page
# articlebody = soup.find(class_='_61c55')
#     # get text
# articletext = soup.find_all('p')[8:]
#     # print text
# for paragraph in articletext[:-1]:
#         # get the text only
#     text = paragraph.get_text()
#     paragraphtext.append(text)        
#     # combine all paragraphs into an article
# thearticle.append(paragraphtext)
# authorname.append(aname)
# title.append(thetitle)