# Getting Started

You'll need several programs / accounts set up to use this repo.

Here's the big picture for how all these programs fit together:
Goal: Clean, explore, visualize data.

We'll use **Python** (the language), but write our code in **Jupyter Notebooks** (an interactive environment to see what's happening step-by-step). We save our code in **GitHub** (a tool for collaborative work and version control). To make sure we're all on the same page with our Python packages and package versions, we use the same **Docker** image for a standardized environment. We will be using the **command line interface**, by setting up **Ubuntu** to start our Docker container and push / pull from GitHub.   

Short explanation programming languages like [Python, R, HTML, CSS, etc](https://github.com/ucla-its/ucla-its-data-camp-2019/blob/master/Pre-Course/Programming-Landscape.md). If you've used Stata, SAS, SPSS, ESRI ArcGIS, and/or other proprietary software knowledge for data wrangling and visualization, most of those skills and concepts are transferable, and you'll simply be learning new syntax. 

One plus of Python (and R) over the proprietary software is that it can clean and visualize tabular and geospatial data.  Stata is  great for tabular data, while ESRI ArcGIS is great for geospatial. Python supports the spatial joins, buffers, and map visualization, as well as calculating descriptive statistics.

The con of Python (and any other open source software) is that there are so many packages out there, they get updated and deprecated often, and one package update can break the functionality of other packages. Stata, SAS, SPSS, ESRI ArcGIS, would all bundle the supporting packages, so you never have to worry about that. It can be someone's full-time job to make sure the Python environment is stable for a team. We'll try and get around that by using Docker.

Go through step-by-step to get set up!

1. [Step 1: Install Programs](#step-1-install-programs)
1. [Step 2: Fork the Repo](#step-2-fork-the-repo)
1. [Step 3: Change into your current directory](#step-3-change-into-your-current-directory)
1. [Step 4: Clone the Repo](#step-4-clone-the-repo)
1. [Step 5: Build the Docker Container](#step-5-build-the-docker-container)
1. [Step 6: Add Credentials](#step-6-add-credentials)

<br>

## Step 1: Install Programs

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


**Optional**

To have a nicer prompt in your terminal, with different colors, show our GitHub info, etc:

* Print what's in our bashrc `cat ~/.bashrc`
* Use vim to change those settings (vim is really clunky to use, so beware!): `vim ~/.bashrc`
    * Some of the clunky and unintuitive ways to use vim (these are tips, not instructions for displaying a nicer prompt): 
        * capital `I` to enable "insert mode"
        * right click to paste
        * `ESC` to leave "insert mode"
        * `:wq` to exit after editing
        * As long as you're in "insert mode", you can type and delete as normal.
        * If you're not in "insert mode", it is more tricky to type and delete characters.
    * `I` to enable "insert mode"
    * Let's get a nicer display for our prompt. Scroll down, by clicking the "down arrow", to somewhere in the `bashrc`, maybe towards the end, and paste (right click) this in:
    ```
    # Show a nicer prompt.
    export GIT_PS1_SHOWDIRTYSTATE=1
    export PS1='\[\033[00;32m\]\u\[\033[01;34m\] \w\[\e[31m\]$(__git_ps1)\[\033[01;34m\] \$\[\033[00m\] '
    ```
    * `ESC` to leave "insert mode"
    * `:wq` to exit after editing
    * Refresh and reflect new changes: `source ~/.bashrc` 
    * To see what's in our `bashrc`, to double check the nicer prompt code is there: `cat ~/.bashrc`


### Docker

Docker images are one way to create a standardized Python environment. Unlike proprietary software, such as Stata 14, Stata 15, each version of Stata is bundled with all the commands. With open source languages like Python and R, packages are constantly getting updated / deprecated. One way to get pretty close to a standardized environment in Python is to use a Docker image. 

Download [Docker for Windows](https://docs.docker.com/docker-for-windows/release-notes/), download 3.1.0.

Download [Docker for Macs](https://docs.docker.com/docker-for-mac/release-notes/), download 3.1.0.

During the install:
* Check `Install required Windows components for WSL 2` 
* Check `Add shortcut to desktop` 
* You do **not** need to create a login with Docker to use it.

Once it's downloaded, start your Docker and we'll change some settings.

* Right click > Settings > Resources 
    * WSL Integration: 
        * Uncheck `Enable integration with my default WSL distro` 
        * Check `Enable integration with additional distros` for Ubuntu.
    * Experimental Features: turn off `Enable cloud experience`
* Restart Docker

If you don't start Docker at startup (recommended, especially if you're not actively using Docker all the time), then you have to remember to start Docker. Once you start it, you're able to restart / change settings by finding the Docker "whale" icon in the System Tray (mini icons in bottom right corner).

### GitHub

Go to [GitHub](https://github.com/) and create an account. While all the code in the repo is public, you'll be practicing how to use GitHub to collaborate and use version control for your work!

With GitHub, there is the **local** and **remote** version of the repo. 
* Local: the entire repo, its folders, files that's on your computer
* Remote: what you see when you visit the website: https://github.com/[USERNAME]/[REPO_NAME]

You will get used to make changes locally, then pushing those changes to the remote repo, so that it's reflected on the website. The way collaborators stay in sync is by pushing their changes to the remote, or by pulling their changes from the remote so that it's reflected locally.

### Text Editor

Optionally, a text editor can be installed. Most of our work will be done in Jupyter Notebooks, so a text editor isn't needed. Within our Docker setup, we'll have access a simple text editor.

Installing another text editor can make your life easier for writing or reading code, as it provides built-in formatting or highlighting. When you're writing Python scripts (.py), Markdown (.md), YAML files (.yml), you might want to have a more advanced text editor handy. 

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
    * If you get a `Git init: fatal: could not set 'core.filemode' to 'false'` error, try it with a "sudo" in front: `sudo git clone https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`
        * [Debugging error references](./install_errors.md)
* Once cloned, move from the `GitHub` folder into the `simple-coronavirus-report` folder: `cd simple-coronavirus-report`
* Add and set your remote repository (by convention, it is called `origin` or `upstream`): `git remote add origin https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`

## Step 5: Build the Docker Container

Now, we'll build the Docker container using the Docker image provided in the repo. Basically, a Docker container is a virtual machine, a virtual computer, and you'll install all your Python packages on that virtual machine. We'll do all on this virutal machine locally, which is how we can standardize the Python environment for everyone. That's how we make sure everyone has the same packages installed, the same package versions, etc.

The relevant files in the repo to have this Docker container set up are: `Dockerfile` and `docker-compose.yml`. 

You can certainly do work without Docker, but if you plan on sharing code, others might not be able to run it (due to lack of packages or different package versions). It is best to have a Docker setup, but it's also a lot of work to set it up and maintain.

In Ubuntu:
* Make sure we're in the repo. If we're not: `cd simple-coronavirus-report` 
* Once we're in this repo, we can run files within this repo, such as the files needed to build the Docker container.
* Build the Docker container (only necessary for the first time): `docker-compose.exe build`
    * Building the Docker container will take awhile (~10 min)
    * If it's hanging too long, you can press the "down arrow" and see if that helps it move on
    * To know when it's done building, you should see: 
        ```
        Successfully built CONTAINER_ID
        SUccessfully tagged simple_coronavirus_report:latest
        ```
* Start Docker container: `docker-compose.exe up`
* Navigate to browser and open Jupyter Lab notebook by typing `localhost:8888/lab/` or `http://localhost:8888/rstudio` for RStudio.
    * ...DO ALL YOUR WORK LOCALLY....
* When you're done for the day, `CTRL+C` to stop the Docker container from running, then stop Docker container: `docker-compose.exe down`
* THe next time you want to do work, start your Docker, then in Ubuntu, repeat the `docker-compose.exe up`, open Jupyter Lab, then `docker-compose.exe down`


## Step 6: Add Credentials

Optional step!

The best practice is to hide your credentials, but have them in a place where you can access them within a notebook without hard-coding it. One way to do this is with .env files. The .env file will not get checked into the GitHub repo, so when you clone/fork, you're not transferring passwords, but you will have to create one for yourself.

There is 1 case where we use a GitHub personal access token to upload a file directly to GitHub using the GitHub API. You can still create a report and upload the file through the the `git add`, `git commit`, and `git push` process without the token. But just in case...

Add a .env file (you'll have to use VSCode or another text editor to be able to see the file) with these contents: 

```
# Environment variables go here, can be read by `python-dotenv` package:
#
#   `src/script.py`
#   ----------------------------------------------------------------
#    import dotenv
#
#    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
#    dotenv_path = os.path.join(project_dir, '.env')
#    dotenv.load_dotenv(dotenv_path)
#   ----------------------------------------------------------------
#
# DO NOT ADD THIS FILE TO VERSION CONTROL!

#Personal Access Key for simple-coronavirus-report
GITHUB_TOKEN_PASSWORD=000000111111111111222222222AAAAABBBBCCC

# Any other passwords can be pasted here
```

<br>

Back to [main README](./README.md), [GitHub Workflow](./github_version_control.md), [Making a Report](./making_report.md), [Data Pipeline](./data_pipeline.md) or [Other Resources](./other_resources.md) 