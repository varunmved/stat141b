#from urllib2 import Request, urlopen
#from urlparse import urlparse, urlunparse
import requests#, requests_cache
import pandas as pd
import json


# my API key
key = "ULxnv6kWU0vTif6L3wHrB5MIkQKj0PrM3IfgfWbG"

#requests_cache.install_cache('food_cache')
# generate the query request to search for results

# Notes: Will return a JSON object. Default sort = "r", aka relevance
# EXAMPLE URL: https://api.nal.usda.gov/ndb/search/?api_key=ULxnv6kWU0vTif6L3wHrB5MIkQKj0PrM3IfgfWbG&format=json&q=mushroom

MAX = 5
SET_MAX = True
FIELDS = ['food']

def get_request(key, searchObject):
    urlbase = "https://api.nal.usda.gov/ndb/search/"
    params = {"q":searchObject}
    params.update({"format":"json"})
    params.update({"api_key":key})
    params.update({"ds": "Standard Reference"})
    if SET_MAX:
        params.update({"max":MAX})
    return requests.get(urlbase,params=params)
    #return urlbase + "/?" + "&".join("{}={}".format(a,b) for a,b in params.items())

def ndb_search(searchObject):
    searchList = []
    request = get_request(key, searchObject)
    searchList = request.json()
    return searchList[u'list']

# part 2
def csvToListOfFood():
    #we only need the food to do our search
    df = pd.read_csv('fresh.csv', skipinitialspace=True, usecols=FIELDS)
    #remove duplicates
    df = df.drop_duplicates(subset="food", keep='last')
    df['ndbList'] = 0
    #only return the first 6 values
    df = df.head(n=5)
    return df

def searchOne(searchTerm):
    ndbl = []
    #add ", Raw" for more accurate results
    resp = (ndb_search(searchTerm+ ", Raw"))
    if not resp['item']:
        resp = ndb_search(searchTerm)
    items = resp['item']
    for item in items:
        if item:
            ndbl.append((item['ndbno']))
    #only return the first one, we'll keep this list handy if we need it later
    return ndbl[0]

def addNdbNumToDf(df):
    #fill the ndb numbers by using an apply function, wohoo!
    df['ndbList'] = df['food'].apply(searchOne)
    return df

# part 3
def ndb_report_request(nbdNumber):
    #api call for report
    url = "https://api.nal.usda.gov/ndb/V2/reports/"
    querystring = {"ndbno":nbdNumber,"format":"json","api_key":"ULxnv6kWU0vTif6L3wHrB5MIkQKj0PrM3IfgfWbG"}
    response = requests.request("GET", url, params=querystring)
    return (response.text)

def parseNdbJson(ndbj):
    #grab just what we need for each nutrition response
    p = ndbj['foods'][0]['food']['nutrients']
    return p

def ndb_report(ndbNumber):
    outl = []
    ndbt = ndb_report_request(ndbNumber)
    ndbj = json.loads(ndbt)
    foods = parseNdbJson(ndbj)
    for food in foods:
        outl.append(food)
    return outl



#print(ndb_search("quail eggs"))
#print(searchOne("kiwi"))
#print(csvToListOfFood())
#a = (csvToListOfFood())
#print(addNdbNumToDf(a))
print(ndb_report("09326"))
