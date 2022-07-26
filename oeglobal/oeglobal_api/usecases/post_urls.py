import requests
from bs4 import BeautifulSoup
from article import get_articles

def get_urls(baseurl):
    page = requests.get(baseurl)

    soup = BeautifulSoup(page.content, 'html.parser')



        
    pagelinks = []
    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):    
            data = td.find_all('div',attrs={'itemprop':'itemListElement'})
    
            for heading3 in data:
                headings = heading3.findAll('h3')
           
                for alink in headings:
                    links = alink.findAll('a')
                
                    for link in links:
                        href = link['href']
                        pagelinks.append('https://connect.oeglobal.org'+href)
                        
                       
    return pagelinks