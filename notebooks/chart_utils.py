"""
Functions to create charts.
"""
import altair as alt
#import altair_saver
import os
import pandas as pd
import utils

from IPython.display import display, SVG

#alt.renderers.enable('altair_saver', fmts=['svg'])
alt.themes.enable("latimes")
#alt.themes.enable("fivethirtyeight")

'''
def show_svg(image_name):
    image_path = f"../notebooks/{image_name}.svg"
    altair_saver.save(image_name, image_path)
    display(SVG(filename = image_path))
    os.remove(image_path)
'''    

two_weeks_ago = utils.two_weeks_ago


def make_chart(df, county_name, start_date):
    
    # Subset by county and start date
    df = (df[(df.date2 >= start_date) & 
            (df.county == county_name)]
          # date2, which is datetime can be used in altair
          # but date will throw up a JSON-serializable error
          .drop(columns = "date")
         )
    
    
    df_two_weeks = (df[df.date2 >= pd.to_datetime(two_weeks_ago)])
    
    # Set up base charts
    '''
    The base charts are a keep certain chart characteristics over multiple charts. 
    Similar to functions, it allows us to "inherit" certain things and then add-on more customization.
    This quickly becomes handy if we're adding many, many layers.
    '''
    base = (alt.Chart(df)
        .mark_line()
        .encode(
            x=alt.X("date2", title="date")
        )
    )
    
    base_2weeks = (
        alt.Chart(df_two_weeks)
        .mark_line()
        .encode(
            x=alt.X("date2", title="date", axis=alt.Axis(format="%-m/%-d"))
        )
    )
        
    # Make cases charts    
    cases_line = (
        base
        .encode(
            y=alt.Y("cases_avg7:Q", title="7-day avg"),
        )
    )
    
    # Area chart gets us the shading
    cases_shaded = (
        base_2weeks
        .mark_area()
        .encode(
            y=alt.Y("cases_avg7:Q", title="7-day avg"),
            color=alt.value("#EAEBEB")
        )
    )

    # F-strings might come in handy for chart titles
    # You can display a string and insert code within the {}
    # Here, county_name is one of the args
    # If county_name == "los Angeles", then chart_title == "Daily New Cases: Los Angeles"
    chart_title = f"Daily New Cases: {county_name}"

    
    # Combine all the layers
    # We'll put the shaded area first, then the line
    # otherwise, the shaded area chart will cover up part of the line
    cases_chart = (
        (cases_shaded + cases_line)
        .properties(
              title=chart_title, width=300, height=200
        )
        .configure_title(fontSize = 14, font = "Roboto",
                         color = "black", anchor = "middle")
        )
    
    display(cases_chart)