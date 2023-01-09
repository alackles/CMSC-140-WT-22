---
title: Week 2 Day 1 - If/Else
permalink: /lectures/wk2-if/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---


# If/Else and Match/Case

So far we've been looking at simple evaluations and expressions in Python. In today's class we're going really start to get into _control flow_: how to make your program make choices. 

**By the end of the class, you should be able to answer the following:**
- How do you use the boolean operators `and`, `or`, and `not`? What do they do? 
- What is the purpose of an `if` statement? 
- What is the difference between `elif` and `else`?
- How do you write a program that can choose between a variety of possible options and inputs? 

## Questions from the Reading

These are questions or themes compiled from Perusall to help guide our discussion before jumping into course content.



## Lecture/Live Coding

### Data types

There are two very basic types of data in Python that we're interested in: Numbers and Strings.

#### Numbers

Numbers come in two basic formats: **integers** and **floating points**.

Integers are numbers without any decimals. E.g. `5`, `7`, `8`.

Floating point numbers, or floats, are numbers with decimal places. E.g. `5.4`, `2.0`, `-1.4`

In most languages, integers and floating point numbers are treated very differently. For example, dividing two integers will always produce an integer. In Python, this isn't the case. They act more like you usually assume numbers to act; they are interchangeable in most contexts. 

#### Strings

Strings are basically words or collections of words. 

Strings can have spaces, numbers, and can be added together (called _concatenation_)

```py
my_string = 'Python is cool'
my_string = 'cmsc140`
my_string = 'hello ' + 'friend'
```

You can use either single or double quotes to note strings, but they have to match. If you want to put a single or double quote _inside_ a string, you can use an escape character like this:

```py
my_string = 'What\'s the temperature?`
```

This tells Python to interpret the apostrophe as a literal character, not a command.

### Interactions between Types

Try this yourself.

Can you add together an int and a float?

```py
num1 = 5
num2 = 4.2
num3 = num1 + num2
print(num3)
```

What about a float and a string? 

```py
apples = 20
sentence = "There are " + apples + "apples."
print(sentence)
```

Strings and integers don't add together because the operation `+` isn't well defined. The program isn't sure whether you want it to return a number or a sequence of letters, so it does neither.

### Conversions Between Type

In Python, it's easily possible to convert between types. For example, to change an integer or float into a string, simply use `str()`.

```python
my_variable = str(4.5)
print(my_variable)
```

It may seem initially as though nothing has changed. But try the following:

```py
apples = 20
sentence = "There are " + str(apples) + "apples."
print(sentence)
```

Now you're able to add them together, because you're being very clear about what you want.

What about something like this?

```py
apples = int("apples")
```

This kind of conversion isn't well-defined in Python. You could certainly create a conversion, but Python doesn't have one by default because it's not obvious what that would be. 

### Some Basic Functions

Here are some basic built-in functions that will help you complete various tasks:

User input can be handled by

```py
a = input()
print(a)
```

By default inputs come in as strings, even if they are numbers. 

As the program is executing, it will stop when it gets to an input line. But it won't tell you that by default, so it's important that you let the user know that that's why the program is idling. 

We have already used print a few itmes, but to be very explicit, you can do the following for pretty much any structure in Python. 

```py
my_list = [3, 4, 5]
print(my_list)
my_string = "My string!"
print(my_string)
my_dict = {1: "Hello", 2: ["another", "example"], 3: 4}
print(my_dict)
```

**This is one of the most popular and powerful features of Python.** In other languages you will often bang your head against the wall just getting something to print in a way that makes intuitive sense to you.

### Booleans

Boolean expressions are a type of expression in computer science. Just like an entity can be a number or a string, it can be a _boolean_. 

```py
my_num = 7 # a numeric value
my_string = "CMSC 140" # a string
my_bool = True # a boolean

```

Unlike numbers and strings though, which can take on an infinite number of values, booleans can only take on two values: `True` or `False`. 

This may not sound very useful, but it's really the key cornerstone of programming! Many, many, many times, you will be checking whether something is `True` or `False` and using that information to make choices in your program. 

#### Boolean Operators

There are three main boolean operators:

- `and`: Evaluates to `True` if both values are true
- `or`: Evalutes to `True` if either value is true
- `not`: Flips the value (True becomes False, False becomes True)

#### Comparison Operators

You can also create boolean values out of comparison operators. 

- `<`, `<=`, `>`, and `>=` act as you expect them to from mathematics
- `==` checks equality
- `!=` checks not-equal
  
**Go to Exercise 1.**

## Control Flow

Control flow is basically a term for things the program does that is not just reading and evaluating expressions as they are typed in. There is some input that triggers the evaluation of certain pieces of the code, called blocks.

This is powerful because it means the same code can be made to do many different things depending on the input, which makes it reusable for many more cases. 

In today's class we'll be looking at `if` statements and `match` statements. Both of these basically use the boolean value of something to decide whether or not to execute. 

### If Statements

`if` statements are lines of code with the following structure

```
if {statement is true}:
    {do something}
```

Here is a very basic example that will always execute:

```py
if True:
    print("Hello!")
```

Here is an example that will never execute:

```py
if False:
    print("Secret message that you won't see.")
```

Note that this is effectively no different than just writing `print("Hello")` in the first case, and writing nothing in the second case. So here is a more realistic example. 

```py
i = 0
if i == 0:
    print("i is equal to 0")
```

Anything you could do outside an `if` statement, you can do inside an `if` statement.

```py
i = 7
if i < 10:
    i = 10
    print(2 + 2)
    y = 25
    if 7 == 7:
        print("7 is 7")
print(i)
print(y)
```

### Else Clauses

You can choose to have your program do more than one thing based on the value of your if statement. 

You can add an `else` clause, which will only evaluate if the `if` clause is False. 

```py
example = 10
if example < 10:
    print("Small number.")
else:
    print("Big number.")
```

What will print if I change `<` to `<=`?

### Elif Clauses

You can similarly chain together these statements with `elif` to create a long chain of flow if there is more than one value you could take as input. 

```py
class_code = 140
if class_code == 140:
    print("This is Python Programming.")
elif class_code == 150:
    print("This is Java Programming.")
elif class_code == 270:
    print("This is Data Structures.")
elif class_code >= 200:
    print("This is an upper-level class.")
elif class_code >= 400: 
    print("This is an advanced class.")
```

You can add an `else` clause at the end to catch all other cases, but this is not required. 

What will print if I set `class_code` to 500? 

Go to in-class exercises.

## In-Class Exercises

### Exercise 1: Booleans

On your whiteboards with your group:

1. Write an expression that uses `<` and evalutes to `True`.
2. Write an expression that uses `or` and `!=` and evalutes to `True`.
3.  Write an expression that uses `and`, `>=`, and `==` and evaluates to `False`.

### Exercise 2: Calculator

With your groups:

We're going to write a very simple caluclator in Python. This calculator takes two numbers from the user and asks them whether they want to add, multiply, divide, or subtract them. Then it performs the correct operation and prints the value. 

Below is what your program's output should be, including user input. It's up to you to write the internals!

```
Welcome to the calculator. 
Enter number 1: 8
Enter number 2: 4
Enter operation [a, s, d, m]: d
8 divided by 4 is 2.
```

Hint: Start _small_ and _build up_. 

You know how to print something stored in a variable, and you know how to take input and store it in a variable. Can you take two numbers from the user and just print them out? 

Can you ask what operation they want and store that in a variable? Take it one step at a time.

-------

_Footnotes:_


[^1]: It _sort of_ matters. The expression on the left side of `and` will be evaluated first, so if it evaluates to `False`, the expression on the right will never be evaluated. This can be useful in certain specific cases where you are checking whether something is true that may be very computationally intensive. This won't come up in this class, but just in case you are curious about the finer details!