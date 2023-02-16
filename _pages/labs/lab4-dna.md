---
title: Lab 5 - DNA Sequencing
permalink: /labs/lab5/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

The purpose of this lab is to get more practice with file I/O and using GitHub while also being exposed to some of the cool things you can do with Python, without having to get bogged down into how to actually write the Python code.  

In this case, we're using the process of transcribing DNA to RNA to proteins as a tool to practice file I/O and using GitHub.

This is an **individual lab**. You turn it in by making a pull request as described at the bottom of this lab page.

# Background - Quick Bio Lesson

Our DNA is made up of sequences of four building blocks called _nucleic acids_, represented by the letters A, C, G, T. Sequences of these letters get read by our body's machinery and transcribed first into RNA, which is represented by A, C, G, and U, and then translated into one of 20 _amino acids_. These amino acids are then used as building blocks for _proteins_, which perform various tasks inside our body to keep us alive. 

The DNA to RNA step works as follows: Each letter ACGT has a complimentary letter UGCA (in that order). So, anywhere there is an A it becomes a U; anywhere there is a C it becomes a G; etc. 

The RNA to Proteins step works as follows: There is a particular sequence of 3 letters that signals the start of the protein. Then each subsequent block of 3 letters has a corresponding amino acid. Finally, there is a sequence of 3 letters that signals the end.

Here is a diagram of this process:

![Central dogma of biology. Image shows a sequence of steps from the ACGT strings to ACGU strings to proteins](https://cdn.kastatic.org/ka-perseus-images/2b597889d05bc601803a3b4d9ec5ccd5e7b8d3af.png)

Here is a chart showing which 3 RNA letters correspond to which amino acids.

![Amino acids chart](https://www.researchgate.net/publication/337736408/figure/fig1/AS:832375021895683@1575465078548/Codon-tables-with-the-amino-acids-encoded-according-to-different-properties-a-The.png)

This process means that if I give you a string of DNA, you can transcribe it into RNA, then into proteins. That is the goal of this lab. 

# Lab Assignment

Go to [this GitHub repository](https://github.com/alackles/CMSC140-DNASEQLAB) and follow the instructions in the `README`, also listed below: 

1. **Fork** the repository to your own GitHub account
2. **Clone** the repository from your GitHub
3. **Explore** the code. Read the comments. What does the code do?
4. **Change** the path to project to accurately reflect where it is stored on your computer
5. **Write** part of the code that outputs the final amino acid string into a text file called `aa.txt`
6. **Commit and Push** your local changes to your remote repository.
7. **Open** a pull request between your remote repository and my repository
8. **Write** a message in the pull request to describe what you have done. 