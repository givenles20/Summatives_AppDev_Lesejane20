import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app= Flask(__name__)


import pandas as pd
import pickle
import requests
import json
from pandas.io.json import json_normalize

def solar_data():
    api_key = "593915a71f21b2521da414e9f5f86127"
    lat = "-19.42"
    lon = "142.11"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data1 = json.loads(response.text)['daily']
    df = pd.json_normalize(data1)
    datetime_series = pd.to_datetime(df['dt'],unit='s')
    datetimeseries1=datetime_series.dt.normalize()
    datetime_index = pd.DatetimeIndex(datetimeseries1.values).day
    df2=df.set_index(datetime_index)
    columns= ['clouds']
    solar=df2[columns]
    solar1 = solar.rename(columns={'clouds': 'Cloud Cover Percentage'})
    X1=solar1.values
    name="solar_pickle_model.sav"
    loaded_model = pickle.load(open(name,'rb'))
    predictions= loaded_model.predict(X1)
    solar1['Power_Predictions'] = predictions
    return solar1


def wind_data():
    api_key = "593915a71f21b2521da414e9f5f86127"
    lat = "8.598084"
    lon = "53.556563"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data1 = json.loads(response.text)['daily']
    df = pd.json_normalize(data1)
    datetime_series = pd.to_datetime(df['dt'],unit='s')
    datetimeseries1=datetime_series.dt.normalize()
    datetime_index = pd.DatetimeIndex(datetimeseries1.values).day
    df2=df.set_index(datetime_index)
    cols = ['wind_speed']
    windy=df2[cols]
    wind = windy.rename(columns={'wind_speed': 'wind speed'})
    W1=wind.values
    name="wind_pickle_model.sav"
    loaded_model = pickle.load(open(name,'rb'))
    wind_pred= loaded_model.predict(W1)
    wind['Power_Predictions'] = wind_pred
    return wind

if __name__ == "__main__":
    #app.run(debug=false)
    app.run(host = '127.0.0.1',port = 5000, debug=False)
