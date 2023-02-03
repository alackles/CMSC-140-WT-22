---
title: Homework 3
permalink: /hwk/hwk3/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

For homework 3, you will be turning five of your previous homework questions into functions, as well as a written question.

For **Proficiency** credit:

- Your code should pass all the test cases on Gradescope. 
- You should have something written for the written response that addresses the question.

For **Mastery** credit:

Everything for proficiency, plus

- Your code should be well-organized with good and informative variable and function names
- Your code should have consistent spacing

Your written response should clearly and accurately explain the difference between print and return.

## Submission Instructions

To make your life, and my life, easier, there are a few submission instructions you should follow to submit your homework to gradescope. 

1. **Each problem has its own assignment on gradescope**. Be sure to submit question 1 to HWK1: Q1, and question 2 to HWK2: Q2, and so on. 
2. **Every submission should be named with the question number and the letter q.** For example, for question 3, the file should be called **`q3.py`**.
3. **Follow the requested print statements exactly.** The autograder is not very intelligent; it just gives input and asks for expected output. I will be reading and giving feedback on your code as a human, but to give you the opportunity to see whether your code is working, the autograder gives feedback too. 

Some general reminders:
- Make sure to **save your code** before running it, and before submitting it. 
- If you are having problems, start small and build. Is there any piece of the problem you think you could do, even if it is just "read a number"? Is there a second piece you can do, like "read a number and add to it"? 

Note also that the arrows in the example below are to mark input. You do not need to print the arrow ">" as part of your answer.

## Questions

### Q1

Write a program that takes a number from the command line. Pass that number to a function which returns the string `"even"` if the number is even, and `"odd"` if the number is odd. Call the function and print the result.

Example:

```
> 9
odd
```

### Q2

Write a program that takes in two strings. Pass those strings as two separate arguments to a function which returns them as a list which is sorted alphabetically. Hint: Python's `<` operator can compare strings too.

Example:

```
> banana
> apple
apple,banana
```

## Q3

Write a program that takes in a number `n` and passes it to a function which generates a list of length `n` where each element of the list contains as many asterisks as its index. Return the list from the function. Then, print the list.

Example

```python
> 7
["", "*", "**", "***", "****", "*****", "******" ]
```

## Q4

**Hint:** See the [tips for printing lists](https://alackles.github.io/CMSC-140-WT-23/lectures/w3-d1#tips-for-printing-lists).

Write a program that takes in two numbers and passes them as arguments to a function. The function should return every number between them (inclusive) as a list. Then, you should print this list separated by commas. Use `join()` somewhere in your program.

**Note:** The program should print from smallest to largest, regardless of which was entered first. 

Example 1:

```
> 2
> 9
2,3,4,5,6,7,8,9
```

# Q5

Explain the difference between printing and returning from a function in 2-3 sentences.