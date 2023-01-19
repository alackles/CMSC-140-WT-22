---
title: Homework 1
permalink: /hwk/hwk1/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

The purpose of this homework is to get further practice with user input, if statements, and loops -- basically, to put together everything you have learned so far. 

On this homework, the problems will be relatively short, but there are many of them, because early on in learning programming (or any new language) doing small projects to reinforce the concepts is helpful. 

Note that questions 1-8 are programming assignments with expected input and output that the autograder will give you feedbakc for. Question 9 is also a programming assignment, but is more open-ended and will not be autograded. 

For **Proficiency** credit:

- Your code should pass all the test cases on Gradescope
- Your code for question 8 should do what you describe that it does

For **Mastery** credit:
- Your code should be well-organized with good and informative variable names
- Your code should have consistent spacing

## Submission Instructions

To make your life, and my life, easier, there are a few submission instructions you should follow to submit your homework to gradescope. 

1. **Each problem has its own assignment on gradescope**. Be sure to submit question 1 to HWK1: Q1, and question 2 to HWK2: Q2, and so on. 
2. **Every submission should be named with the question number and the letter q.** For example, for question 3, the file should be called **`q3.py`**.
3. **Follow the requested print statements exactly.** The autograder is not very intelligent; it just gives input and asks for expected output. I will be reading and giving feedback on your code as a human, but to give you the opportunity to see whether your code is working, the autograder gives feedback too. 

Some general reminders:
- Make sure to **save your code** before running it, and before submitting it. 
- If you are having problems, start small and build. Is there any piece of the problem you think you could do, even if it is just "read a number"? Is there a second piece you can do, like "read a number and add to it"? 

## Questions

### Q1

Write a program that takes a number from the command line and outputs the string `"even"` if the number is even, and `"odd"` if the number is odd. No text prompt for the number is needed.

Example:

```
> 9
odd
```

### Q2

Write a program that takes two numbers from the command line and outputs the larger number with the label `Larger: `. If the numbers are equal, output `Equal` with no number.

Example 1:

```
> 9
> 3
Larger: 9
```

Example 2:

```
> 2
>  2
Equal
```

### Q3

Write a program that takes in two strings and prints them in alphabetical order separated by a comma. Hint: Python's `<` operator can compare strings too.

Example:

```
> banana
> apple
apple,banana
```

### Q4

Write a program that takes in 3 numbers and outputs them in sorted order, separated by spaces.

Example: 

```
> 2
> 9
> 1
1 2 9
```

### Q5

Write a program that simply prints the word "beans" five times, using a while loop.

Example:

```
beans
beans
beans
beans
beans
```

### Q6

Write a program that does the same as the above, but use a `for` loop.

### Q7

Write a program that takes in two numbers and counts down from the first number by the second number until you reach 0. Do not print any numbers less than or equal to 0. 

Example 1: 

```
> 18
> 5
18
13
8
3
```

Example 2:

```
> 18
> 6
18
12
6
```

### Q8

Write a program that takes in two numbers and prints every number between them (inclusive) separated by commas.

**Note:** The program should print from smallest to largest, regardless of which was entered first. 

Example 1:

```
> 2
> 9
2,3,4,5,6,7,8,9
```

Example 2:

```
> 20
> 17
17,18,19,20
```

### Q9

For question 9, write your own question. Come up with some small program that uses a `while` or `for` loop to perform some simple task like the ones listed above. It can be very simple. The only requirements are:

- There should be a comment near the top of the file that describes what the file is intended to do
- The code should use a loop


Example file (you can't use this one!):

```python
# this program prints out all the even numbers between 20 and 40
i = 20
while i < 40:
    print(i)
    i += 2
```
