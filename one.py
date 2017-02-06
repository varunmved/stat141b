import pandas as pd
from os import listdir
from os.path import isfile, join

fruit_path = "data/fruit/"

onlyfiles = [f.split('.xlsx', 1)[0] for f in listdir(fruit_path) if isfile(join(fruit_path, f))]

#i don't use this
col = ["type", "food", "form", "price_per_lb", "yield_v", "lb_per_cup", "price_per_cup"]

def extract(fruit):
    bkb = pd.read_excel(fruit_path + fruit+".xlsx", header= None, skiprows = [0,1,2])
    fresh_row = bkb.iloc[0]
    price_per_lb = fresh_row[1]
    yield_v = fresh_row[3]
    lb_per_cup = fresh_row[4]
    price_per_cup = fresh_row[6]
    dout = {"type" : ["fruit"], "food" : [fruit], "form": ["Fresh1"], "price_per_lb" :[price_per_lb] , "yield_v":[yield_v], "lb_per_cup":[lb_per_cup], "price_per_cup":[price_per_cup]}

    return dout

def getFruit(fruitList):
    df2 = pd.DataFrame()
    l = []
    for f in fruitList:
        if '$' not in f:
            d = extract(f)
            new_df = pd.DataFrame.from_dict(d)
            l.append(new_df)
    df2 = pd.concat(l, axis = 0)
    return df2


print(getFruit(onlyfiles))
