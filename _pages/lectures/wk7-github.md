---
title: Week 7 Day 2 - Git and GitHub
permalink: /lectures/w7-d2
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

_This is adapted from a lab created by Dr. Joshua Nahum for CSE 232 at Michigan State University. Thanks, Josh!_

You will need a partner. Choose someone at your table; you'll work together for this lab whenever it mentions "partner". 

## Introduction to Version Control with git and GitHub
One of the most important tools every software developer uses on a daily basis is version control.
Version control is software that can track and share changes to a code base (repository) with others.
"git" is the most popular of the version control systems and GitHub is the most popular online hosting site for git repositories.  


## Initial Setup
Make a free account on <a href="https://github.com/">GitHub.com</a>. 
Then complete the introductory tutorial named  <a href="https://guides.github.com/activities/hello-world/">"Read the Guide"</a>.
In this tutorial, you will make a public repository. You can give it a fun name if you like.

## Collaboration

* Find your partner's newly created repository on GitHub.
* Click the "Fork" button in the top-right of the repository page to make your own copy of their repository.
* Edit and commit changes to your copy of their repository. (Perhaps leave a nice compliment.) 
* Click on the "New Pull Request" button and initiate a pull request for the changes you just made.
* Accept the pull request from your partner and confirm the changes made.


## git
GitHub is a useful website for sharing git repositories with the wider world, but most or your work with version control will be on your local computer.
For this part of the lab, you need to create a new repository.
Then click on the green "Code" button and select the "HTTPS" option. Copy the HTTPS URL to the clipboard (to be used later).
This next part of the lab will be done in the terminal in VSCode; make sure VSCode is open to your folder for this class.

1. `cd` to the directory where you want a local copy of the repository to be placed.
2. Run `git clone https...` where the link is the url you copied from your GitHub repository.
3. You should be prompted for your GitHub username and a personal access token (_not_ your GitHub password). [Follow these instructions to obtain a personal access token with "repo" permissions.](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

Next we need to give git some information about yourself.

1. Run `git config --global push.default simple`
2. Run `git config --global user.name "Your Name Here"` where Your Name should be replaced with your actual name.
3. Run `git config --global user.email "blah@lawrence.edu"` where the email should be replaced with your email.

Next we will make changes to the repository. Note: most git commands require your current working directory to be inside the the repository to work.

1. Right click on the left-sidebar and refresh it to see the repository you cloned (it should be in a folder with the name of the respository).
2. `cd` into the newly created repository folder.
3. Edit the README.md file to have your name in it (or create this file if it doesn't exist). Save it.
4. Run `git status` to have git inform you of any changes to the repo it detects. It should show you that the README file has changed.
5. Run `git add README.md` to instruct git that it should track that change.
6. Run `git commit -m "Changed the README"` to have git save the changes to the history. You can replace the commit message with anything you like.
7. Run `git push` to have git share the commits (history) with the repo it was cloned from (the private repo on GitHub.)
8. If you refresh the repo page on GitHub, you should now see the changes you made to the README file.
8. Run `git fetch` to have git sync (download) any commits that have been made on the remote (Github) repository.

If you'd like a visual representation of what is happening here, here is a diagram of what these commands do and where they move work to be saved.

![git lifecycle](/CMSC-150-WT-23/assets/img/git-lifecycle.png)


## Adding Code to the Repo
This next part of the lab will involve you editing code in your repository.

1. Find some code you wrote for a previous lab and add that to your repository (copy the `.py` file into the repository folder).
2. Run `git status`to confirm that git notices the presence of the project.cpp file.
3. Run `git add example.py` (be sure to **use the actual name for the file**) and then `git commit -m "example added"` to add and commit your example file.

## Git Problems?
`git` is a complicated program with many working parts. 
Without teaching you quite a bit more about how it works, it can be difficult to know how to fix certain problems.
But if your local repo is giving you trouble, one easy fix is to clone a new copy of the repo from GitHub and work with that one (make sure to copy and commit any changed files from the old repo before deleting it).