from bs4 import BeautifulSoup
import requests
import requests_cache

BASE_URL = "https://theaggie.org/"
PAGE_ROUTE = "/page/"
ARTS = "arts"
SPORTS = "sports"
CAMPUS = "campus"

# cache
requests_cache.install_cache('aggie_cache')


def getAllLinksOnPage(url, page=1):
    endpoint = (BASE_URL + url + PAGE_ROUTE + str(page))
    a = requests.get(endpoint)
    soup = BeautifulSoup(a.text)
    stories = soup.findAll('h3', "story-h")
    l = []
    for element in stories:
        #l.append(element.a.get_text())
        l.append(element.a['href'])
    return l


print(getAllLinksOnPage(CAMPUS))
