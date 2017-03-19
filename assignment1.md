
Cynthia Lai <br>
1/22/2017<br>
I asked Edie Espejo for help.


## Part 1: The Doomsday Algorithm

The Doomsday algorithm, devised by mathematician J. H. Conway, computes the day of the week any given date fell on. The algorithm is designed to be simple enough to memorize and use for mental calculation.

__Example.__ With the algorithm, we can compute that July 4, 1776 (the day the United States declared independence from Great Britain) was a Thursday.

The algorithm is based on the fact that for any year, several dates always fall on the same day of the week, called the <em style="color:#F00">doomsday</em> for the year. These dates include 4/4, 6/6, 8/8, 10/10, and 12/12.

__Example.__ The doomsday for 2016 is Monday, so in 2016 the dates above all fell on Mondays. The doomsday for 2017 is Tuesday, so in 2017 the dates above will all fall on Tuesdays.

The doomsday algorithm has three major steps:

1. Compute the anchor day for the target century.
2. Compute the doomsday for the target year based on the anchor day.
3. Determine the day of week for the target date by counting the number of days to the nearest doomsday.

Each step is explained in detail below.

### The Anchor Day

The doomsday for the first year in a century is called the <em style="color:#F00">anchor day</em> for that century. The anchor day is needed to compute the doomsday for any other year in that century. The anchor day for a century $c$ can be computed with the formula:
$$
a = \bigl( 5 (c \bmod 4) + 2 \bigr) \bmod 7
$$
The result $a$ corresponds to a day of the week, starting with $0$ for Sunday and ending with $6$ for Saturday.

__Note.__ The modulo operation $(x \bmod y)$ finds the remainder after dividing $x$ by $y$. For instance, $12 \bmod 3 = 0$ since the remainder after dividing $12$ by $3$ is $0$. Similarly, $11 \bmod 7 = 4$, since the remainder after dividing $11$ by $7$ is $4$.

__Example.__ Suppose the target year is 1954, so the century is $c = 19$. Plugging this into the formula gives
$$a = \bigl( 5 (19 \bmod 4) + 2 \bigr) \bmod 7 = \bigl( 5(3) + 2 \bigr) \bmod 7 = 3.$$
In other words, the anchor day for 1900-1999 is Wednesday, which is also the doomsday for 1900.

__Exercise 1.1.__ Write a function that accepts a year as input and computes the anchor day for that year's century. The modulo operator `%` and functions in the `math` module may be useful. Document your function with a docstring and test your function for a few different years.  Do this in a new cell below this one.


```python
def anchorDay(year):
    remainder = year % 100
    century = (year-remainder)/100
    anchor = (5 * (century % 4) + 2) % 7
    return(anchor)

for year in [1, 2000, 1520]:
    print(anchorDay(year))
```

    2
    2
    3
    

### The Doomsday

Once the anchor day is known, let $y$ be the last two digits of the target year. Then the doomsday for the target year can be computed with the formula:
$$d = \left(y + \left\lfloor\frac{y}{4}\right\rfloor + a\right) \bmod 7$$
The result $d$ corresponds to a day of the week.

__Note.__ The floor operation $\lfloor x \rfloor$ rounds $x$ down to the nearest integer. For instance, $\lfloor 3.1 \rfloor = 3$ and $\lfloor 3.8 \rfloor = 3$.

__Example.__ Again suppose the target year is 1954. Then the anchor day is $a = 3$, and $y = 54$, so the formula gives
$$
d = \left(54 + \left\lfloor\frac{54}{4}\right\rfloor + 3\right) \bmod 7 = (54 + 13 + 3) \bmod 7 = 0.
$$
Thus the doomsday for 1954 is Sunday.

__Exercise 1.2.__ Write a function that accepts a year as input and computes the doomsday for that year. Your function may need to call the function you wrote in exercise 1.1. Make sure to document and test your function.


```python
def Doomsday(year):
    remainder = year % 100
    doom = (remainder + int(remainder/4) + anchorDay(year)) % 7
    return(doom)

for year in [1, 2000, 1520]:
    print(Doomsday(year))
```

    3
    2
    0
    

### The Day of Week

The final step in the Doomsday algorithm is to count the number of days between the target date and a nearby doomsday, modulo 7. This gives the day of the week.

Every month has at least one doomsday:
* (regular years) 1/10, 2/28
* (leap years) 1/11, 2/29
* 3/21, 4/4, 5/9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12

__Example.__ Suppose we want to find the day of the week for 7/21/1954. The doomsday for 1954 is Sunday, and a nearby doomsday is 7/11. There are 10 days in July between 7/11 and 7/21. Since $10 \bmod 7 = 3$, the date 7/21/1954 falls 3 days after a Sunday, on a Wednesday.

__Exercise 1.3.__ Write a function to determine the day of the week for a given day, month, and year. Be careful of leap years! Your function should return a string such as "Thursday" rather than a number. As usual, document and test your code.


```python
def leapYear(year):
    leap = False
    if year % 4 == 0:
        leap = True
    return(leap)

for year in [1, 2000, 1520]:
    print(leapYear(year))
```

    False
    True
    True
    


```python
daysWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
ddays = [10, 28, 21, 4, 9, 6, 11, 8, 5, 10, 7, 12]


def dayOfWeek(month, day, year):
    doomsYear = Doomsday(year)
    if leapYear(year):
        ddays[1] = 29
        ddays[0] = 11
    dayDistance = abs(ddays[month - 1] - day)
    weekDistance = dayDistance % 7
    index = (doomsYear + weekDistance) % 7
    return(daysWeek[index])

print(dayOfWeek(1,22,2017))
print(dayOfWeek(1,23,2017))
```

    Sunday
    Monday
    

__Exercise 1.4.__ How many times did Friday the 13th occur in the years 1900-1999? Does this number seem to be similar to other centuries?


```python
def friday13(startYear, endYear):
    years = range(startYear, endYear + 1)
    months = range(1,13)
    count = 0
    for year in years:
        for month in months:
            dow = dayOfWeek(months[month - 1], 13, year)
            if dow == "Friday":
                count += 1
    return(count)

print(friday13(1900,1999)) #172
print(friday13(1800,1899)) #170
print(friday13(1700,1799)) #173
# all pretty close
```

    172
    170
    173
    

__Exercise 1.5.__ How many times did Friday the 13th occur between the year 2000 and today?


```python
friday13(2000,2016)
```




    30



## Part 2: 1978 Birthdays

__Exercise 2.1.__ The file `birthdays.txt` contains the number of births in the United States for each day in 1978. Inspect the file to determine the format. Note that columns are separated by the tab character, which can be entered in Python as `\t`. Write a function that uses iterators and list comprehensions with the string methods `split()` and `strip()` to  convert each line of data to the list format

```Python
[month, day, year, count]
```
The elements of this list should be integers, not strings. The function `read_birthdays` provided below will help you load the file.


```python
def readBirthdays(file_path):
    """Read the contents of the birthdays file into a string.
    
    Arguments:
        file_path (string): The path to the birthdays file.
        
    Returns:
        string: The contents of the birthdays file.
    """
    with open(file_path) as file:
        return file.read()
```


```python
data = readBirthdays('birthdays.txt')
data = data.strip()
data = [data.split("\n")][0]
data = data[6:]

data = [entry.replace("\t","/") for entry in data]
data = [entry.split("/") for entry in data]

#print(data[1:10])

bdays = []
for entry in data:
    #print(entry)
    li = []
    for element in li:
        print(element)
        li.append(int(element))
    bdays.append(li)
```

__Exercise 2.2.__ Which month had the most births in 1978? Which day of the week had the most births? Which day of the week had the fewest? What conclusions can you draw? You may find the `Counter` class in the `collections` module useful.

__Exercise 2.3.__ What would be an effective way to present the information in exercise 2.2? You don't need to write any code for this exercise, just discuss what you would do.
