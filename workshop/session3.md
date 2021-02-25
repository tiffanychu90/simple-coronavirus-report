# Session 3 Outline

## Clean Up 

Wrap up all the commits from last week into 1 pull request (PR).

* Make PR
* Merge
* Pull from `master`
* Check out new branch
* Do this week's work on new branch

## Functions!

* Repeat data cleaning or visualizing steps
    * Do you data cleaning on a subset of data first (just 1 or 2 counties)
    * Check to make sure it works as expected
    * Generalize to all US counties
* Keeps code tidy
    * To use a function across notebooks or scripts, you can create a `utils.py`, and call/invoke it.
    * Note: the `utils.py` must be in the same directory as the notebooks / scripts.
    * Ex: function called `clean_data_make_chart()` in `utils.py`. To use in a notebook: `utils.clean_data_make_chart()`.
    * In R, you similarly `source` a function, and then invoke it.


## Notebook Exercise

Run through `1-read-in-data.ipynb` and `utils.py`.
Run through `2-demo-chart.ipynb`.

References:
* **[Other Resources](../other_resources.md)** to complete data cleaning.

## To Do 
1. Make progress on `2-demo-chart.ipynb`, or create new notebook.
1. Make at least 1 more commit.
1. Turn last week's work in data cleaning into a function and move it into `utils.py`.

