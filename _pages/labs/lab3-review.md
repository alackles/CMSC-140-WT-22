---
title: Lab 3 - Review
permalink: /labs/lab3/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# Overview

The purpose of this lab is to give you a chance to practice the skills you've learned throughout the course thus far with some smaller practice problems. 

The idea here is to give you a chance to figure out what you don't yet understand. Below is a list of many different problems; for each section, you only have to pick a few to answer, but you should try to pick the ones that you don't immediately think 'oh, I know how to solve that.'

**This is an individual lab**, and is graded on how many problems you complete _accurately_. The idea is just to get some practice with a wide variety of problems. 

You will notice there is also no sample input or output for these problems. You'll have to come up with your own sample input/output to test your programs. 

If a problem says "take an input from the user", you should use `input()`. 

If a problem does not specify, you can either use `input()` or use a fixed input in the code itself.

## Instructions

Turn in your lab to gradescope. There is no autograder for this lab, so formatting your output precisely doesn't matter so long as it follows what the question is asking. 

Gradescope expects a single file to be uploaded. You can combine all of your answers into one file, or have separate files that you put in a zip folder. 

No matter what, be sure you have comments indicating which question you are working on. (E.g. `#set B question 1`)

## Assessment

For **Proficiency** credit, you should complete 2 problems from Sets A and B and 1 problem from Set C. All of your programs should accomplish what is asked in the question.

For **Mastery** credit, you should complete 3 problems from Sets A and B and 2 problems from Set C. All of your programs should accomplish what is asked in the question.

# Questions

## Set A: If/Else

1. Write a program to accept two numbers from the user. Return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
2. Given two values, print their sum. However, if the two values are the same, then print double their sum.
3. Given an int `n` and a second int `y`, print `True` if `n` is within 10 of `y`. (That is, if `y = 200`, the numbers 190, 191, 192, .... , 208, 209, 210 should all print `True`, and all other numbers should print `False`). 
4. Given 2 ints, `a` and `b`, print `True` if one if them is 10 or if their sum is 10.

## Set B: Loops

1. Fibonnaci: Write a program that takes an input `n` from the user and prints out the first `n` numbers of the Fibonacci sequence. The Fibonacci sequence is created by starting with two 1s and adding the previous two numbers together: `1, 1, 2, 3, 5, 8, 13, 21, ...`
2. Fizzbuzz: Write a program that prints out the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead. If it is divisible by 5, print "Buzz" instead. If it is divisible by both 3 and 5, print "Fizz Buzz".
3. Write a program that asks the user to guess Heads or Tails, and then randomly "flips" a coin (using `random`) and tells the user whether they hvae won or lost. 
4. Write a program that creates the following pattern using a nested `for` loop:

```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
```

(There are 9 rows here and 5 columns)

## Set C: Lists 

1. Given some list of all integers, print how many even numbers are in the list.
2. Write a program that, given some list, swaps the first and last elements. 
3. Write a program that, given some list, creates a new list where each element is turned into a string and has a "!" added to the end.