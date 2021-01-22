# Getting Started

You'll need several programs / accounts set up to use this repo.

Here's the big picture for how all these programs fit together:
Goal: Clean, explore, visualize data.

We'll use **Python** (the language), but write our code in **Jupyter Notebooks** (an interactive environment to see what's happening step-by-step). We save our code in **GitHub** (a tool for collaborative work and version control). To make sure we're all on the same page with our Python packages and package versions, we use the same **Docker** image for a standardized environment. We will be using the **command line interface**, by setting up **Ubuntu** to start our Docker container and push / pull from GitHub.   

Short explanation programming languages like [Python, R, HTML, CSS, etc](https://github.com/ucla-its/ucla-its-data-camp-2019/blob/master/Pre-Course/Programming-Landscape.md). If you've used Stata, SAS, SPSS, ESRI ArcGIS, and/or other proprietary software knowledge for data wrangling and visualization, most of those skills and concepts are transferable, and you'll simply be learning new syntax. 

One plus of Python (and R) over the proprietary software is that it can clean and visualize tabular and geospatial data.  Stata is  great for tabular data, while ESRI ArcGIS is great for geospatial. Python supports the spatial joins, buffers, and map visualization, as well as calculating descriptive statistics.

The con of Python (and any other open source software) is that there are so many packages out there, they get updated and deprecated often, and one package update can break the functionality of other packages. Stata, SAS, SPSS, ESRI ArcGIS, would all bundle the supporting packages, so you never have to worry about that. It can be someone's full-time job to make sure the Python environment is stable for a team. We'll try and get around that by using Docker.

## Step 1a: Install Programs

1. [Ubuntu](#terminal): Terminal, command line interface
1. [Docker](#docker) 
1. [GitHub](#github)
1. Optional: [Text Editor](#text-editor)

### Terminal

For Windows, visit the Microsoft Store, search "Ubuntu", and install it.

For Macs, you can also install Ubuntu. If not, there might be some additional steps to get Docker to work.

Once Ubuntu is installed:
* Set a Unix username and password. When you type the password, it won't show up (but that's for security).
* Type `sudo apt update`

### Docker

Docker images are one way to create a standardized Python environment. Unlike proprietary software, such as Stata 14, Stata 15, each version of Stata is bundled with all the commands. With open source languages like Python and R, packages are constantly getting updated / deprecated. One way to get pretty close to a standardized environment in Python is to use a Docker image. 

Download [Docker for Windows](https://docs.docker.com/docker-for-windows/release-notes/), download 3.1.0.

Download [Docker for Macs](https://docs.docker.com/docker-for-mac/release-notes/), download 3.1.0.

During the install, make sure both `Install required Windows components for WSL 2` and `Add shortcut to desktop` are checked.

### GitHub

Go to GitHub and create an account. While all the code in the repo is public, you'll be practicing how to use GitHub to collaborate and use version control for your work!

With GitHub, there is the **local** and **remote** version of the repo. 
* Local: the entire repo, its folders, files that's on your computer
* Remote: what you see when you visit the website: https://github.com/[USERNAME]/[REPO_NAME]

You will get used to make changes locally, then pushing those changes to the remote repo, so that it's reflected on the website. The way collaborators stay in sync is by pushing their changes to the remote, or by pulling their changes from the remote so that it's reflected locally.

### Text Editor

Optionally, a text editor can be installed. Most of our work will be done in Jupyter Notebooks, so a text editor isn't needed. Within our Docker setup, we'll have access a simple text editor.

Installing another text editor can make your life for writing or reading code, as it provides built-in formatting or highlighting. When you're writing Python scripts (.py), Markdown (.md), YAML files (.yml), having a more advanced text editor may make your life easier. 

Some options:
* [Visual Studio Code](https://code.visualstudio.com/) 
* [Atom](https://atom.io/)
* [Sublime Text](https://www.sublimetext.com/)


## Step 2: Fork the Repo

Change into the directory where you want to store your GitHub repos (each individual repo will be its own folder). The `simple-coronavirus-report` repo will be one folder. But, if you ever do more projects, you'll set up a new GitHub repo for it, and you'll have many folders, reflecting each GitHub repo you've cloned, on your local computer. 

You will [fork the repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo). Forking the repo makes a personal copy of the repo. You can do this in the browser on the GitHub webiste.

Once the repo is forked, you need to clone the repo. This moves it over from what you see remotely, or on the GitHub website, to a folder sitting on your local computer. You'll be able to make changes to the notebook. We'll cover that in Steps 3-4 below.

## Step 3: Change into your current directory

We're going to `clone` the GitHub repo, which means we're going to download a copy of the entire directory, all its sub-folders, all the files, etc onto our computer. But first, we need to know where we are.

In Ubuntu:
* Type `cd /mnt/c/`
* Type `ls` to see find out what the next directory / folder you can change into. 
    * Find the file path of where you want to store your folder, maybe Documents, Desktop, etc. Pick one that is in the C:// drive on your local computer and not cloud storage like Google Drive (G://)
    * If at any point you don't know what's the next folder you can get into, type `ls` and see the options.
* Change into that directory: `cd /mnt/c/Users/Documents/GitHub/`. For me, I'm in my `Documents` folder, and within that, a sub-folder called `GitHub`.
* We'll need to [set our GitHub credentials](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
) too (one time only):
* `git config --global user.name MY_USERNAME`
* `git config --global user.email MY_EMAIL`
* Check that it's all set: `git config --list --show-origin`

## Step 4: Clone the Repo

Since you've forked the repo, you won't be using this repo, which is linked to my username. You should see a repo under `Your repositories` when you go to your GitHub page, which is `https://github.com/YOUR-USERNAME`.

In Ubuntu: 
* Clone the repo: `git clone https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`. 
    * In the GitHub repo, you'll see a green button `Code`
    * Click on the arrow > HTTPS > URL for GitHub repo
* Add and set your remote repository (call `origin`): `git remote add origin https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`

## Step 5: Build the Docker Container

Now, we'll build the Docker container using the Docker image provided in the repo. Basically, a Docker container is a virtual machine, a virtual computer, and you'll install all your Python packages on that virtual machine. We'll do all on this virutal machine locally, which is how we can standardize the Python environment for everyone. That's how we make sure everyone has the same packages installed, the same package versions, etc.

The relevant files in the repo to have this Docker container set up are: `Dockerfile` and `docker-compose.yml`. 

You can certainly do work without Docker, but if you plan on sharing code, others might not be able to run it (due to lack of packages or different package versions). It is best to have a Docker setup, but it's also a lot of work to set it up and maintain.

In Ubuntu:
* Change into the repo's directory (so far, we're in the GitHub folder): `cd simple-coronavirus-report` 
* Once we're in this repo, we can run files within this repo, such as the files needed to build the Docker container.
* Build the Docker container (only necessary for the first time): `docker-compose.exe build`
* Start Docker container: `docker-compose.exe up`
* Navigate to browser and open Jupyter Lab notebook by typing `localhost:8888/lab/` or `http://localhost:8888/rstudio` for RStudio.
    * ...DO ALL YOUR WORK LOCALLY....
* When you're done for the day, `CTRL+C` to stop the Docker container from running, then stop Docker container: `docker-compose.exe down`
* THe next time you want to do work, repeat the `docker-compose.exe up`, open Jupyter Lab, then `docker-compose.exe down`

<br>

Back to [main README](./README.md), [GitHub Workflow](/.github_version_control.md), [Making a Report](./making_report.md), [Data Pipeline](./data_pipeline.md) or [Other Resources](/.other_resources.md) 