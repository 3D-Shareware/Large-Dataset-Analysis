import pandas as pd
import plotly.express as px
import csv
import os

# date is year/month/day
# temp is average temp, in celcius
# wind is top speed, in km/h
# precip should be a formatted array
# icon should have associated images
# description is simply a string
def create_record(icon: str, datetime: str, temp: float, windspeed: float, preciptype: str, description: str):
    return {
        "icon": icon,
        "Date": datetime,
        "Temperature (°C)": float(temp),
        "Wind speed (km/h)": float(windspeed),
        "preciptype": preciptype,
        "description": description
    }

def load_weather_data(filepath):
    weather_list = []                                 # Initialize empty list to hold city dictionaries
    with open(filepath, newline='') as f:          # Open the CSV file for reading
        reader = csv.DictReader(f)                 # Read CSV rows into dictionaries
        for row in reader:                         # Loop through each row in the CSV
            day = create_record(             # Create a city dictionary from row data
                row['icon'],
                row['datetime'],
                row['temp'],
                row['windspeed'],
                row['preciptype'],
                row['description']
            )
            weather_list.append(day)                 # Add created city dictionary to list
    return weather_list    

def plot_it(weather_list):
    df = pd.DataFrame(weather_list)                                      # Convert city list to pandas DataFrame              # Select top 5 by growth
    fig = px.pie(df, values="Wind speed (km/h)", names="Date", title="Days with ice precipitation and their comparative wind speeds")
    fig.show()

plot_it(load_weather_data("dc_weather_ice_only.csv"))