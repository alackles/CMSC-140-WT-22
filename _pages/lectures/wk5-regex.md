---
title: Week 5 Day 2 - Regex
permalink: /lectures/wk5-d2
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---


Regular Expressions is a deep topic in computer science and in programming. Regex is not something I'm going to be able to teach you right off the bat! It's not something I always remember exactly how to do. But it's something I want to introduce you to so that when we start reading in strings from files next week, it'll be a tool in your toolbox. 

**I do not recommend using these lecture notes as a reference for regular expressions.** There are many, many, MANY better and more complete references out there, including the two linked below. 

Here's a link to [my favorite regex checker](https://regexr.com/), which is not Python-specific.

Here's a link to [another pretty good regex checker](https://regex101.com/), which you can set to be Python-specific.

For most use cases, there won't be any difference between the two.

# Live Code/Lecture

## Regex: General

Instead of me stumbling through an explanation of regex for you, I want to point you at a video that I think does an excellent job of explaining what a regular expression is regardless of programming language. We'll watch the first 12 or so minutes of it, pausing when people have questions. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/rhzKDrUiJVk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Using Regexes in Python

To use these regexes in Python, the process is pretty simple. First we have to import the regex module:

```py
import re
```

There are three basic parts to checking something with a regular expression. 

Let's use as an example the idea at the beginning of checking if someone has a valid Lawrence email address. 

### 1 - Compile the RegEx

First you have to tell Python what you want the regex to be, in regex terms. 

```py
email_regex = re.compile(r'[a-z\.]+@lawrence.edu')
```

### 2 - Check if it matches

Now, `email_regex` stores a piece of data that you can access to compare to a string. 

To check this match, try something like this:

```py
is_match = re.match(email_regex, "acacia.ackles@lawrence.edu")
print(is_match)
```

Now we can see how we can use this in a loop to check these emails. 

### 3 - Use the information somehow

```py
def email_checker(emails):
    for email in emails:
        if not re.search(email_regex, email):
            print(f"{email} is not a valid LU email!")
```

Go to In-Class Exercise 3 for some practice writing regexes.

## Other Features of the RE module

If there's time, here's a few additional features we'll cover:

- ignorecase: You can ignore the case of an entry with `re.IGNORECASE`, or passing `re.I` as an optional third argument ot `re.search()`.
- match: `re.match()` has the same syntax as `re.search()` but only searches the beginning of a string.
- findall: `re.findall()` has the same syntax as `re.search() but will return a list of matches instead of a True or False value.