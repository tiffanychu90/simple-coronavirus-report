"""
Create the report as HTML and upload to GitHub.
"""
import datetime
import dotenv
import os
import subprocess
#import sys

import pandas as pd
import papermill as pm 
import automate

dotenv.load_dotenv()

#sys.path.append(os.getcwd())

# Constants for loading the file to GH Pages branch
TOKEN = os.environ["GITHUB_TOKEN_PASSWORD"]
REPO = "tiffanychu90/simple-coronavirus-report"
BRANCH = "master"
COMMIT_MESSAGE = "Update report"

notebooks_to_run = {
    "4-geospatial-example.ipynb": "./4-geospatial-example.ipynb",
}

for key, file_name in notebooks_to_run.items():
    try:
        pm.execute_notebook(
            f'../notebooks/{key}',
            file_name,
            cwd='./reports'
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
            TOKEN,
            REPO,
            BRANCH,
            f"{html_file_name}",
            f"{html_file_name}",
            f"{COMMIT_MESSAGE}",
            DEFAULT_COMMITTER,
        )
        
        print("Successful upload to GitHub")
    except: 
        pass
        print("Unsuccessful upload to GitHub")
        