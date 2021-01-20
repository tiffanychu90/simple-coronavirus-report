# Getting Started

You'll need several programs / accounts set up to use this repo.

Here's the big picture for how all these programs fit together:
Goal: Clean, explore, visualize data.

We'll use **Python** (the language), but write our code in **Jupyter Notebooks** (an interactive environment to see what's happening step-by-step). We save our code in **GitHub** (a tool for collaborative work and version control). To make sure we're all on the same page with our Python packages and package versions, we use the same **Docker** image for a standardized environment. We will be using the **command line interface**, by setting up **Ubuntu** to start our Docker container and push / pull from GitHub.   

Short explanation programming languages like [Python, R, HTML, CSS, etc](https://github.com/ucla-its/ucla-its-data-camp-2019/blob/master/Pre-Course/Programming-Landscape.md). If you've used Stata, SAS, SPSS, ESRI ArcGIS, and/or other proprietary software knowledge for data wrangling and visualization, most of those skills and concepts are transferable, and you'll simply be learning new syntax. 

One plus of Python (and R) over the proprietary software is that it can clean and visualize tabular and geospatial data.  Stata is  great for tabular data, while ESRI ArcGIS is great for geospatial. Python supports the spatial joins, buffers, and map visualization, as well as calculating descriptive statistics.

The con of Python (and any other open source software) is that there are so many packages out there, they get updated and deprecated often, and one package update can break the functionality of other packages. Stata, SAS, SPSS, ESRI ArcGIS, would all bundle the supporting packages, so you never have to worry about that. It can be someone's full-time job to make sure the Python environment is stable for a team. We'll try and get around that by using Docker.

## Step 1: Install Stuff

1. [Ubuntu](#terminal): Terminal, command line interface
1. [Docker](#docker) 
1. [GitHub](#github)
1. Optional: [Text Editor](#text-editor)

### [Terminal](#terminal)

For Windows, visit the Microsoft Store, search "Ubuntu", and install it.

For Macs, you can also install Ubuntu. If not, there might be some additional steps to get Docker to work.

### [Docker](#docker)

Docker images are one way to create a standardized Python environment. Unlike proprietary software, such as Stata 14, Stata 15, each version of Stata is bundled with all the commands. With open source languages like Python and R, packages are constantly getting updated / deprecated. One way to get pretty close to a standardized environment in Python is to use a Docker image. 

Download [Docker for Windows](https://docs.docker.com/docker-for-windows/release-notes/), download 2.5.0.1.

Download [Docker for Macs](https://docs.docker.com/docker-for-mac/release-notes/), download 2.5.0.1.

### [GitHub](#github)

Go to GitHub and create an account. While all the code in the repo is public, you'll be practicing how to use GitHub to collaborate and use version control for your work!

With GitHub, there is the **local** and **remote** version of the repo. 
* Local: the entire repo, its folders, files that's on your computer
* Remote: what you see when you visit the website: https://github.com/[USERNAME]/[REPO_NAME]

You will get used to make changes locally, then pushing those changes to the remote repo, so that it's reflected on the website. The way collaborators stay in sync is by pushing their changes to the remote, or by pulling their changes from the remote so that it's reflected locally.

### [Text Editor](#text-editor)

Optionally, a text editor can be installed. Most of our work will be done in Jupyter Notebooks, so a text editor isn't needed. Within our Docker setup, we'll have access a simple text editor.

Installing another text editor can make your life for writing or reading code, as it provides built-in formatting or highlighting. When you're writing Python scripts (.py), Markdown (.md), YAML files (.yml), having a more advanced text editor may make your life easier. 

Some options:
* [Visual Studio Code](https://code.visualstudio.com/) 
* [Atom](https://atom.io/)
* [Sublime Text](https://www.sublimetext.com/). 

## Step 2: Fork the Repo

One group member  will [fork the repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo). This allows everyone in your group to make changes to the code and practice collaborating with one another.

Once the repo is forked, everyone needs to clone the repo to their local computer. This moves it over from what you see remotely, or on the GitHub website, to a folder sitting on your local computer. You'll be able to make changes to the notebook.

## Step 3: Change into your current directory

We're going to `clone` the GitHub repo, which means we're going to download a copy of the entire directory, all its sub-folders, all the files, etc onto our computer. But first, we need to know where we are.

In Ubuntu:
* Type `ls`
* Find the file path of where you want to store your folder, maybe Documents, Desktop, etc. Pick one that is in the C:// drive on your local computer and not cloud storage like Google Drive (G://)
* Change into that directory: `cd /mnt/c/Users/Documents/GitHub/`. For me, I'm in my `Documents` folder, and within that, a sub-folder called `GitHub`.

## Step 4: Clone the Repo

In Ubuntu: 
* Clone the repo: `git clone https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`
* Add and set your remote repository (call `origin`): `git remote add origin https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`

## Collaborate and Use Version Control
One major learning objective of this workshop is to learn how to write code in a collaborative setting. Version control is super important for this. GitHub can facilitate this collaborative workflow.

As mentioned in the [GitHub](#github) section, the way for collaborators to stay in sync with their code is by pushing and pulling their code. 

In GitHub, there's a `master` branch, the latest version of code that is ready to go for everyone. When you're working on an individual task, make sure you've pulled all the changes from the `master` branch, and then make a new branch to do your work. When you've finished the task, your new branch is ready to be **merged** into the master branch.

### Make new branch
In Ubuntu:
* Checkout the master branch: `git checkout master`
* Pull all the latest changes in the master branch (make sure your local matches the remote): `git pull origin master`
* Make a new branch to do your work: `git checkout -b my-new-branch`
* ....DO ALL YOUR WORK LOCALLY....

### Push changes to the remote
When you've done some work locally, you want to save a version in the remote repo. Think of this as "saving" in your Word Doc, Google Doc, etc. With GitHub, you have explicitly "save" by **committing** the changes. Otherwise, your changes are saved locally only. Think of this as creating checkpoints in your code, and you can always revert back any versioned changes in the remote repo.

In Ubuntu:
* Push your local changes to the remote: `git add notebooks/1-read-in-data.ipynb`. For multiple files, do `git add notebooks/1-read-in-data.ipynb utils.py`
* Commit the change by including a short commit message: `git commit -m "Exploratory analysis"`
* Push the changes from local to the remote: `git push origin my-new-branch`
* Go to the site: `https://github.com/YOUR-USERNAME/my-new-branch` and you should see your changes reflected there. 