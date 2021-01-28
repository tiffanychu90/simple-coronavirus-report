"""
Create the report as HTML and upload to GitHub.
"""
import datetime
import dotenv
import os
import subprocess
import sys

import pandas as pd
import papermill as pm 
import automate

dotenv.load_dotenv()

"""
To do this upload to GitHub, go to Profile > Settings > Developer Settings
Create a personal access token
Copy and paste it into a .env file. 
.env files should not be checked into version control!

In the .env, put an entry with this format:
GITHUB_TOKEN_PASSWORD=abcd000000000000000abcd

Then, we'll access it later in this script.
"""


# Constants for loading the file to GH Pages branch
TOKEN = os.environ["GITHUB_TOKEN_PASSWORD"]
REPO = "tiffanychu90/simple-coronavirus-report"
BRANCH = "master"
COMMIT_MESSAGE = "Update report"

#DEFAULT_COMMITTER = automate.DEFAULT_COMMITTER
DEFAULT_COMMITTER = {
    "name": "Service User",
    "email": "tiffany.chu@lacity.org",
}

notebooks_to_run = {
    #"4-geospatial-example.ipynb": "./geospatial-example.ipynb",
    "5-full-report.ipynb": "./full-report.ipynb",
}

for key, file_name in notebooks_to_run.items():
    # Use papermill to execute notebook
    # Rename notebook to the name we want displayed as HTML
    pm.execute_notebook(
        f'../notebooks/{key}',
        file_name,
    )
    
    print("Ran notebook")
    # shell out, run NB Convert 
    output_format = 'html'

    subprocess.run([
        "jupyter",
        "nbconvert",
        "--to",
        output_format,
        "--no-input",
        "--no-prompt",
        file_name,
    ]) 

    print("Converted to HTML")
    
    # Now find the HTML file and upload
    name = file_name.replace(".ipynb", "").replace("./", "")
    html_file_name = f"{name}.html" 
    print(f"name: {name}")
    print(f"html name: {html_file_name}")

    automate.upload_file_to_github(
        token=TOKEN,
        repo=REPO,
        branch=BRANCH,
        # GitHub path
        path=f"reports/{html_file_name}",
        # local path
        local_file_path = f"{html_file_name}",
        commit_message=f"{COMMIT_MESSAGE}",
        committer=DEFAULT_COMMITTER,
    )
    
    print("Successful upload to GitHub")
    
    # Cleanup
    os.remove(f"../notebooks/{file_name}")
    os.remove(f"../notebooks/{html_file_name}")