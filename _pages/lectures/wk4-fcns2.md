---
title: Week 4 Day 1 - Functions with Returns
permalink: /lectures/w4-d1
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

Find the code for class [here](https://github.com/alackles/CMSC-140-WT-23/tree/main/_pages/lectures/code).

# Functions (with Returns)

Last class we looked at functions that printed something. The function was basically a way to organize a bunch of code into one place. 

Now we're looking at functions that _return_ something. These functions will be a way to organize a bunch of code into one place, and then _save the result_ of that execution somewhere. 

## In-Class Exercise Warm-Up

The quadratic formula is a simple way to find the roots of a polynomial function of the form

$$f(x) = ax^2 + bx + c$$

That is, if we set `f(x) = 0` and solve the equation for `x`, we get:

$$ x = \frac{-b \pm \sqrt{b^2-4ac}}{2a} $$

The part of the quadratic formula under the radical (square root sign) is called the _discriminant_. 

Write a program with a function called `discriminant()` that takes `a`, `b`, and `c` as arguments and prints out the discriminant (`b^2 - 4ac`). 

Your program should take `a`, `b`, and `c` as input from the user. 


## Questions from the Reading

> Why would I need to choose not to print a newline? 

> How does the call stack actually work? That part was confusing. 

> What is the point of setting variables in the function parentheses? 

## Lecture/Live-Code

### Returns

Last class we talked about functions that just print something, like this:

```python
def greeting():
    print("Hello")
```

We could also give parameters to these functions and print something out:

```python
def adder(x, y):
    mysum = x + y
    print(mysum)
```

When we call these functions, their values are directly printed.

But what if we wanted to use these values elsewhere? Like if we calculate some kind of intermediate step?

Say for example we want to convert between Fahrenheit and Celsius

```python
def f_to_c(f):
    c = (f - 32)*(5/9)
    print(round(c))
```

This is good if we just want to get the value once and display it. But maybe we also want to run some sort of check like this:

```python
if temp < 0:
    print("Freezing!")
elif temp < 10: 
    print("Cold!")
elif temp < 20:
    print("Warm!")
elif temp < 30:
    print("Hot!")
else:
    print("Scorching!")
```

How do we actually use the temperature we calculated? 

What we have to do is _return_ the value not print it, so it can be saved. 

```python
def f_to_c(f):
    c = (f - 32)*(5/9)
    return round(c)
```

Now we can save it into a variable:

```
temp = f_to_c(90)
```

And we can use this in the rest of our code. 

Here's the full program:

```python
def f_to_c(f):
    c = (f - 32)*(5/9)
    return round(c)

temp = f_to_c(90)

if temp < 0:
    print("Freezing!")
elif temp < 10: 
    print("Cold!")
elif temp < 20:
    print("Warm!")
elif temp < 30:
    print("Hot!")
else:
    print("Scorching!")
```

Anything can be returned from a function: a string, an integer, even a list. A list is a good way to return multiple values from a function. 

### The Call Stack 

These are helpful to understand, but not strictly necessary. Here are the basics:

The call stack is a term for the order in which Python executes operations. As I alluded to last class, functions are run at the place where they are called, not at the place where they are written. 

```py
print("Start of Script.")

def outer_function():
    print("Outer Function Called.")

print("After function definition.")

outer_function()

print("After function called.")
```

However, it's also important to know that this is also true when functions are placed _inside other functions_. We've actually already seen that this is true with the `print()` function, but let's make it more explicit with our own defined functions.

```py
print("Start of Script.")

def outer_function():
    print("Outer Function Called.")
    inner_function()
    print("Outer Function Ends.")

def inner_function():
    print("Inner Function Called.")
    print("Inner Function Ends.")

print("End of Script.")
```

This order of execution is what's referred to as the call stack. It is handled behind the scenes and you usually don't have to worry too much about it, except to know when certain things will execute. 

## In-Class Exercise

Modify your program from the beginning of class so that the function `discriminant()` now _returns_ the discriminant, rather than printing it. 

Then, write a second function called `quadratic()` which also takes three arguments: `a`, `b`, and `c`. It should then calculate both roots of the quadratic formula, and return them in a list. 

quadratic() should call the discriminant() method you wrote.

As an example, the inputs `a=1, b=-2, c=-8` should return `[2.0, 4.0]`. 

This exercise is intentionally vague. I want you to get used to where to apply certain concepts, to try things, work through them, get stuck, and get help from your group. If you get really, really stuck, I can give you a hint to nudge you along, but you can do this! Every piece of this is something we have learned in class. 

Hints: 

- Recall that you can square a number by simply multiplying it by itself
- Remember that to do a square root operation, you will have to import the `math` module. 
- Right now, you don't have to worry about equations with imaginary roots (where the discriminant is negative). Just make sure it works on the example input.
