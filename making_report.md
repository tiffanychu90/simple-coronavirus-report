# Making a Report

Jupyter Notebooks are a great way to do your data cleaning, data wrangling, and visualization. However, you might not be able to hand over a Jupyter Notebook (.ipynb) to people, as people aren't accustomed to opening that file.

People are used to getting PDFs and people are used to looking at websites. Let's explore a couple of options with the tools we already have. To do more, of course, you might have to pick up more web programming skills and additional languages (Javascript, CSS) to support your endeavors.

* [RMarkdown](#rmarkdown)
    * [Examples](#rmarkdown-examples)
* [Jupyter Notebooks](#jupyter-notebooks)
    * [Examples](#jupyter-notebook-examples)
* [GitHub Pages](#github-pages)

## RMarkdown
One familiar option you may have heard of is RMarkdown. Using RMarkdown, you might use `knitr` to knit the code and outputs into a Word doc, HTML doc, or PDF. 

Our Docker image includes RStudio, and you are able to create an RMarkdown doc and knit that into HTML or PDF. If you know R/RStudio, you can use this option!

### RMarkdown Examples
All these examples use `knitr` function. The script to run is `notebooks/iterate.R`, and output files are created in the `report` directory.

* Charts + pdf [code](./notebooks/A-county-charts.Rmd), [output 1](https://tiffanychu90.github.io/simple-coronavirus-report/reports/Alameda.pdf), [output 2](https://tiffanychu90.github.io/simple-coronavirus-report/reports/Los%20Angeles.pdf)
* Charts + html [code](./notebooks/B-county-charts-html.Rmd), [output 1](https://tiffanychu90.github.io/simple-coronavirus-report/reports/Alameda.html), [output 2](https://tiffanychu90.github.io/simple-coronavirus-report/reports/Los%20Angeles.html)
* Charts with loop + html [code](./notebooks/C-ca-report.Rmd), [output](https://tiffanychu90.github.io/simple-coronavirus-report/reports/county-report.html)
* Sample pdf report [code](./notebooks/D-sample-report.Rmd), [output](https://tiffanychu90.github.io/simple-coronavirus-report/reports/sample-report.pdf)


## Jupyter Notebooks
There is a similar functionality for Jupyter notebooks. Normally, to get PDFs, it requires LaTex, and other packages to support, which can get very complicated, very easily. Our Docker image has all of that installed, so converting to a PDF is fairly easy for us!

Use the terminal within the Docker
* Launcher > Terminal 
* Convert the notebook into HTML: `jupyter nbconvert --to html --no-input --no-prompt my-notebook.ipynb`
    * `no-input`: do not display input cells (code you wrote), just the outputs
    * `no-prompt`: do not display input and output prompts
    * [nbconvert docs on exporting](https://nbconvert.readthedocs.io/en/latest/config_options.html#exporter-options)
* Convert the notebook into PDF: `jupyter nbconvert --to pdf --no-input --no-prompt my-notebook.ipynb`

### Jupyter Notebook Examples

Similar to the `iterate.R`, there is a `report.py` that is a script that can be run in the terminal.

There `report.py` uses `papermill` to execute a notebook, convert it to HTML, then relies on `automate.py` for a function to upload to GitHub pages. You may need credentials to upload to GitHub pages automatically; uploading by checking in the HTML or pdf will not require additional credentials (refer back to [Getting Started - Credentials](./getting_started.md#step-6-add-credentials)). 


Within the terminal inside Docker (Launcher > Terminal):
* Change into the notebook directory: `cd notebooks`
* Execute the Python script: `python report.py`
    * Within `report.py`, the line `TOKEN = os.environ["GITHUB_TOKEN_PASSWORD"]` is where it accesses the token without displaying it for everyone to see.

Examples: 

* Full report [code](./notebooks/5-full-report.ipynb), [output](https://tiffanychu90.github.io/simple-coronavirus-report/reports/full-report.html)
* CA counties report [code](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/notebooks/ca-counties.ipynb) and [output](https://cityoflosangeles.github.io/covid19-indicators/ca-county-trends.html)
* US counties report [code](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/notebooks/us-counties.ipynb) and [output](https://cityoflosangeles.github.io/covid19-indicators/us-county-trends.html)


## GitHub Pages

GitHub can display HTML pages and render it like a simple website. For those who don't want to venture into web programming, this is one way to get more functionality from the tools already at your disposal. People have used this to make their online portfolios or resumes.

You can set your `master` branch, or any other branch, as the one you tell GitHub to render as a webpage. Let's stick with the `master` branch for now.
* [GitHub pages docs](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
*  Convert the notebook to HTML: `jupyter nbconvert --to html --no-input --no-prompt my-notebook.ipynb`
    * Make sure you set up your file path correctly! For organization, our notebooks are in the `notebooks` folder, so your file path might be `notebooks/3-make-report.ipynb`. 
* A successful conversion will result in a file called `my-notebook.html` to be created.
* Add this file in our commit: `git add my-notebook.html`
* Add commit message: `git commit -m "Add report"`
* Push changes to remote: `git push origin my-branch-name`
* Make a pull request and merge in `my-branch-name` to the `master` branch.
* View your HTML page as a "website": navigate to `https://YOUR-USERNAME.github.io/simple-coronavirus-report/my-notebook.html`

You might need a GitHub personal access token for some of the functionalities, such as uploading files within a script rather than adding/committing yourself.

Getting a GitHub personal access token:
* On GitHub website: Settings > Developer Settings (left tab) > Personal Access Tokens > Generate a New Token
    * Check off all functionalities except `delete_repo` and `admin:enterprise`.
    * Copy and save that token somewhere! It's long and a bunch of scrambled letters/numbers.

<br>

Back to [main README](./README.md), [Getting Started](./getting_started.md), [GitHub Workflow](./github_version_control.md), [Data Pipeline](./data_pipeline.md) or [Other Resources](./other_resources.md) 