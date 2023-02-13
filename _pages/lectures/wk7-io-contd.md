---
title: Week 7 Day 1 - More File I/O
permalink: /lectures/w7-d1
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

More file loading!

Today's class is going to be primarily **practical**: we'll talk a little bit about some of the things we missed from last class, do a little review, and then you'll spend the class working with data.
## Pandas

Reading in tabular data like this is a very common use of Python, so there are a lot of prewritten modules that make it easier to do things like this. 

One of them is pandas, which handles files in CSV format. CSV file format is basically how things like excel spreadsheets are stored. If you've used R, you'll be familiar with a lot of the syntax of Pandas.

Pandas has a lot of features, so we'll just look at a few of them. Here's a good supplementary guide to these notes if this all makes good sense to you, or if you have some experience with R and want to know how to do similar things in Python.

[Supplement.](https://medium.com/bhavaniravi/python-pandas-tutorial-92018da85a33)

### Installing Pandas

First we have to install Pandas with

```
pip3 install pandas
```

Check if it's installed by running a python script with the following:

```py
import pandas as pd
prof_info = {
    "Ackles" : {
        "classes": ["Python", "Algorithms"],
        "office": "Steitz 131",
        "firstname": "Acacia"
    },
    "Krebsbach" : {
        "classes": ["Java", "FYS"],
        "office": "Briggs 411"
    },
    "Gregg" : {
        "classes": ["Web Devel", "Algorithms"],
        "office": "Briggs 413"

    }
}
df = pd.DataFrame(data=prof_info)
print(df)
```

Now we have a table with all of this information, instead of a dictionary. 

### Reading to Pandas

We can read an entire file directly into a pandas dataframe with `read_csv`.

Take the example of the temps file from earlier.

```py
hattemps = pd.read_csv("hats.txt", sep = " ")
```

Note that it doesn't actually have to be a csv, just saved in csv format.

Note also that this automatically detects the header row!

### Working with Data

There are many, many things you can do with data in Pandas. Here are a few common ones. 

Indexing:

```py
templist = df["temps"]
temp = df["temps"][4]
```

Or `.loc` and `.iloc`

```py
t1 = df.loc[2, "temp"]
t2 = df.iloc[2, 0]
```

Changing names:

```py
df = df.rename(columns={"hats": "num_hats"})
```

or

```py
df.rename(columns={"num_hats": "hats"}, inplace=True)
```

Same for rows, but use _index_.


Creating columns from other columns:

```py
def isWarm(temp):
    return row['temp'] > 70

df['warm'] = df.apply(lambda row: isWarm(row), axis =1)
```

### Writing from Pandas

Finally, we can write out from pandas to a new file.

```py
df.write_csv("new_temps.csv")
```

## In-Class Exercise

Produce a visualization of some of the data from any of the CSV files at [this site](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html). You can create a bar graph, a line graph, a pie chart -- whatever you want! Here's the [matplotlib site](https://matplotlib.org/stable/plot_types/index.html) where you can see some popular kinds of plots you might want to make. 

Go wild with it in your groups, and then after a few minutes you'll share with each other. Then, each group will pick one visualization to share with the class. 