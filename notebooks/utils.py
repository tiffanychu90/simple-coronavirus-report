"""
Functions to create county or state-specific indicators.
Use JHU county data.
Specific City of LA data also used to generate LA-specific charts. 
"""
import numpy as np
import pandas as pd
import pytz

import default_parameters
import make_charts
import useful_dict

from datetime import date, datetime, timedelta
from IPython.display import display, Markdown

S3_FILE_PATH = "s3://public-health-dashboard/jhu_covid19/"

US_COUNTY_URL = f"{S3_FILE_PATH}us-county-time-series.parquet"


CROSSWALK_URL = (
    "https://raw.githubusercontent.com/tiffanychu90/simple-indicators/master/data/"
    "msa_county_pop_crosswalk.csv"
)

#---------------------------------------------------------------#
# Default parameters
#---------------------------------------------------------------#
yesterday_date = default_parameters.yesterday_date
today_date = default_parameters.today_date
fulldate_format = default_parameters.fulldate_format
monthdate_format = default_parameters.monthdate_format

#---------------------------------------------------------------#
# Case Data (County)
#---------------------------------------------------------------#
"""
Make cases and deaths chart for county / state / MSA.
Some data cleaning for by geographic level (listed in 1, 2a, 2b, 2c)
Call functions to make charts.
"""
# County Case Data
def county_case_charts(county_state_name, start_date):
    df = prep_county(county_state_name, start_date)
    name = df.county.iloc[0]
    # 'date' column is not JSON serializable...
    # If we drop and use date2, chart will work (https://github.com/altair-viz/altair/issues/1355) 
    make_charts.make_cases_deaths_chart(df, "county", name)
    return df


"""
Sub-functions for case, deaths data.
"""
# (1) Sub-function to prep all US time-series data
def prep_us_county_time_series():
    df = pd.read_parquet(US_COUNTY_URL)
    df = df.assign(
        date=pd.to_datetime(df.date).dt.date,
        state_abbrev=df.state.map(useful_dict.us_state_abbrev),
    )
    
    return df


# (2a) Sub-function to prep county data
def prep_county(county_state_name, start_date):
    df = prep_us_county_time_series()

    # Parse the county_state_name into county_name and state_name (abbrev)
    if "," in county_state_name:
        state_name = county_state_name.split(",")[1].strip()
        county_name = county_state_name.split(",")[0].strip()

        if len(state_name) > 2:
            state_name = useful_dict.us_state_abbrev[state_name]

        # County names don't have " County" at the end. There is a TriCounty, UT though.
        if " County" in county_name:
            county_name = county_name.replace(" County", "").strip()

    elif any(map(str.isdigit, county_state_name)):
        state_name = df[df.fips == county_state_name].state_abbrev.iloc[0]
        county_name = df[df.fips == county_state_name].county.iloc[0]

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

    df = (
        df[
            (df.county == county_name)
            & (df.state_abbrev == state_name)
        ][keep_cols]
        .sort_values(["county", "state", "fips", "date"])
        .reset_index(drop=True)
    )
    
    # Merge in population
    pop = (pd.read_csv(CROSSWALK_URL, dtype={"county_fips": "str", "cbsacode": "str"})
           [["county_fips", "county_pop"]]
           .rename(columns = {"county_fips": "fips"})
          )

    df = pd.merge(df, pop,
                  on = "fips", how = "inner", validate = "m:1"
    )
    
    df = calculate_rolling_average(df, start_date, today_date)
    df = find_tier_cutoffs(df, "county_pop")
    
    return df


def calculate_rolling_average(df, start_date, today_date):
    # Drop any NaNs or rolling average will choke
    df = df.dropna(subset = ["new_cases", "new_deaths"])
    
    # Derive new columns
    df = df.assign(
        cases_avg7=df.new_cases.rolling(window=7).mean(),
        deaths_avg7=df.new_deaths.rolling(window=7).mean(),
    )    
    
    # Subset from start date up to yesterday's date
    # Have version of date that we can use in chart
    df = df.assign(
        date2 = pd.to_datetime(df.date)
    )   
    
    df = df[(df.date >= start_date) & (df.date < today_date)]
    
    return df


def find_tier_cutoffs(df, population_col):
    
    # Use CA's definition of what is widespread vs minimal
    population = df[population_col]
    POP_DENOM = 100_000
    
    df = df.assign(
        tier1_case_cutoff = round(((1 / POP_DENOM) * population), 2),
        tier2_case_cutoff = round(((4 / POP_DENOM) * population), 2),
        tier3_case_cutoff = round(((7 / POP_DENOM) * population), 2),
    )
    
    return df



#---------------------------------------------------------------#
# Calculate doubling time on JHU case data
#---------------------------------------------------------------#
def days_since_100_cases(df, sort_cols, group_cols):
    
    # Start counting day 1 as when 100 cases is reached
    df = df.assign(
        gt_100cases = df.apply(lambda x: 1 if x.cases >= 100 else 0, axis=1)
    )

    df = df.assign(
        days_obs = df.sort_values(sort_cols).groupby(group_cols).cumcount() + 1
    )

    
    return df

def doubling_time(df, window=7):
    sort_cols = ["fips", "county", "date"]
    group_cols = ["fips", "county", "gt_100cases"]
    
    df = days_since_100_cases(df, sort_cols, group_cols)
    
    shift_amt = (window - 1)
    df = df.assign(
        cases_in_past = (df.sort_values(sort_cols)
                           .groupby(group_cols)["cases"]
                           .apply(lambda x: x.shift(shift_amt))
                          ),
        days_in_past = (df.sort_values(sort_cols)
                          .groupby(group_cols)["days_obs"]
                          .apply(lambda x: x.shift(shift_amt))
                         ),
    )
    
    np.seterr(divide='ignore')
    #https://stackoverflow.com/questions/27784528/numpy-division-with-runtimewarning-invalid-value-encountered-in-double-scalars?rq=1
    df = df.assign(
        doubling_time = ( ((df.days_obs - df.days_in_past) * np.log(2)) / 
                        ( np.log(df.cases / df.cases_in_past) )
                       ),
    )
    
    # Set doubling time to NaN if it's before 100 cases
    df = df.assign(
        doubling_time = df.apply(lambda x: x.doubling_time if x.gt_100cases==1 
                                 else np.nan, axis=1)
    )
    
    drop_cols = ["gt_100cases", "days_in_past", "cases_in_past", "days_obs"]
    
    df = df.drop(columns = drop_cols)
    
    return df