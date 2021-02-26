"""
Utility functions.
Can be reused across multiple noteboks
"""
import datetime
import intake
import pandas as pd

catalog = intake.open_catalog("../catalog.yml")

"""
This is an example of a .py file I created, and now want to import
It contains a dictionary, which contains a list of key-value pairs
For every key, there is a value.
In this case, for every state's full name (key), the abbreviation (value) is listed, and vice versa

To use:
useful_dict.us_state_abbrev 
"""
import useful_dict

# Define some default parameters to use across notebooks
fulldate_format = "%-m/%-d/%y"
time_zone = "US/Pacific"
start_date = datetime.datetime(2020, 4, 15).date()
two_weeks_ago = (
    (datetime.date.today()
        - datetime.timedelta(days=15)
    )
)


# Calculate a 7-day rolling average
def calculate_rolling_average(df):
    # Drop any NaNs or rolling average will choke
    df = df.dropna(subset = ["new_cases", "new_deaths"])
    
    # Derive new columns
    df = df.assign(
        date2 = pd.to_datetime(df.date),
        cases_avg7=df.new_cases.rolling(window=7).mean(),
        deaths_avg7=df.new_deaths.rolling(window=7).mean(),
    )     
        
    return df

# Clean the JHU county data at once
def clean_jhu():
    # Import data
    df = catalog.jhu_us_cases_parquet.read()
    
    # Get some new columns
    df = df.assign(
        date=pd.to_datetime(df.date).dt.date,
        state_abbrev=df.state.map(useful_dict.us_state_abbrev),
    )
    
    # Define which columns to keep, drop the rest
    keep_cols = [
        "county",
        "state",
        "state_abbrev",
        "fips",
        "date",
        "Lat",
        "Lon",
        "cases",
        "deaths",
        "new_cases",
        "new_deaths",
    ]
    
    # We'll subset and only keep certain columns
    # Then sort our data according to county-state-fips-date, so everything is in the right order
    # before we calculate rolling averages
    # reset_index just re-orders our index so everything is labeled in the right sort order
    df1 = (df[keep_cols]
        .sort_values(["county", "state", "fips", "date"])
        .reset_index(drop=True)
    )
    
    # Bring in population crosswalk
    pop = catalog.msa_county_crosswalk.read()
    
    # Only need certain columns
    pop = (pop[["county_fips", "county_pop"]]
           .rename(columns = {"county_fips": "fips"})
          )
    
    # Merge cases with population
    df2 = pd.merge(df1, pop,
                  on = "fips", how = "inner", validate = "m:1"
    )
    
    # Call the function we just defined above
    # Can roll-up sub-functions into main functions as one way to keep things clean
    df3 = calculate_rolling_average(df2)
    
    return df3