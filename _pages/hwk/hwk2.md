---
title: Homework 2
permalink: /hwk/hwk2/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# Homework 2

The purpose of this homework is to start using lists in conjunction with the other skills you have built so far in this class.

Note that questions 1-4 are programming assignments with expected input and output that the autograder will give you feedback for. Question 5 is a programming assignment that is fully manually graded. Question 6 is a written response. 

For **Proficiency** credit:

- Your code should pass all the test cases on Gradescope
- You should turn in a complete answer for question 6.

For **Mastery** credit:

Everything for proficiency, plus

- Your code should be well-organized with good and informative variable names
- Your code should have consistent spacing
- Your answer for question 6 should show some thoughtful reflection

## Submission Instructions

To make your life, and my life, easier, there are a few submission instructions you should follow to submit your homework to gradescope. 

1. **Each problem has its own assignment on gradescope**. Be sure to submit question 1 to HWK1: Q1, and question 2 to HWK2: Q2, and so on. 
2. **Every submission should be named with the question number and the letter q.** For example, for question 3, the file should be called **`q3.py`**. (This is not necessary for question 6)
3. **Follow the requested print statements exactly.** The autograder is not very intelligent; it just gives input and asks for expected output. I will be reading and giving feedback on your code as a human, but to give you the opportunity to see whether your code is working, the autograder gives feedback too. 

Some general reminders:
- Make sure to **save your code** before running it, and before submitting it. 
- If you are having problems, start small and build. Is there any piece of the problem you think you could do, even if it is just "read a number"? Is there a second piece you can do, like "read a number and add to it"? 

# Questions

## Q1

Write a program that takes in 5 numbers and outputs them in sorted order, separated by spaces. 

**Hint:** Store the numbers in a list, and use a sorting function. 

Example: 

```
> 2
> 9
> 1
> 4
> 8
1 2 4 8 9
```

## Q2 

Write a program that takes in two numbers and prints every number between them (inclusive) separated by commas. Use `join()` somewhere in your program.

**Note:** The program should print from smallest to largest, regardless of which was entered first. 

Example 1:

```
> 2
> 9
2,3,4,5,6,7,8,9
```

## Q3

Write a program that takes in a number `n` and generates a list of length `n` where each element of the list contains as many asterisks as its index. Then, print the list.

Example

```python
> 7
["", "*", "**", "***", "****", "*****", "******" ]
```

## Q4

Write a program that takes the following list and prints the elements of the list separated by spaces, except for the last element. Do this repeatedly nothing would print, then it should print, "All done!"

Your input list (you can just save this into a variable):

`[3, 4, 6, 9, 2, 0, 4, 2, 1, 1, 1, 1, 1, 1, 1, 38, 49, 29, 0]`


Example on a smaller list(note there is no input)

Smaller list: `[2, 3, 4]`

```
2 3 4
2 3
2
All done!
```

## Q5

_Note: this question is not autograded._

Write a dictionary to store your own course schedule for this term. The keys should be the name of each course. The values should themselves be dictionaries with the following information as key-value pairs:

- Course name
- Professor(s)
- Units
- Meeting times as a list (e.g. for this class `["M 1:50 - 3:00", "W 1:50 - 3:00", "R 8:30 - 10:15"]`)

Then, print your schedule in whatever format you like by accessing elements of the dictionary.

(This is intentionally open-ended. I am interested in seeing what you come up with!)

## Q6

Explain how a list differs from a dictionary in Python as if I have never heard of lists or dictionaries, but I am familiar with all the other aspects of the Python language that you have learned so far. In particular, touch on when you might want to use one over the other. This response should be about 4-6 sentences.