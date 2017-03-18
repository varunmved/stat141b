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
    #construct url and make request
    endpoint = (BASE_URL + url + PAGE_ROUTE + str(page))
    a = requests.get(endpoint)

    #lets get soupayyyy
    soup = BeautifulSoup(a.text)

    #all stories are in an h3
    stories = soup.findAll('h3', "story-h")

    #grab the urls by href
    l = []
    for element in stories:
        l.append(element.a['href'])

    #done-zo
    return l

def getArticleInfo(url):
    #make request on endpoint
    endpoint = (url)
    a = requests.get(endpoint)

    #get the article body and title
    soup = BeautifulSoup(a.text)
    article = soup.find(itemprop = "articleBody")
    sections = article.findAll('p')

    #add all the <p> into a list
    l = []
    for elements in sections:
        l.append(elements.text)

    print(l)
    #get title, text, author after they're cleaned
    if not l:
        outj = {'author' : 'NaN', 'text' : 'NaN', 'title' : 'NaN', 'url' : 'NaN'}

    else:
        title = cleanTitle(soup.title.string)
        text = l[1:len(l)-1]
        author = cleanAuthor(l[-1])

        #build the return dictionary
        outj = {'author' : author, 'text' : text, 'title' : title, 'url' : url}

    #done-zo
    return outj

# utility functions to clean text
def cleanText(text):
    return text

def cleanTitle(raw):
    a = (raw.partition("|")[0]).split()
    title = ' '.join(a)
    return title

def cleanAuthor(raw):
    a = raw.split()
    name = a[2] + " " +  a[3]
    return name

def test():
    for i in range(0,4):
        articles = getAllLinksOnPage(CAMPUS, i)
        for a in articles:
            print(getArticleInfo(a))

test()

