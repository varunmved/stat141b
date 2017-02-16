import pandas as pd
from os import listdir
from os.path import isfile, join

vegetable_path = "data/vegetables/"

onlyfiles = [f.split('.xlsx', 1)[0] for f in listdir(vegetable_path) if isfile(join(vegetable_path, f))]

#i dont use this
col = ["type", "food", "form", "price_per_lb", "yield_v", "lb_per_cup", "price_per_cup"]

def extract(vegetable):
    bkb = pd.read_excel(vegetable_path + vegetable+".xlsx", header= None, skiprows = [0,1,2])
    fresh_row = bkb.iloc[0]
    price_per_lb = fresh_row[1]
    yield_v = fresh_row[3]
    lb_per_cup = fresh_row[4]
    price_per_cup = fresh_row[6]

    dout = {"type" : ["vegetable"], "food" : [vegetable], "form": ["Fresh1"], "price_per_lb" :[price_per_lb] , "yield_v":[yield_v], "lb_per_cup":[lb_per_cup], "price_per_cup":[price_per_cup]}

    '''
    vegetableSeries = pd.Series(data=["vegetable", vegetable, "Fresh1", price_per_lb, yield_v, lb_per_cup, price_per_cup], name = vegetable)
    return vegetableSeries
    '''
    return dout

def getVegetable(vegetableList):
    df2 = pd.DataFrame()
    l = []
    for f in vegetableList:
        if '$' not in f:
            d = extract(f)
            new_df = pd.DataFrame.from_dict(d)
            l.append(new_df)
    df2 = pd.concat(l, axis = 0)
    return df2

print(getVegetable(onlyfiles))
