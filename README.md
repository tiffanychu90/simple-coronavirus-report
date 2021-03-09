simple-coronavirus-report
==============================

Demo Python / Jupyter Notebooks for making simple report.


Project Organization
------------

    ├── LICENSE
    ├── README.md                <- The top-level README for developers using this project.
    ├── Dockerfile               <- Docker image for this project.
    ├── data                     <- Scripts to create the data and CSVs.
    ├── catalog                  <- Catalog listing data sources used.
    ├── notebooks                <- Jupyter notebooks.
    ├── conda-requirements.txt   <- The requirements file for conda installs.
    ├── requirements.txt         <- The requirements file for reproducing the analysis environment,
    │                               e.g generated with `pip freeze > requirements.txt`



--------

Create a simpler version of what was done in the [City of LA covid19-indicators repo](https://github.com/CityOfLosAngeles/covid19-indicators). 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tiffanychu90/simple-coronavirus-report/binder)

All the docs to guide you for our workshop:
* [Getting Started](./getting_started.md)
* [GitHub Workflow](./github_version_control.md)
* [Making a Report](./making_report.md)
* [Data Pipeline](./data_pipeline.md)
* [Other Resources](./other_resources.md)
* Workshop Session Outlines: [1](./workshop/session1.md), [2](./workshop/session2.md), [3](./workshop/session3.md), [4](./workshop/session4.md)

Sample reports: 
* **CA COUNTIES REPORT:** [https://tinyurl.com/cacovidtrends](https://cityoflosangeles.github.io/covid19-indicators/ca-county-trends.html)

* **MAJOR US COUNTIES REPORT:** [https://tinyurl.com/uscountycovidtrends](https://cityoflosangeles.github.io/covid19-indicators/us-county-trends.html)


## Table of Contents

1. [Data](#data)
1. [Starting with Docker](#starting-with-docker)
1. [Helpful Hints for Jupyter Notebooks](#helpful-hints)

## Data

* US county-level time-series [parquet](https://github.com/CityOfLosAngeles/covid19-indicators/blob/master/data/us-county-time-series.parquet)
    * A local version is checked into `data`
* Other relevant datasets listed in `catalog.yml`


## Starting with Docker
1. Build Docker container: `docker-compose.exe build` (only necessary for 1st time)
1. Start Docker container `docker-compose.exe up`
    * The error `docker.errors.DockerException: Error while fetching server API version: 500 Server Error: Internal Serve
r Error ("b'open \\\\.\\pipe\\docker_engine_linux: The system cannot find the file specified.'")
[16928] Failed to execute script docker-compose` means you need to make sure Docker has finished starting up and is currently running.
1. Open Jupyter Lab notebook by typing `localhost:8888/lab/` in the browser or `http://localhost:8888/rstudio` for RStudio.
1. Stop Docker container with CTRL+C and then `docker-compose.exe down`


## Helpful Hints
Jupyter Notebooks can read in both the ESRI feature layer and the CSV. 

Ex: JHU global province-level time-series [feature layer](http://lahub.maps.arcgis.com/home/item.html?id=20271474d3c3404d9c79bed0dbd48580) and [CSV](https://lahub.maps.arcgis.com/home/item.html?id=daeef8efe43941748cb98d7c1f716122)

**Import the CSV**

All you need is the item ID of the CSV item. We use an f-string to construct the URL and use Python `pandas` package to import the CSV.

```
JHU_GLOBAL_ITEM_ID = "daeef8efe43941748cb98d7c1f716122"

JHU_URL = f"http://lahub.maps.arcgis.com/sharing/rest/content/items/{JHU_GLOBAL_ITEM_ID}/data"

TESTING_URL = (
    "https://raw.githubusercontent.com/CityOfLosAngeles/covid19-indicators"
    "master/data/county-city-testing.csv"
)

import pandas as pd

df = pd.read_csv(JHU_URL)
df = pd.read_csv(TESTING_URL)
```

**Import from data catalog**
```
import intake
import pandas as pd

catalog = intake.open_catalog("../catalog.yml")

# See files are inside catalog
list(catalog)

# To open a file called hospital_surge_capacity:
df = catalog.ca_hospital_surge_capacity.read()
```

**Import ESRI feature layer**

* From the feature layer, click on `service URL`.
* Scroll to the bottom and click `Query`
* Fill in the following parameters:
    * WHERE: 1=1
    * Out Fields (fill in the list of columns to retrieve): Province_State, Country_Region, Lat, Long, date, number_of_cases, number_of_deaths, number_of_recovered, ObjectId
    * Format: GeoJSON
    * Query (GET)
* Now, grab the new URL (it should be quite long), and read in that URL through `geopandas`. Note: the ESRI date field is less understandable, and converting it to pandas datetime will be incorrect.

```
FEATURE_LAYER_URL = "http://lahub.maps.arcgis.com/home/item.html?id=20271474d3c3404d9c79bed0dbd48580"

SERVICE_URL = "https://services5.arcgis.com/7nsPwEMP38bSkCjy/arcgis/rest/services/jhu_covid19_time_series/FeatureServer/0"

CORRECT_URL = "https://services5.arcgis.com/7nsPwEMP38bSkCjy/ArcGIS/rest/services/jhu_covid19_time_series/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=Province_State%2C+Country_Region%2C+Lat%2C+Long%2C+date%2C+number_of_cases%2C+number_of_deaths%2C+number_of_recovered%2C+ObjectId&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token="


import geopandas as gpd
gdf = gpd.read_file(CORRECT_URL)
```

To convert to HTML: `jupyter nbconvert --to html --no-input --no-prompt my-notebook.ipynb`


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>