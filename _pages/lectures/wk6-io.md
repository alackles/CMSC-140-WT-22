---
title: Week 6 Day 2 - Basic File I/O
permalink: /lectures/w6-d2
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

Time to start loading in outside data! We're going to be spending some time on this because it's something you'll have to do very often in day-to-day applications of programming. 

# Questions from the Reading

> What kinds of files can I read/write in Python?

> 

# Lecture/Live Code

Just as you can open a file on your computer, make some changes to it, and then save that file, you can do the same inside Python itself. 

There are three basic steps to doing so, and they're the same steps you use when you're doing things manually.

1. Open the file
2. Read something from and/or write something to the file
3. Close the file

## Python Pathing

Windows and Mac have different ways of writing file paths. Windows uses a backslash `\` while Mac (and Linux) uses a forward slash `/`. 

Python has ways to handle these discrepancies so that your code will work on any computer. We use the `Path` module. 

```py
from pathlib import Path
```

Notice that we're using a `from ... import` construction here. This is because we're only using a single function from `pathlib`, called `Path`, so we want to be able to call it without needing to specify the import slug beforehand. 

If this is confusing to you, you can do 

```py
import pathlib
```

And any time you need to use `Path()`, you can use `pathlib.Path()` instead.

The Path function takes a string representing a path in your computer and processes it for whatever operating system your code is running on. 

Here's an example. 

```py
home_dir = "/home/acacia"
home_path = Path(home_dir)
```

You can add to this homedir path with a forward slash:

```py
new_path = home_path / "Documents"
```

But at least one of the objects here must be a Path object. 

You can chain them, but at least one of the first two objects has to be a Path object. 

This makes it safe to run your code on any computer. A common thing to do is to make the base path to the project a string that the user can change at will, and then have folders that you provide stuck on the end so if they download your code, it will run with only one change. 

Example:

```py
from pathlib import Path
path_to_proj = "home/acacia/Documents/teaching/AY-22-23/fall/CMSC140/"
base_path = Path(path_to_proj)
pages_path = base_path / "_pages"
syllabus = base_path / "syllabus.md"
hwk_path = pages_path / "hwk"
```

## Working with Files 

### Opening Files 

You can open files in Python by calling the `open()` function, where the argument is the path to the file. 

As an example, create a file called `hello.txt` in the same folder as your current python script. Write some text in it; anything you want. Then, you can do the following:

```py
hello = open('hello.txt')
```

Now, if you print `hello`, what do you expect to be in there?


### Reading Files 

To read the contents of a file, we need to call another function called `.read()` or `.readlines()`, depending on how you want to save your file. 

```py
file_contents = hello.read()
file_contents_list = hello.readlines()
```

### Writing Files

To write to a file, we need to explicitly tell Python we want to be able to write to it. The reason for this is that by default, Python will open files in _read only_ mode to protect you from doing something you don't want to do. (Unlike most interfaces you're used to using, there's no "are you sure?" in Python; it will just do whatever you ask.)

You can either overwrite the file contents entirely, or append to them.

To append, you should open the file in append mode.

```py
hello = open('hello.txt', 'a')
hello.write("here's some new content")
```

To overwrite, you should open the file in write mode.

```py
hello = open('hello.txt', 'w')
hello.write("here's some new content")
```

If you want to read in one of those modes, you have to use `w+` or `a+` instead.

### Closing Files

Finally, we need to make sure we close our file when our script ends. The reason for this is that when you run the script, if you don't close the file, it'll just keep hanging out in memory. This is okay when you're using a standalone script, but a very bad habit to get into for when you eventually want to start loading programs into other programs. 

So whenever you have an `open()`, make sure you also do a `close()`.

```py
hello.close()
```


### With Open 

It's extremely easy to forget to close the file. That's why most of the time what you'll want to use `with open()` instead. It's a code block that automatically closes the file as soon as the code block is finished executing. 

```py
with open("hello.txt", 'a') as f:
    file_content = f.readlines()
print(file_content)
```

Notice that outside the `with open` block, you can work with the contents as normal. 

Go to In-Class Exercise 1.

## Files Line-by-line

Often times, you'll have files that have some kind of data in them that you're interested in processing one line at a time. For example, maybe you collected some data for a sociology class comparing the temperature outside on a given day to the number of people you noticed wearing hats. Your data looks  something like this

```
temp hats
72 2
42 18
60 19
77 5
88 4
21 20
38 22
```

Now you want to plot temperature vs. hats and see if there's any correlation. 

First, we would want to make lists of each of the values. But how do we do that if we're reading a file line by line?

Remember that readlines() returns a list of strings where each string is a line in the file. 

Here's some code to do so:

```py
temps = []
hats = []
with open("hats.txt") as f:
    next(f) # this allows us to skip the first line, which is header text
    for line in f.readlines():
        t, h = line.split(" ")
        temps.append(t)
        hats.append(h)
```

To plot these now, we can use matplotlib's plot function, which when given two lists plots them as x and y coordinates.

```py
import matplotlib.pyplot as plt
plt.plot(temps, hats)
plt.show()
```

Go to in-class exercise 2.

# In-Class Exercises

## Exercise 1

These are some randomly generated names. 

Copy the following into a file on your computer called `names.txt`. 

Using Python's file handling methods:

1. Print out the names to the console, separated by newlines
2. Add your name to the end of the file

```
Kajetan Phan
Ameer Alexander
Woodrow Hill
Winnie Holding
Kathryn Stacey
Tyra Gilmour
Steve Markham
Grant Olson
Elowen Blair
Mcauley Duran
```
