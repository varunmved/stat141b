#from urllib2 import Request, urlopen
#from urlparse import urlparse, urlunparse
import requests#, requests_cache
import pandas as pd
#import json


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
    #print(searchObject)
    searchList = []
    request = get_request(key, searchObject)
    searchList = request.json()
    #print(searchList)
    return searchList[u'list']

def csvToListOfFood():
    #we only need the food to do our search
    df = pd.read_csv('fresh.csv', skipinitialspace=True, usecols=FIELDS)
    #remove duplicates
    df = df.drop_duplicates(subset="food", keep='last')
    df['ndbList'] = 0
    #only return the first 6 values
    df = df.head(n=5)
    return df
    #listFromDf = df['food'].tolist()
    #remove duplicates and return a list
    #return list(set(listFromDf))

def searchFromList(foodList):
    for food in foodList:
        #we're making the assumption that all our food is raw
        #we'll get better results if we explicitly say that in our search params
        ndb_search(food + ", Raw")

def searchOne(searchTerm):
    #print(searchTerm)
    ndbl = []
    resp = (ndb_search(searchTerm+ ", Raw"))
    items = resp['item']
    for item in items:
        if item:
            ndbl.append((item['ndbno']))
    #only return the first three
    return ndbl[:2]

def addNdbNumToDf(df):
    #fakel = [1,2,3,3]
    #print(df)
    df['ndbList'] = df['food'].apply(searchOne)
    return df

#print(ndb_search("quail eggs"))
print(csvToListOfFood())
a = (csvToListOfFood())
print(addNdbNumToDf(a))
#print(searchOne("plum"))
