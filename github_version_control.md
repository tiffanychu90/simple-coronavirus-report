# GitHub Workflow

We'll outline a very simple GitHub workflow here. 

## Collaborate and Use Version Control
One major learning objective of this workshop is to learn how to write code in a collaborative setting. Version control is super important for this. GitHub can facilitate this collaborative workflow. For this workshop, you'll learn to collaborate with yourself (a past version of you collaborating with a future version of you). You'll apply all these best practices, but we'll strip away some of the more advanced GitHub workflows that come with collaborative work, as that isn't the focus for now.

As mentioned in the [GitHub](#github) section, the way for collaborators to stay in sync with their code is by pushing and pulling their code. You can upload a lot of different files to GitHub, ranging from code stored in text files (.py, .R, .do), Jupyter Notebooks (.ipynb), HTML files (.html, .md), datasets (.csv, .xlsx, .parquet, .zip, .geojson, etc), to images and reports (.pdf, .png, .jpg, etc). GitHub has some built-in functionality to display some of those, but not all of them, but it can certainly store all of them. Large datasets shouldn't be uploaded (>25MB via browser, >100MB via command line). 

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

When all the work on the branch is done, you're ready to **merge** the branch in. On the GitHub website, you'll open a pull request, and take a look at the "summary" of all those changes, and merge! Merging it applies all those changes, the entire commit history, and tacks that onto the master branch. You'll pull from the master branch, and then checkout a new branch to go off on a new assignment, and repeat the cycle.