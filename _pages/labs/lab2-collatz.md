---
title: Lab 2 - The Collatz Conjecture
permalink: /labs/lab2/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

The purpose of this lab is to get practice with user input, if statements, and loops -- basically, to put together everything you have learned so far. 

The other purpose is to get practice building up complex programs from simple steps. If I just told you, "write a program that performs the Collatz conjecture operations", that would probably feeling overwhelming. We are going to do just that, but piece by piece so that you get a sense of how to approach these kinds of general problems in the future and on your homework. 

**This is a group lab with an individual grade.** That means in class you will work together, but everyone needs to turn in a lab and you will all be evaluated and given the opportunity to revise on an individual basis.

For **Proficiency** credit, your code should pass all the test cases on Gradescope.

For **Mastery** credit, your code should be well-organized with good and informative variable names, as well as consistent spacing. 

# The Collatz Conjecture

The Collatz Conjecture is a famous unproven conjecture in mathematics.

## Problem Statement

Consider the following operations on any positive integer:

- If the number is even, divide it by two
- If the number is odd, multiply it by three and add one

Repeat these steps by taking the output as the new input

The conjecture states that no matter what integer you choose as your starting value, you will end up at 1. 

### Okay. So What?

It currently has not been proven whether this is true or false. 

It seems like an extremely easy problem to get a handle on, and yet expert mathematicians are unable to determine whether it is true for every number or whether there are some exceptions. 

For more, you can check out this nice pop-sci write-up in [Quanta Magazine](https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/). But we aren't really interested in solving it; we just want to implement it. 

# Lab Instructions

This lab will ask you to slowly build up a program that will print out the _collatz chain_ and its length for any number that a user gives it. Your job with your group mates is to write this program and ensure that it runs properly.

1. Create a file called `collatz.py` in which to do your lab. 
2. Make sure that you can take an input from the user, save it as a number, and then print it back out. (How can you make sure that it is being saved as a number, and not as a string?)

Example output:

```
Enter a number:  5
5
```

3. Write a block of code that will take the number input in step 2 and perform the collatz operations just _one_ time. That is, if the number is even, divide it by two. If the number is odd, multiply it by three. Print out both the result of this operation, and the original number. 

Example output: 

```
Enter a number:  5
5
16
```

4. Write some code to do this operation a set number of times. You can choose the number of times; just see that you can do it more than once. Remember that the _output_ of the previous operation should be the _input_ for the next operation. For example, if you choose to do it 3 times:

```
Enter a number: 5
5
16
8
4
```


5. Now, write some code to do this operation _until the number you get out is 1_. 

Example output:

```
Enter a number: 5
5
16
8
4
2
1
```

6. Finally, print out how _many_ times you did this operation as the very last thing that is printed. Add some text that says `"Ops Performed: "` as well. **Spacing is important.**

Example output:

```
Enter a number: 5
5
16
8
4
2
1
Ops Performed: 5
```

7. Submit to the autograder, and fix any problems. 

In programming, sometimes your program will display behavior that you did not intend because you didn't consider what would happen if it encountered some particular input or type of input. These are called _edge cases_. 

Two _edge cases_ you might run into at this point in the lab are:

1. What if you give your program the number 1?
2. What if you give your program a negative number?

In both these cases, the program should simply print the number and perform no operations (the collatz conjecture only works for positive integers). The autograder's tests 2 and 3 check these possibilities.

You may need to modify your code to make sure that it has the behavior you intend. 

**This is the end of the lab. Submit your `.py` file to Gradescope for credit.**