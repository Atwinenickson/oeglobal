import requests
from bs4 import BeautifulSoup
from article import get_articles

def get_urls(baseurl):
    page = requests.get(baseurl)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())


        
    pagelinks = []
    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):    
            data = td.find_all('div',attrs={'itemprop':'itemListElement'})
            # print(data)
            for heading3 in data:
                headings = heading3.findAll('h3')
                # print(headings)
                for alink in headings:
                    links = alink.findAll('a')
                    # print(links)
                    for link in links:
                        print("Found the URL:", link['href'])
                        href = link['href']
                        # print(href)
                        pagelinks.append('https://connect.oeglobal.org'+href)
                        
                                    
    # print(pagelinks)
    return pagelinks