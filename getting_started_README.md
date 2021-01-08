# Getting Started

You'll need several programs / accounts set up to use this repo.

## Step 1: Install Stuff

1. Terminal, command line interface
1. [Docker](#docker) 
1. [GitHub](#github)

### Terminal
For Windows, visit the Microsoft Store, search "Ubuntu", and install it.

For Macs, you can also install Ubuntu. If not, there might be some additional steps to get Docker to work.

### [Docker](#docker)

Docker images are one way to create a standardized Python environment. Unlike proprietary software, such as Stata 14, Stata 15, each version of Stata is bundled with all the commands. With open source languages like Python and R, packages are constantly getting updated / deprecated. One way to get pretty close to a standardized environment in Python is to use a Docker image. 

Download [Docker for Windows](https://docs.docker.com/docker-for-windows/release-notes/), download 2.5.0.1.
Download [Docker for Macs](https://docs.docker.com/docker-for-mac/release-notes/), download 2.5.0.1.

### [GitHub](#github)

Go to GitHub and create an account. While all the code in the repo is public, you'll be practicing how to use GitHub to collaborate and use version control for your work!


## Step 2: Fork the Repo

One group member  will [fork the repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo). This allows everyone in your group to make changes to the code and practice collaborating with one another.

Once the repo is forked, everyone needs to clone the repo to their local computer. This moves it over from what you see remotely, or on the GitHub website, to a folder sitting on your local computer. You'll be able to make changes to the notebook.

## Step 3: Change into your current directory

We're going to `clone` the GitHub repo, which means we're going to download a copy of the entire directory, all its sub-folders, all the files, etc onto our computer. But first, we need to know where we are.

In Ubuntu:
* Type `ls`
* Find the file path of where you want to store your folder, maybe Documents, Desktop, etc.
* Change into that directory: `cd /mnt/c/Users/Documents/GitHub/`. For me, I'm in my `Documents` folder, and within that, a sub-folder called `GitHub`.

## Step 4: Clone the Repo

To clone: 
* In Ubuntu, type `git clone https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`

## Collaborate and Use Version Control
Part of