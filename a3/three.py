import pandas as pd
import os
from os import listdir
from os.path import isfile, join

vegetable_path = "data/vegetables/"
fruit_path = "data/fruit/"

num_files = sum(os.path.isfile(os.path.join(vegetable_path, f)) for f in os.listdir(vegetable_path))

vegetableFiles = [f.split('.xlsx', 1)[0] for f in listdir(vegetable_path) if isfile(join(vegetable_path, f))]
fruitFiles  = [f.split('.xlsx', 1)[0] for f in listdir(fruit_path) if isfile(join(fruit_path, f))]

col = ["type", "food", "form", "price_per_lb", "yield_v", "lb_per_cup", "price_per_cup"]

df = pd.DataFrame()

#extract function, works for both fruits and veggies
def extract(typeO, path, obj):
    bkb = pd.read_excel(path + obj+".xlsx", header= None, skiprows = [0,1,2])
    fresh_row = bkb.iloc[0]
    price_per_lb = fresh_row[1]
    yield_v = fresh_row[3]
    lb_per_cup = fresh_row[4]
    price_per_cup = fresh_row[6]
    dout = {"type" : [typeO], "food" : [obj], "form": ["Fresh1"], "price_per_lb" :[price_per_lb] , "yield_v":[yield_v], "lb_per_cup":[lb_per_cup], "price_per_cup":[price_per_cup]}

    return dout

#returns combined dataframe of both fruits and veggies
def getBoth(fruitList, vegetableList):
    df2 = pd.DataFrame()
    l = []
    for f in fruitList:
        if '$' not in f:
            d = extract("fruit", fruit_path, f)
            new_df = pd.DataFrame.from_dict(d)
            l.append(new_df)
    for f in vegetableList:
         if '$' not in f:
            d = extract("vegetables", vegetable_path, f)
            new_df = pd.DataFrame.from_dict(d)
            l.append(new_df)

    df2 = pd.concat(l, axis = 0)
    return df2

def cleanData(df):
    df2 = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
    df2 = df2[pd.notnull(df2['price_per_lb'])]
    df2 = df2[pd.notnull(df2['price_per_cup'])]
    return df2

merged_df = getBoth(fruitFiles, vegetableFiles)
print(cleanData(merged_df))
