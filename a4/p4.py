import requests
import requests_cache
import pandas as pd
import json

# my API key
key = "ULxnv6kWU0vTif6L3wHrB5MIkQKj0PrM3IfgfWbG"

requests_cache.install_cache('food_cache')
# generate the query request to search for results

# Notes: Will return a JSON object. Default sort = "r", aka relevance
# EXAMPLE URL: https://api.nal.usda.gov/ndb/search/?api_key=ULxnv6kWU0vTif6L3wHrB5MIkQKj0PrM3IfgfWbG&format=json&q=mushroom

MAX = 5
SET_MAX = True
FIELDS = ['food']

# part 1
def get_request(key, searchObject):
    urlbase = "https://api.nal.usda.gov/ndb/search/"
    params = {"q":searchObject}
    params.update({"format":"json"})
    params.update({"api_key":key})
    params.update({"ds": "Standard Reference"})
    if SET_MAX:
        params.update({"max":MAX})
    return requests.get(urlbase,params=params)

def ndb_search(searchObject):
    searchList = []
    request = get_request(key, searchObject)
    searchList = request.json()
    try:
        searchList['errors']
    except:
       a = searchList[u'list']
       return a
    try:
       a = searchList[u'list']
       return a
    except:
       return "NaN"

# part 2
def csvToListOfFood():
    #we only need the food to do our search
    df = pd.read_csv('fresh.csv', skipinitialspace=True, usecols=FIELDS)
    #remove duplicates
    df = df.drop_duplicates(subset="food", keep='last')
    df['ndbList'] = 0
    #only return the first 2 values
    #df = df.head(n=2)
    return df

def searchOne(searchTerm):
    ndbl = []
    #add ", Raw" for more accurate results
    resp = ndb_search(searchTerm+ ", Raw")
    print(resp)
    if resp ==  "NaN":
        print('try again!')
        resp = ndb_search(removeUnderScore(searchTerm))
        if resp == "NaN":
            resp = ndb_search(stripBeforeSpace(searchTerm))

    items = resp['item']
    for item in items:
        if item:
            ndbl.append((item['ndbno']))
    #only return the first one, we'll keep this list handy if we need it later
    return ndbl[0]

def removeUnderScore(a):
    if "_" in a:
        a.replace("_", " ")
    return a

def stripBeforeSpace(a):
    return a[1]

def addNdbNumToDf(df):
    #fill the ndb numbers by using an apply function, wohoo!
    df['ndbNumber'] = df['food'].apply(searchOne)
    return df

def getListOfNdbNums(df):
    a = df['ndbNumber'].tolist()
    print(a)
    return(a)

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
    #make a dataframe of nutrients
    outl = []
    ndbt = ndb_report_request(ndbNumber)
    ndbj = json.loads(ndbt)
    foods = parseNdbJson(ndbj)
    for food in foods:
        #add the number so we can join it
        food.update({"ndbNumber":ndbNumber})
        outl.append(food)
    df = makeDfFromL(outl)
    return df

def makeDfFromL(l):
    #dataframe from a list, easy-peasy
    df = pd.DataFrame(l)
    return df

def applyNdbNumDf(df):
    #use an apply function to get a dataframe of the nutrients based on ndbNumber
    df['nutrition'] = df['ndbNumber'].apply(ndb_report)
    return df

def applyNdbNumList(a):
    outl = []
    for item in a:
        outl.append(ndb_report(item))
    df = pd.concat(outl)
    return df

def join_df(food, nutr):
    #merge the csv dataset to the nutrient dataset, tidy data :)
    df = pd.merge(food, nutr, on='ndbNumber')
    return df

def dfToCsv(df):
    return df.to_csv(path_or_buf="out.csv")

a = (csvToListOfFood())
a = addNdbNumToDf(a)
l = getListOfNdbNums(a)
b = (applyNdbNumList(l))
c =  join_df(a,b)
d = dfToCsv(c)
