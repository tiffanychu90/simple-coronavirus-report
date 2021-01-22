# Data Pipeline Overview

Coming up with a report, or some visualization, seems simple enough. Yet, it requires an entire data pipeline to support it, especially if this report is something you'd like to automate daily, weekly, or monthly.

We won't be able to cover the entirety of the data pipeline with this workshop, but we can get the "meat and potatoes" done. You'll also know which components are missing, and perhaps add those components later on when you have the resources and/or know-how.

We'll describe these steps generally, and apply it specifically to coronavirus data. Coronavirus stats is a great example for illustrating a relevant piece of information people want to know daily. Once you have a set of visualizations down, you want to update that daily so that it reflects the most up-to-date information.

Dashboards have become extremely common in the data science / visualization world as a means to communicate with the public. The most common dashboards out there (Tableau, PowerBI, ESRI) are easy to spin up, but limited when you want to do more complicated data processing or more complicated charts. Most of the time, you need to offload all your data processing elsewhere (Python, R, Stata, etc) and connect your dashboard to the cleaned data to visualize. Dashboards are great for displaying counts, but what about cases when you want some simple analysis?

1. [Connecting to Data Sources](#connecting-to-data-sources)
1. [Data Cleaning](data-cleaning)
1. [Data Wrangling and Transforming](#data-wrangling-and-transforming)
1. [Visualizing](#visualizing)
1. [Publishing the Report](#publishing-the-report)


## Connecting to Data Sources

Identify where your data is coming from, and this should be a canonical data source.

With coronavirus data, a couple of sources emerged as reputable, canonical data sources in March and April. These are Johns Hopkins University (JHU), Covid Tracking Project, and the New York Times. 

This repo uses JHU data. JHU provided county-level time-series data as ESRI layers and CSVs in their GitHub repo. CSVs can be read directly in GitHub, and this became an easy way for us to pull their CSV time-series file.

As an entity publishing data, you also want to think of the tools others are using to connect to your data. Are you providing it in a format that they can pull repeatedly with their code, or do they have to manually click and download?

## Data Cleaning

Hopefully, the data provided is clean and tidy. Even so, you might have to do some initial processing before you save your version.

With JHU's data, their CSV time-series ends yesterday. But they also had an ESRI layer that displayed today's numbers. Some steps for initial data cleaning are:
* Append these 2 so we can get as much data as possible
* Today's data doesn't come with a date, so we need to timestamp it ourselves and save it. Then, we can construct our own time-series.
* If we're appending, we want to check for duplicates and drop them. Ex: If we're running our code several times to test, we don't want to keep appending today's date over and over and have that in our dataset. 

You would use a Python script to bring in these raw data sources, a little data cleaning, and save it somewhere (AWS S3 bucket, GitHub, locally, etc). Scheduling this would require additional cloud and storage resources.

**Ex: [Import JHU US county data script](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/data/jhu_county.py)**

## Data Wrangling and Transforming

The next step is the figure out what you want to visualize, and how you need to wrangle and transform the data to get there. The US county data came with cumulative cases each day.

### Deriving New Columns

We could plot cumulative cases, but there are so many other interesting metrics to plot! Also, the CA Department of Public Health guidelines set tier thresholds based on a 7-day rolling average of *new* cases. Additionally, new metrics that help us compare counties across CA and the US is useful; population-adjusted numbers, doubling time, etc are ways to normalize cumulative cases and deaths.

We'll have to derive additional columns:
* new cases (change from the prior day)
* 7-day rolling average for cases, deaths, new cases, new deaths
* per capita 
* doubling time 
* severity

### Transforming Data

After getting new columns, there might be data *transformations* we could do (aggregations). For example, test positivity rates are often the positivity rate over the entire week, so we'd want to take Sun-Sat weeks and aggregate. If we don't have a full week's worth of data, we want to exclude that week before we visualize.

### Using General Functions

**Use functions** and comment frequently when you clean your data! It can keep your code clean and readable (as much as possible). For our US county data, we have data for all US counties, and even if we're only interested in LA County, we should always set up our data cleaning and functions to be as general as possible. You can always set your default parameters to extract LA County at the very end of your data cleaning.

**Ex: [Data wrangling for our charts](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/notebooks/utils.py)**

## Visualizing

Data wrangling and visualizing actually go hand-in-hand, and these two steps are iterative. As you come up with new ideas of what to visualize, you'll be adding more to your data wrangling step. In Python, there are different visualization packages, including `matplotlib`, `seaborn`, and `altair`. We'll cover `altair` in the workshop. In R, there's `ggplot2`, `plotly`, and many others.

Keep things generalizable, even in the visualization. Some things are going to be pre-set, such as always using the 7-day rolling average, or line colors, or chart height / width. Other things can be variable and flexible, such as start date, which county to plot, chart title, etc.

Once you make a chart for a county, it's good practice to also use charting functions. You'll build those variable and flexible components into your charting function. If the plot displays LA County trends in new cases, the title might be `Los Angeles County: New Cases`, taking the form of `[COUNTY NAME]: New Cases`. You'll want that chart title to be handled for you directly in the function. Or, you want to keep the start date flexible, maybe you're interested in plotting the last 6 months of trends, so you'll want to subset your data with `[TODAY'S DATE] - 6 months`. Anything that can be done repetitively can be written up as code, it just takes a little bit of setup.

**Ex: [Functions to make charts and add captions](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/notebooks/us_county_utils.py)**

## Publishing the Report

Now that we've set up our Jupyter Notebook to be a report, we need to publish it in a format that's familiar to others. If it's a report that's emailed daily, it should be pdf. If you're displaying like a website, you can convert the notebook to HTML and upload it to GitHub pages.

GitHub does come with some built-in capabilities to show what's in a Jupyter Notebook or render a simple website. We can take advantage of GitHub pages and display our results as an HTML page. Many people use GitHub pages to host their resume, online portfolio, blog, or personal website.

If you want a really lightweight HTML page that you can create with very little HTML knowledge, you can use a Markdown document (.md). All the docs in this workshop are done using Markdown. 

To display more complicated things like charts, we'll need to use a Jupyter Notebook. Jupyter Notebook also comes with Markdown cells; you can add your title, headers, and text in your report and weave the visualizations with narrative together.

Scheduling this would require additional cloud and storage resources.

**Ex: [Run a notebook, convert to HTML, upload to GitHub](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/report_county_trends.py)**

<br>

Back to [main README](./README.md), [Getting Started](./getting_started.md), [GitHub Workflow](./github_version_control.md), [Making a Report](./making_report.md) or [Other Resources](./other_resources.md) 
