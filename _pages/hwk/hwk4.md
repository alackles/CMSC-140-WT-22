---
title: Homework 4 - Strings
permalink: /hwk/hwk4
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# Homework 4: Strings and Arrays

The puprose of this homework is to get additional practice with strings and lists, and working with them in Python. This is just a single small project.  

Make sure to follow the [collaboration policy][collab] for all homework.

## Assessment

For **Proficiency** credit, your submissions must pass all the test cases on Gradescope.

For **Mastery** credit, your submission must pass all test cases, and also have:

- Useful, informative variable names 
- Clear and consistent spacing/linebreaks
- At least one function that you have written that _returns_ a value

## Q1: `q1.py`


You will be given an integer `n`, followed by `n` words, each on their own line. Your job is to read in the input, and then output:

1. How many duplicate words there are
2. What the duplicate words were, in alphabetical order

Importantly, words that are capitalized differently should be considered to be the same word and treated accordingly. The duplicate words should be output in alphabetical order.

Example input:

```
5
apple
zebra
Bear
ZEBRA
bear
```

Example output:

```
2
bear
zebra
```