
# Assignment 3

The US Department of Agriculture publishes price estimates for fruits and vegetables [online](https://www.ers.usda.gov/data-products/fruit-and-vegetable-prices/fruit-and-vegetable-prices/). The most recent estimates are based on a 2013 survey of US retail stores.

The estimates are provided as a collection of MS Excel files, with one file per fruit or vegetable. The `assignment3_data.zip` file contains the fruit and vegetable files in the directories `fruit` and `vegetables`, respectively.

__Exercise 1.1.__ Use pandas to extract the "Fresh" row(s) from the <strong style="color:#B0B">fruit</strong> Excel files. Combine the data into a single data frame. Your data frame should look something like this:

type       | food       | form   | price_per_lb | yield | lb_per_cup | price_per_cup
---------- | ---------- | ------ | ------------ | ----- | ---------- | -------------
fruit      | watermelon | Fresh1 | 0.333412     | 0.52  | 0.330693   | 0.212033
fruit      | cantaloupe | Fresh1 | 0.535874     | 0.51  | 0.374786   | 0.3938
vegetables | onions     | Fresh1 | 1.03811      | 0.9   | 0.35274    | 0.406868
...        |            |        |              |       |            |


It's okay if the rows and columns of your data frame are in a different order. These modules are especially relevant:

* [`str` methods](https://docs.python.org/2/library/stdtypes.html#string-methods)
* [`os`](https://docs.python.org/2/library/os.html)
* [`os.path`](https://docs.python.org/2/library/os.path.html)
* [pandas](http://pandas.pydata.org/pandas-docs/stable/): `read_excel()`, `concat()`, `.fillna()`, `.str`, plotting methods

Ask questions and search the documentation/web to find the functions you need.


I set the path to the fruit directory and use a list comprehension to get fruit names.


```python
import pandas as pd
import os
from os import listdir
from os.path import isfile, join

fruit_path = "data/fruit/"

num_files = sum(os.path.isfile(os.path.join(fruit_path, f)) for f in os.listdir(fruit_path))

onlyfiles = [f.split('.xlsx', 1)[0] for f in listdir(fruit_path) if isfile(join(fruit_path, f))]

col = ["type", "food", "form", "price_per_lb", "yield_v", "lb_per_cup", "price_per_cup"]

df = pd.DataFrame()

onlyfiles[1]
```




    'apricots'



This is the extract function which will read in a fruit (input will be from onlyfiles), and extract specified values. It returns a dictionary.


```python
def extract(fruit):
    bkb = pd.read_excel(fruit_path + fruit+".xlsx", header= None, skiprows = [0,1,2])
    fresh_row = bkb.iloc[0]
    price_per_lb = fresh_row[1]
    yield_v = fresh_row[3]
    lb_per_cup = fresh_row[4]
    price_per_cup = fresh_row[6]
    lout = ["fruit", fruit, "Fresh1" , price_per_lb, yield_v, lb_per_cup, price_per_cup]

    dout = {"type" : ["fruit"], "food" : [fruit], "form": ["Fresh1"], "price_per_lb" :[price_per_lb] , "yield_v":[yield_v], "lb_per_cup":[lb_per_cup], "price_per_cup":[price_per_cup]}

    return dout

extract(onlyfiles[1])
```




    {'food': ['apricots'],
     'form': ['Fresh1'],
     'lb_per_cup': [0.363762732605048],
     'price_per_cup': [1.1891020280290363],
     'price_per_lb': [3.040071967096438],
     'type': ['fruit'],
     'yield_v': [0.93]}



The getFruit function will get all the fruits in the fruit folder and create a data frame out of all the entries.


```python
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

fruit_df = getFruit(onlyfiles)
fruit_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>form</th>
      <th>lb_per_cup</th>
      <th>price_per_cup</th>
      <th>price_per_lb</th>
      <th>type</th>
      <th>yield_v</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apples</td>
      <td>Fresh1</td>
      <td>0.242508</td>
      <td>0.422373</td>
      <td>1.567515</td>
      <td>fruit</td>
      <td>0.90</td>
    </tr>
    <tr>
      <th>0</th>
      <td>apricots</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>1.189102</td>
      <td>3.040072</td>
      <td>fruit</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>0</th>
      <td>bananas</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.292965</td>
      <td>0.566983</td>
      <td>fruit</td>
      <td>0.64</td>
    </tr>
    <tr>
      <th>0</th>
      <td>berries_mixed</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>1.127735</td>
      <td>3.410215</td>
      <td>fruit</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blackberries</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>1.922919</td>
      <td>5.774708</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blueberries</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>1.593177</td>
      <td>4.734622</td>
      <td>fruit</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cantaloupe</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.393800</td>
      <td>0.535874</td>
      <td>fruit</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cherries</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>1.334548</td>
      <td>3.592990</td>
      <td>fruit</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cranberries</td>
      <td>Fresh1</td>
      <td>0.123163</td>
      <td>0.589551</td>
      <td>4.786741</td>
      <td>fruit</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>dates</td>
      <td>Fresh1</td>
      <td>0.165347</td>
      <td>0.792234</td>
      <td>4.791351</td>
      <td>fruit</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>figs</td>
      <td>Fresh1</td>
      <td>0.165347</td>
      <td>0.990068</td>
      <td>5.748318</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>fruit_cocktail</td>
      <td>Fresh1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>fruit</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>grapefruit</td>
      <td>Fresh1</td>
      <td>0.462971</td>
      <td>0.848278</td>
      <td>0.897802</td>
      <td>fruit</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>0</th>
      <td>grapes</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.721266</td>
      <td>2.093827</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>honeydew</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.649077</td>
      <td>0.796656</td>
      <td>fruit</td>
      <td>0.46</td>
    </tr>
    <tr>
      <th>0</th>
      <td>kiwi</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>1.037970</td>
      <td>2.044683</td>
      <td>fruit</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>0</th>
      <td>mangoes</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.705783</td>
      <td>1.377563</td>
      <td>fruit</td>
      <td>0.71</td>
    </tr>
    <tr>
      <th>0</th>
      <td>nectarines</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>0.618667</td>
      <td>1.761148</td>
      <td>fruit</td>
      <td>0.91</td>
    </tr>
    <tr>
      <th>0</th>
      <td>oranges</td>
      <td>Fresh1</td>
      <td>0.407855</td>
      <td>0.578357</td>
      <td>1.035173</td>
      <td>fruit</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>0</th>
      <td>papaya</td>
      <td>Fresh1</td>
      <td>0.308647</td>
      <td>0.646174</td>
      <td>1.298012</td>
      <td>fruit</td>
      <td>0.62</td>
    </tr>
    <tr>
      <th>0</th>
      <td>peaches</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>0.566390</td>
      <td>1.591187</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pears</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.590740</td>
      <td>1.461575</td>
      <td>fruit</td>
      <td>0.90</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pineapple</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.447686</td>
      <td>0.627662</td>
      <td>fruit</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>0</th>
      <td>plums</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.707176</td>
      <td>1.827416</td>
      <td>fruit</td>
      <td>0.94</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pomegranate</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>1.326342</td>
      <td>2.173590</td>
      <td>fruit</td>
      <td>0.56</td>
    </tr>
    <tr>
      <th>0</th>
      <td>raspberries</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>2.322874</td>
      <td>6.975811</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>strawberries</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>0.802171</td>
      <td>2.358808</td>
      <td>fruit</td>
      <td>0.94</td>
    </tr>
    <tr>
      <th>0</th>
      <td>tangerines</td>
      <td>Fresh1</td>
      <td>0.407855</td>
      <td>0.759471</td>
      <td>1.377962</td>
      <td>fruit</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>0</th>
      <td>watermelon</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.212033</td>
      <td>0.333412</td>
      <td>fruit</td>
      <td>0.52</td>
    </tr>
  </tbody>
</table>
</div>



__Exercise 1.2.__ Reuse your code from exercise 1.1 to extract the "Fresh" row(s) from the <strong style="color:#B0B">vegetable</strong> Excel files.

Does your code produce the correct prices for tomatoes? If not, why not? Do any other files have the same problem as the tomatoes file?

You don't need to extract the prices for these problem files. However, make sure the prices are extracted for files like asparagus that don't have this problem.

Using the same code for fruit, I simply change the path to vegetables.


```python
vegetable_path = "data/vegetables/"

onlyfiles = [f.split('.xlsx', 1)[0] for f in listdir(vegetable_path) if isfile(join(vegetable_path, f))]


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
```


```python
extract(onlyfiles[1])
```




    {'food': ['artichoke'],
     'form': ['Fresh1'],
     'lb_per_cup': [0.38580895882353577],
     'price_per_cup': [2.2749668026387808],
     'price_per_lb': [2.2130504792860322],
     'type': ['vegetable'],
     'yield_v': [0.37530864197530867]}




```python
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

vegetable_df = getVegetable(onlyfiles)
vegetable_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>form</th>
      <th>lb_per_cup</th>
      <th>price_per_cup</th>
      <th>price_per_lb</th>
      <th>type</th>
      <th>yield_v</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>acorn_squash</td>
      <td>Fresh1</td>
      <td>0.451948</td>
      <td>1.155360</td>
      <td>1.17225</td>
      <td>vegetable</td>
      <td>0.458554</td>
    </tr>
    <tr>
      <th>0</th>
      <td>artichoke</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>2.274967</td>
      <td>2.21305</td>
      <td>vegetable</td>
      <td>0.375309</td>
    </tr>
    <tr>
      <th>0</th>
      <td>asparagus</td>
      <td>Fresh1</td>
      <td>0.396832</td>
      <td>2.582272</td>
      <td>3.21349</td>
      <td>vegetable</td>
      <td>0.493835</td>
    </tr>
    <tr>
      <th>0</th>
      <td>avocados</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>0.964886</td>
      <td>2.23587</td>
      <td>vegetable</td>
      <td>0.740753</td>
    </tr>
    <tr>
      <th>0</th>
      <td>beets</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.586555</td>
      <td>1.01728</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blackeye_peas</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.524954</td>
      <td>0.910441</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>black_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.582025</td>
      <td>0.98058</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>broccoli</td>
      <td>Fresh1</td>
      <td></td>
      <td>NaN</td>
      <td></td>
      <td>vegetable</td>
      <td></td>
    </tr>
    <tr>
      <th>0</th>
      <td>brussels_sprouts</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>0.890898</td>
      <td>2.76355</td>
      <td>vegetable</td>
      <td>1.06</td>
    </tr>
    <tr>
      <th>0</th>
      <td>butternut_squash</td>
      <td>Fresh1</td>
      <td>0.451948</td>
      <td>0.787893</td>
      <td>1.24474</td>
      <td>vegetable</td>
      <td>0.714</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cabbage</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.245944</td>
      <td>0.579208</td>
      <td>vegetable</td>
      <td>0.778797</td>
    </tr>
    <tr>
      <th>0</th>
      <td>carrots</td>
      <td>Fresh1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>vegetable</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cauliflower</td>
      <td>Fresh1</td>
      <td></td>
      <td>NaN</td>
      <td></td>
      <td>vegetable</td>
      <td></td>
    </tr>
    <tr>
      <th>0</th>
      <td>celery</td>
      <td>Fresh1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>vegetable</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>collard_greens</td>
      <td>Fresh1</td>
      <td>0.286601</td>
      <td>0.650001</td>
      <td>2.63084</td>
      <td>vegetable</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>0</th>
      <td>corn_sweet</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>1.812497</td>
      <td>2.69062</td>
      <td>vegetable</td>
      <td>0.54</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cucumbers</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.353448</td>
      <td>1.29593</td>
      <td>vegetable</td>
      <td>0.97</td>
    </tr>
    <tr>
      <th>0</th>
      <td>great_northern_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.548392</td>
      <td>0.923916</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>green_beans</td>
      <td>Fresh1</td>
      <td>0.275578</td>
      <td>0.696606</td>
      <td>2.13997</td>
      <td>vegetable</td>
      <td>0.846575</td>
    </tr>
    <tr>
      <th>0</th>
      <td>green_peas</td>
      <td>Fresh1</td>
      <td>0.35274</td>
      <td>0.549769</td>
      <td>1.01307</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>green_peppers</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.455022</td>
      <td>1.41036</td>
      <td>vegetable</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>0</th>
      <td>kale</td>
      <td>Fresh1</td>
      <td>0.286601</td>
      <td>0.766262</td>
      <td>2.8073</td>
      <td>vegetable</td>
      <td>1.05</td>
    </tr>
    <tr>
      <th>0</th>
      <td>kidney_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.535194</td>
      <td>0.90168</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>lentils</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.196738</td>
      <td>1.38504</td>
      <td>vegetable</td>
      <td>2.7161</td>
    </tr>
    <tr>
      <th>0</th>
      <td>lettuce_iceberg</td>
      <td>Fresh1</td>
      <td>0.242508</td>
      <td>0.309655</td>
      <td>1.21304</td>
      <td>vegetable</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>0</th>
      <td>lettuce_romaine</td>
      <td>Fresh1</td>
      <td></td>
      <td>NaN</td>
      <td></td>
      <td>vegetable</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>lima_beans</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.797757</td>
      <td>1.38357</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>mixed_vegetables</td>
      <td>Fresh1</td>
      <td></td>
      <td>NaN</td>
      <td></td>
      <td>vegetable</td>
      <td></td>
    </tr>
    <tr>
      <th>0</th>
      <td>mushrooms</td>
      <td>Fresh1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>vegetable</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>mustard_greens</td>
      <td>Fresh1</td>
      <td>0.308647</td>
      <td>0.944032</td>
      <td>2.56924</td>
      <td>vegetable</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>0</th>
      <td>navy_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.575997</td>
      <td>0.970423</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>okra</td>
      <td>Fresh1</td>
      <td>0.35274</td>
      <td>1.473146</td>
      <td>3.21355</td>
      <td>vegetable</td>
      <td>0.769474</td>
    </tr>
    <tr>
      <th>0</th>
      <td>olives</td>
      <td>Fresh1</td>
      <td>0.297624</td>
      <td>1.246102</td>
      <td>4.18683</td>
      <td>vegetable</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>onions</td>
      <td>Fresh1</td>
      <td>0.35274</td>
      <td>0.406868</td>
      <td>1.03811</td>
      <td>vegetable</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pinto_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.514129</td>
      <td>0.86619</td>
      <td>vegetable</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>potatoes</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.184017</td>
      <td>0.56432</td>
      <td>vegetable</td>
      <td>0.811301</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pumpkin</td>
      <td>Fresh1</td>
      <td>0.540133</td>
      <td>0.730411</td>
      <td>1.35228</td>
      <td>vegetable</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>radish</td>
      <td>Fresh1</td>
      <td>0.275578</td>
      <td>0.401618</td>
      <td>1.31163</td>
      <td>vegetable</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>red_peppers</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.734926</td>
      <td>2.27794</td>
      <td>vegetable</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>0</th>
      <td>spinach</td>
      <td>Fresh1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>vegetable</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>summer_squash</td>
      <td>Fresh1</td>
      <td>0.396832</td>
      <td>0.845480</td>
      <td>1.63948</td>
      <td>vegetable</td>
      <td>0.7695</td>
    </tr>
    <tr>
      <th>0</th>
      <td>sweet_potatoes</td>
      <td>Fresh1</td>
      <td>0.440925</td>
      <td>0.499400</td>
      <td>0.918897</td>
      <td>vegetable</td>
      <td>0.811301</td>
    </tr>
    <tr>
      <th>0</th>
      <td>tomatoes</td>
      <td>Fresh1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>vegetable</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>turnip_greens</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>1.053526</td>
      <td>2.47175</td>
      <td>vegetable</td>
      <td>0.75</td>
    </tr>
  </tbody>
</table>
</div>



The tomatoes entry does not have the correct information (it displays NaN for all its rows instead).
Broccoli, celery, carrots, cauliflower, romaine lettuce, mixed vegetables, mushrooms, and spinach also have NaN values.

This is because these entries have nothing on the row which is labeled "Fresh". There are different types of those vegetables which are sold at different prices.

__Exercise 1.3.__ Remove rows without a price from the vegetable data frame and then combine the fruit and vegetable data frames. Make sure all columns of numbers are numeric (not strings).

I now combine the vegetable and fruit files into one data frame. I then clean for invalid entries.


```python
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
```


```python
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
```


```python
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

merged_df = getBoth(fruitFiles, vegetableFiles)
merged_df[:5]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>form</th>
      <th>lb_per_cup</th>
      <th>price_per_cup</th>
      <th>price_per_lb</th>
      <th>type</th>
      <th>yield_v</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apples</td>
      <td>Fresh1</td>
      <td>0.242508</td>
      <td>0.422373</td>
      <td>1.56752</td>
      <td>fruit</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>apricots</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>1.189102</td>
      <td>3.04007</td>
      <td>fruit</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>0</th>
      <td>bananas</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.292965</td>
      <td>0.566983</td>
      <td>fruit</td>
      <td>0.64</td>
    </tr>
    <tr>
      <th>0</th>
      <td>berries_mixed</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>1.127735</td>
      <td>3.41021</td>
      <td>fruit</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blackberries</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>1.922919</td>
      <td>5.77471</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
  </tbody>
</table>
</div>



I now clean the data to remove invalid rows.


```python
def cleanData(df):
    df2 = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
    df2 = df2[pd.notnull(df2['price_per_lb'])]
    df2 = df2[pd.notnull(df2['price_per_cup'])]
    return df2

clean_df = cleanData(merged_df)
clean_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>form</th>
      <th>lb_per_cup</th>
      <th>price_per_cup</th>
      <th>price_per_lb</th>
      <th>type</th>
      <th>yield_v</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apples</td>
      <td>Fresh1</td>
      <td>0.242508</td>
      <td>0.422373</td>
      <td>1.56752</td>
      <td>fruit</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>apricots</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>1.189102</td>
      <td>3.04007</td>
      <td>fruit</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>0</th>
      <td>bananas</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.292965</td>
      <td>0.566983</td>
      <td>fruit</td>
      <td>0.64</td>
    </tr>
    <tr>
      <th>0</th>
      <td>berries_mixed</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>1.127735</td>
      <td>3.41021</td>
      <td>fruit</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blackberries</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>1.922919</td>
      <td>5.77471</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blueberries</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>1.593177</td>
      <td>4.73462</td>
      <td>fruit</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cantaloupe</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.393800</td>
      <td>0.535874</td>
      <td>fruit</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cherries</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>1.334548</td>
      <td>3.59299</td>
      <td>fruit</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cranberries</td>
      <td>Fresh1</td>
      <td>0.123163</td>
      <td>0.589551</td>
      <td>4.78674</td>
      <td>fruit</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>dates</td>
      <td>Fresh1</td>
      <td>0.165347</td>
      <td>0.792234</td>
      <td>4.79135</td>
      <td>fruit</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>figs</td>
      <td>Fresh1</td>
      <td>0.165347</td>
      <td>0.990068</td>
      <td>5.74832</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>grapefruit</td>
      <td>Fresh1</td>
      <td>0.462971</td>
      <td>0.848278</td>
      <td>0.897802</td>
      <td>fruit</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>0</th>
      <td>grapes</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.721266</td>
      <td>2.09383</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>honeydew</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.649077</td>
      <td>0.796656</td>
      <td>fruit</td>
      <td>0.46</td>
    </tr>
    <tr>
      <th>0</th>
      <td>kiwi</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>1.037970</td>
      <td>2.04468</td>
      <td>fruit</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>0</th>
      <td>mangoes</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.705783</td>
      <td>1.37756</td>
      <td>fruit</td>
      <td>0.71</td>
    </tr>
    <tr>
      <th>0</th>
      <td>nectarines</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>0.618667</td>
      <td>1.76115</td>
      <td>fruit</td>
      <td>0.91</td>
    </tr>
    <tr>
      <th>0</th>
      <td>oranges</td>
      <td>Fresh1</td>
      <td>0.407855</td>
      <td>0.578357</td>
      <td>1.03517</td>
      <td>fruit</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>0</th>
      <td>papaya</td>
      <td>Fresh1</td>
      <td>0.308647</td>
      <td>0.646174</td>
      <td>1.29801</td>
      <td>fruit</td>
      <td>0.62</td>
    </tr>
    <tr>
      <th>0</th>
      <td>peaches</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>0.566390</td>
      <td>1.59119</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pears</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.590740</td>
      <td>1.46157</td>
      <td>fruit</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pineapple</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.447686</td>
      <td>0.627662</td>
      <td>fruit</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>0</th>
      <td>plums</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.707176</td>
      <td>1.82742</td>
      <td>fruit</td>
      <td>0.94</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pomegranate</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>1.326342</td>
      <td>2.17359</td>
      <td>fruit</td>
      <td>0.56</td>
    </tr>
    <tr>
      <th>0</th>
      <td>raspberries</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>2.322874</td>
      <td>6.97581</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>strawberries</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>0.802171</td>
      <td>2.35881</td>
      <td>fruit</td>
      <td>0.94</td>
    </tr>
    <tr>
      <th>0</th>
      <td>tangerines</td>
      <td>Fresh1</td>
      <td>0.407855</td>
      <td>0.759471</td>
      <td>1.37796</td>
      <td>fruit</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>0</th>
      <td>watermelon</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.212033</td>
      <td>0.333412</td>
      <td>fruit</td>
      <td>0.52</td>
    </tr>
    <tr>
      <th>0</th>
      <td>acorn_squash</td>
      <td>Fresh1</td>
      <td>0.451948</td>
      <td>1.155360</td>
      <td>1.17225</td>
      <td>vegetables</td>
      <td>0.458554</td>
    </tr>
    <tr>
      <th>0</th>
      <td>artichoke</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>2.274967</td>
      <td>2.21305</td>
      <td>vegetables</td>
      <td>0.375309</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blackeye_peas</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.524954</td>
      <td>0.910441</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>black_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.582025</td>
      <td>0.98058</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>brussels_sprouts</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>0.890898</td>
      <td>2.76355</td>
      <td>vegetables</td>
      <td>1.06</td>
    </tr>
    <tr>
      <th>0</th>
      <td>butternut_squash</td>
      <td>Fresh1</td>
      <td>0.451948</td>
      <td>0.787893</td>
      <td>1.24474</td>
      <td>vegetables</td>
      <td>0.714</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cabbage</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.245944</td>
      <td>0.579208</td>
      <td>vegetables</td>
      <td>0.778797</td>
    </tr>
    <tr>
      <th>0</th>
      <td>collard_greens</td>
      <td>Fresh1</td>
      <td>0.286601</td>
      <td>0.650001</td>
      <td>2.63084</td>
      <td>vegetables</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>0</th>
      <td>corn_sweet</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>1.812497</td>
      <td>2.69062</td>
      <td>vegetables</td>
      <td>0.54</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cucumbers</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.353448</td>
      <td>1.29593</td>
      <td>vegetables</td>
      <td>0.97</td>
    </tr>
    <tr>
      <th>0</th>
      <td>great_northern_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.548392</td>
      <td>0.923916</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>green_beans</td>
      <td>Fresh1</td>
      <td>0.275578</td>
      <td>0.696606</td>
      <td>2.13997</td>
      <td>vegetables</td>
      <td>0.846575</td>
    </tr>
    <tr>
      <th>0</th>
      <td>green_peas</td>
      <td>Fresh1</td>
      <td>0.35274</td>
      <td>0.549769</td>
      <td>1.01307</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>green_peppers</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.455022</td>
      <td>1.41036</td>
      <td>vegetables</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>0</th>
      <td>kale</td>
      <td>Fresh1</td>
      <td>0.286601</td>
      <td>0.766262</td>
      <td>2.8073</td>
      <td>vegetables</td>
      <td>1.05</td>
    </tr>
    <tr>
      <th>0</th>
      <td>kidney_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.535194</td>
      <td>0.90168</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>lentils</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.196738</td>
      <td>1.38504</td>
      <td>vegetables</td>
      <td>2.7161</td>
    </tr>
    <tr>
      <th>0</th>
      <td>lettuce_iceberg</td>
      <td>Fresh1</td>
      <td>0.242508</td>
      <td>0.309655</td>
      <td>1.21304</td>
      <td>vegetables</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>0</th>
      <td>lima_beans</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.797757</td>
      <td>1.38357</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>mustard_greens</td>
      <td>Fresh1</td>
      <td>0.308647</td>
      <td>0.944032</td>
      <td>2.56924</td>
      <td>vegetables</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>0</th>
      <td>navy_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.575997</td>
      <td>0.970423</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>okra</td>
      <td>Fresh1</td>
      <td>0.35274</td>
      <td>1.473146</td>
      <td>3.21355</td>
      <td>vegetables</td>
      <td>0.769474</td>
    </tr>
    <tr>
      <th>0</th>
      <td>olives</td>
      <td>Fresh1</td>
      <td>0.297624</td>
      <td>1.246102</td>
      <td>4.18683</td>
      <td>vegetables</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>onions</td>
      <td>Fresh1</td>
      <td>0.35274</td>
      <td>0.406868</td>
      <td>1.03811</td>
      <td>vegetables</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pinto_beans</td>
      <td>Fresh1</td>
      <td>0.385809</td>
      <td>0.514129</td>
      <td>0.86619</td>
      <td>vegetables</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>potatoes</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.184017</td>
      <td>0.56432</td>
      <td>vegetables</td>
      <td>0.811301</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pumpkin</td>
      <td>Fresh1</td>
      <td>0.540133</td>
      <td>0.730411</td>
      <td>1.35228</td>
      <td>vegetables</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>radish</td>
      <td>Fresh1</td>
      <td>0.275578</td>
      <td>0.401618</td>
      <td>1.31163</td>
      <td>vegetables</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>red_peppers</td>
      <td>Fresh1</td>
      <td>0.264555</td>
      <td>0.734926</td>
      <td>2.27794</td>
      <td>vegetables</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>0</th>
      <td>summer_squash</td>
      <td>Fresh1</td>
      <td>0.396832</td>
      <td>0.845480</td>
      <td>1.63948</td>
      <td>vegetables</td>
      <td>0.7695</td>
    </tr>
    <tr>
      <th>0</th>
      <td>sweet_potatoes</td>
      <td>Fresh1</td>
      <td>0.440925</td>
      <td>0.499400</td>
      <td>0.918897</td>
      <td>vegetables</td>
      <td>0.811301</td>
    </tr>
    <tr>
      <th>0</th>
      <td>turnip_greens</td>
      <td>Fresh1</td>
      <td>0.31967</td>
      <td>1.053526</td>
      <td>2.47175</td>
      <td>vegetables</td>
      <td>0.75</td>
    </tr>
  </tbody>
</table>
<p>63 rows × 7 columns</p>
</div>



__Exercise 1.4.__ Discuss the questions below (a paragraph each is sufficient). Use plots to support your ideas.

* What kinds of fruits are the most expensive (per pound)? What kinds are the least expensive?
* How do the price distributions compare for fruit and vegetables?
* Which foods are the best value for the price?
* What's something surprising about this data set?
* Which foods do you expect to provide the best combination of price, yield, and nutrition? A future assignment may combine this data set with another so you can check your hypothesis.

1. Most expensive fruits are the berries (raspberries, blackberries, cranberries, blueberries) and figs/dates. The least expensive are bananas, watermelon, cantalope, and pineapple.


```python
fruit_df.sort_values(['price_per_lb'], ascending = 0)[:9]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>form</th>
      <th>lb_per_cup</th>
      <th>price_per_cup</th>
      <th>price_per_lb</th>
      <th>type</th>
      <th>yield_v</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>raspberries</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>2.322874</td>
      <td>6.975811</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blackberries</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>1.922919</td>
      <td>5.774708</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>figs</td>
      <td>Fresh1</td>
      <td>0.165347</td>
      <td>0.990068</td>
      <td>5.748318</td>
      <td>fruit</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>0</th>
      <td>dates</td>
      <td>Fresh1</td>
      <td>0.165347</td>
      <td>0.792234</td>
      <td>4.791351</td>
      <td>fruit</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cranberries</td>
      <td>Fresh1</td>
      <td>0.123163</td>
      <td>0.589551</td>
      <td>4.786741</td>
      <td>fruit</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>blueberries</td>
      <td>Fresh1</td>
      <td>0.319670</td>
      <td>1.593177</td>
      <td>4.734622</td>
      <td>fruit</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cherries</td>
      <td>Fresh1</td>
      <td>0.341717</td>
      <td>1.334548</td>
      <td>3.592990</td>
      <td>fruit</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>0</th>
      <td>berries_mixed</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>1.127735</td>
      <td>3.410215</td>
      <td>fruit</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>apricots</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>1.189102</td>
      <td>3.040072</td>
      <td>fruit</td>
      <td>0.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
fruit_df.sort_values(['price_per_lb'], ascending = 1)[:9]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>form</th>
      <th>lb_per_cup</th>
      <th>price_per_cup</th>
      <th>price_per_lb</th>
      <th>type</th>
      <th>yield_v</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>watermelon</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.212033</td>
      <td>0.333412</td>
      <td>fruit</td>
      <td>0.52</td>
    </tr>
    <tr>
      <th>0</th>
      <td>cantaloupe</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.393800</td>
      <td>0.535874</td>
      <td>fruit</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>0</th>
      <td>bananas</td>
      <td>Fresh1</td>
      <td>0.330693</td>
      <td>0.292965</td>
      <td>0.566983</td>
      <td>fruit</td>
      <td>0.64</td>
    </tr>
    <tr>
      <th>0</th>
      <td>pineapple</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.447686</td>
      <td>0.627662</td>
      <td>fruit</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>0</th>
      <td>honeydew</td>
      <td>Fresh1</td>
      <td>0.374786</td>
      <td>0.649077</td>
      <td>0.796656</td>
      <td>fruit</td>
      <td>0.46</td>
    </tr>
    <tr>
      <th>0</th>
      <td>grapefruit</td>
      <td>Fresh1</td>
      <td>0.462971</td>
      <td>0.848278</td>
      <td>0.897802</td>
      <td>fruit</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>0</th>
      <td>oranges</td>
      <td>Fresh1</td>
      <td>0.407855</td>
      <td>0.578357</td>
      <td>1.035173</td>
      <td>fruit</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>0</th>
      <td>papaya</td>
      <td>Fresh1</td>
      <td>0.308647</td>
      <td>0.646174</td>
      <td>1.298012</td>
      <td>fruit</td>
      <td>0.62</td>
    </tr>
    <tr>
      <th>0</th>
      <td>mangoes</td>
      <td>Fresh1</td>
      <td>0.363763</td>
      <td>0.705783</td>
      <td>1.377563</td>
      <td>fruit</td>
      <td>0.71</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_df.boxplot("type", "price_per_lb")
plt.show()
```
