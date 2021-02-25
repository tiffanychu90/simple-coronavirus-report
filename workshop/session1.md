# Session 1 Outline

## Introductions 

## Workshop Arc

### Workshop Goals

1. Progressively work toward 1 work product / deliverable. 

1. Complete an actual on-the-job assignment expected of a data analyst / data scientist.

1. Understand the data pipeline behind creating a visualization.

1. Learn best practices around reproducibility with open-source software and version control.
    * Python, Jupyter Notebooks
    * Docker
    * GitHub
    * Markdown

### Sessions

__1st session__: more lecture-driven, screen-share.

**Future sessions**: use notebook to cover concepts, time to work within Jupyter Notebooks, use breakout rooms to address questions.

Practice using GitHub as version control...even for class notes!

## Why coronavirus?

* Rapidly evolving situation, need for up-to-date information

* Early issues of large-scale, daily data collection, compilation
    * From web scraping to dedicated GitHub or other APIs to make data publicly available
    * [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
    * [Covid Tracking Project](https://covidtracking.com/data)
    * [New York Times](https://github.com/nytimes/covid-19-data)

* General consensus in the scientific / public health community by late spring / summer
    * Total cases --> daily new cases
    * Positive tests --> number of tests conducted
    * **Maintenance mode**: show the public the same set of visualizations everyday to monitor developments
* One of the most visualized topics ever
* Evolving public health guidance and standards
    * Visualizations might regional standards to convey how well we're doing
* Mayor's office approach vs data team's approach of automating a pipeline
    * First visualization uses time-series data, and each subsequent day, you need to add yesterday's data and recreate the same visualization
    * Adding 1 day's of data doesn't seem too time-consuming, if you repeated it for 30 days. What about 100 days? What about 200 days? When is it too much?
    * Our automated daily reports have been emailing since 6/1/2020! Occasionally make changes when public health directives change.


## Overview of Data Science Stack

Our stack is Python-based, but RStudio is also made available, and there are working examples in the repo.

### Screen-share setup

## To Do 
1. Go through the **[Getting Started Guide](../getting_started.md)** and get set up.
1. Explore and familiarize yourself with the GitHub repo (locally)