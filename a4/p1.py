#from urllib2 import Request, urlopen
#from urlparse import urlparse, urlunparse
import requests#, requests_cache
#import pandas as pd
#import json


# my API key
key = "ULxnv6kWU0vTif6L3wHrB5MIkQKj0PrM3IfgfWbG"

#requests_cache.install_cache('food_cache')
# generate the query request to search for results

# Notes: Will return a JSON object. Default sort = "r", aka relevance
# EXAMPLE URL: https://api.nal.usda.gov/ndb/search/?api_key=ULxnv6kWU0vTif6L3wHrB5MIkQKj0PrM3IfgfWbG&format=json&q=mushroom

MAX = 5
SET_MAX = True

def get_request(key, searchObject):
    urlbase = "https://api.nal.usda.gov/ndb/search/"
    params = {"q":searchObject}
    params.update({"format":"json"})
    params.update({"api_key":key})
    if SET_MAX:
        params.update({"max":MAX})
    return requests.get(urlbase,params=params)
    #return urlbase + "/?" + "&".join("{}={}".format(a,b) for a,b in params.items())

def ndb_search(searchObject):
    searchList = []
    request = get_request(key, searchObject)
    searchList = request.json()
    return searchList[u'list']

print(ndb_search("quail eggs"))
