---
title: Week 3 Day 1 - Lists and Dictionaries
permalink: /lectures/w3-d1
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk3-listdicts.py).

# Loops

## In-Class Exercise

To warm up and refresh our memories from last class, we'll start with a two-part in-class exercise. 

Take 10 minutes to silently and individually work on the following problem. Then, take 5 minutes to discuss with your group. At the end, we'll all come together to look at some solutions. 

It is okay, and even expected, if you don't finish within 10 minutes. It is also okay if you don't come to an answer with your whole group. 

**Question:** Write a Python program that stores a random number (you can pick the number) and asks the user for an input. If the user's number is too low, print the message `Too low!`, and ask the user to guess again. If the user's number is too high, print the message `Too high!`, and ask the user to guess again. If the user's number is equal to the stored number, print `You guessed it!`, and the guessing should stop.

If you're stuck, try breaking the problem into smaller steps. Here are some possible steps:

1. Make sure you can get input from the user
2. Make sure you can compare that input to a number you have saved
3. Make sure you can make all the comparisons that the problem asks for
4. Figure out how to repeatedly ask for input until some condition is met (what is the condition)? 

## Questions from the Reading

> If you have nested lists, can you access two elements with a single call? For example, is there a single call to get "bear 6" out of this?:
> ```python
> A = [["cat", "bat", "bear"], [1, 5, 6]]
> ```

## Lecture/Live Coding

### Lists

Creating a list is as simple as putting multiple values into square brackets, separated by commas.

```py
my_list = [1, 3, 5, 8, 3, 2]
print(my_list)
```

You can have lists of any type, and you can mix types. 

```py
my_mixed_list = [2, "green", 2.4, True]
print(my_mixed_list)
```

To get a single value out of a list, you use square brackets to indicate which element you want.

```py
a = my_list[1]
print(a)
```

Notice this evaluates to 3; this is because, like with ranges, lists are 0-indexed.

```py
b = my_list[0]
print(b)
```

You can also use negative indices in lists to count backwards, but these don't start from 0 (because negative 0 is 0)

```py
classes = ["CMSC", "MATH", "STAT", "BIOL", "ART", "MUS"]
print(classes[-1])
print(classes[-2])
```

Finally, if you want a chunk of a list, you can use list slices:

```py
print(classes[0:5])
print(classes[1:2])
```

You can also leave off the first or second number if you want everything to the end or everything from the start:

```py
print(classes[:2])
print(classes[2:])
```

### Modifying Lists

You can modify lists by accessing them at particular indices. Here's an example.

```py
print(classes)
classes[0] = "PHYS"
print(classes)
```

You can even use one part of a list to modify another part.

```py
classes[1] = classes[0]
print(classes)
```

### Concatenation and Loops

Lists can be concatenated, like strings:

```py
list_a = ['a','b','c']
list_b = ['x','y','z']
final_list = list_a + list_b
print(final_list)
```

You can use this to build up a list piece by piece:

```py
numbers = []
for i in range(5)
    numbers = numbers + [i]
    print(numbers)
```

Speaking of for loops, you can actually use a for loop over a list:

```py
for item in final_list:
    print(item)
```

Or something like this:

```py
nums = [1, 3, 4, 8]
for i in nums:
    a = i**2
    print("Square of", i, "is", i**2)
```

### Methods on Lists

There are some things we want to do to lists directly without creating a new list. Two of the most common things we might want to do are add to a list and sort a list. 

```py
example_list = []
example_list.append(4)
print(example_list)
example_list.append(2)
example_list.append(1)
example_list.append(3)
```

Notice we don't assign it back to itself. That's because when we're using a method it's doing something directly to the list, as indicated by the `.`. Not all functions can be used as methods.

We might also want to sort a list:

```py
example_list.sort()
```

Which changes the list in-place. 


### Dictionaries

Dictionaries are a lot like lists, but instead of having numerical indices, they can have any type of index. This index is called a _key_, and the thing stored at that key is called a _value_. 

Compare these two structures:

```python
my_list = [2, 3, "hello", [4, 5]]
```

```python
my_dict = {
    0: 2,
    1: 3,
    2: "hello",
    3: [4, 5]
}
```

These store the exact same data in the exact same way, and are accessed the same. `my_list[0]` and `my_dict[0]` both give you `2`.

The difference is you can change the labels of `my_dict` to be anything you want (except for a list or a dict).

```python
my_dict = {
    False : 2,
    "bananas": 3,
    "greeting": "hello",
    3.4: [4, 5]
}
```

The time this is most useful is if you want to access something via a label. Often you will store values in a dictionary when you don't need to iterate through the entire data structure every time, but you need to be able to access information at particular locations. For example, you could store everyone's ID numbers and access them by name. 

```python
student_names = { 
    "Acacia": 2830084,
    "Kurt": 1919182,
    "Joe": 89483929,
}
name = input("What is your name?")
print("Your ID number is", student_names[name])
```

You _can_ also iterate through every entry in a dictionary, through every key, and through every value. But for now, we are going to think of dictionaries as structures to access data one piece at a time, instead of iteratively. If you just want to iterate, you can probably use a list. 

