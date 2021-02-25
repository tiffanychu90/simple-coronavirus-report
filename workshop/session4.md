# Session 4 Outline

## Clean Up 

Wrap up all the commits from last week into 1 pull request (PR).

* Make PR
* Merge
* Pull from `master`
* Check out new branch
* Do this week's work on new branch

## Making a Report

* Now that you have functions, it should be easy to make a report comparing 5 places.
* A report isn't just charts or maps, it should also contain explanation, narrative, or conclusions, maybe even some captions. Use Markdown cells in the Jupyter Notebook to do so. 

**[Making a Report docs](../making_report.md)**

## Notebook Exercise

Run through `5-full-report.ipynb`.

Demo using terminal to do `jupyter nbconvert` to convert a Jupyter Notebok into HTML or pdf.

Run through `automate.py` and `report.py`.

If time permits:

Run through `A-county-charts.Rmd` and `iterate.R` and `D-sample-report.Rmd`.


|  | Python | R |
| ---| ---- | --- |
| utility functions | `utils.py`, `chart_utils.py` | `r_utils.R`, `r_chart_utils.R` |
| full report | `5-full-report.ipynb` | `D-sample-report.Rmd` |
| automating report | `automate.py`, `report.py` | `iterate.R` |
| individual county report | N/A | `A-county-charts.Rmd` (pdf), `B-county-charts-html.Rmd` (HTML) |
| report with hyperlinks to various places | [CA](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/notebooks/ca-counties.ipynb) or [US](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/notebooks/us-counties.ipynb) | N/A |
| pdf formatting | [PDFviaHTML](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/main.py) | `preamble.tex` invoked in all Rmd |


## To Do 
1. Make progress on `5-full-report.ipynb` or create new notebook.
1. Make at least 1 more commit.
1. Merge in any open PRs, clean up your merged branches, clean up your repo.
1. Open a GitHub issue on **MY** repo, embed the URL of your report (HTML or PDF), and tag me. Your report should be on the `master` branch, because your PRs should be merged in.
    * Hint: Markdown syntax for URLs is `[DISPLAY NAME](URL_LINK)`

