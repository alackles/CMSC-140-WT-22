---
title: Week 4 Day 1 - Functions
permalink: /lectures/w4-d1
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk3-listdicts.py).

# Functions (void)

## Questions from the Reading

> What if I wanted to use the same local variable in two functions? How would I do that? 

> Can I call a local and global variable the same name?

> How does Python know that a local variable doesn't exist if it is being read line by line in this example?
> ```python
> spam = 20
> def spammer():
>    print(spam)
>    spam = 5
> ```
> 

## Lecture/Live Coding

We've so far looked at programs that have all their code organized in the body of the script. Sometimes we have functions that we call, like `print()` or `input()` that do something specific for us. We can write our own functions too, though. 

This is the example given in the book, modified a little

```python
def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")

def hello_three():
    hello()
    hello()
    hello()

hello()
hello_three()
```

Key things to note here are:
- There is no assignment needed when a function is called, just like there is no assignment needed when `print()` is called. It just does what is asked of it.
- A function can consist of nothing but calling other functions
- functions are not executed when they are written; functions are executed when they are called

### Parameters and Arguments

A **parameter** is a special name given to a variable that is defined in a function definition. In the function below, the parameter is _my_string_.

```python
def excite(myString): 
    print(myString + "!!!!!!")
```

You can give multiple parameters to a function and use them both.

```python
def dashes(a, b):
    print(a + "-" + b)
```

```python
dashes("one","two") # would print "one-two"
```

Note that you have to be pretty sure about what kind of data you're giving a function, because Python doesn't force you to tell it what type you want. If you give it the wrong type, it'll throw an error.

```python
dashes(1, 2) #cannot concatenate int and str 
```

An **argument** is the name given to what we actually pass in to the function when it is called (not defined). In the function call below, the argument is the string _"Hello"_. 

```python
excite("Hello");
```

You can pass in variables as arguments, too. 

```python
h = "Hello"
excite(h)
```

### Scope and Stack Diagrams

In addition to naming a group of related commands and making them easier to call, creating a new function actually creates a new _scope_, or basically a little world of its own. So the variables that exist in one function have no effect on the variables that exist inside another function. 

Consider the following example.

```python
    def print_time(hour, minute):
        example_num = 0
        print(str(hour) + ":" + str(minute))
        print("print_time i", example_num)
    
    example_num = 20
    hour = 11
    minute = 59
    print_time(hour, minute)
    print("global i", example_num)
```


Even though the variable `example_num` is declared in both print_time and the script body, they are two completely different variables, the same way that the variable `hour` that is declared in the definition of print_time is different than the `hour` declared in the script body.

One way you can think of different functions is as boxes with little glass windows cut out. All the boxes for functions are in a larger box, the class. Different functions can look into each other, ask them to do something, and see the answer, but they cannot actually go in and change the things in the boxes, and they can't take things out of the boxes. They are self-contained worlds. 

Another way of looking at this is through a _stack diagram_, which is a drawing or visual representation of the variables and objects contained in your code. There are some handy tools to generate these that can be very useful for debugging your code. One example is [here](https://pythontutor.com/python-debugger.html). 

## In-Class Exercise

Turn the following question from your homework 1 into a function which takes two _parameters_, `start` and `step`, and prints the coutdown. Call that function with arguments that you take in from the user. 

Write a program that takes in two numbers and counts down from the first number (`start`) by the second number (`step`) until you reach 0. Do not print any numbers less than or equal to 0. 