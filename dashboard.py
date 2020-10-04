import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

from functions_file import solar_data, wind_data

solar = solar_data()
wind = wind_data()

data = go.Bar(x = solar.index, y = solar['Power_Predictions'])
layout =go.Layout(title =  "Solar Predictions",
                  xaxis = {'title': 'Day of Month'},
                  yaxis = {'title': 'Power (MW)'})
data_1 = go.Bar(x = solar.index, y = wind['Power_Predictions'])
layout_1 =go.Layout(title =  "Wind Predictions",
                  xaxis = {'title': 'Day of Month'},
                  yaxis = {'title': 'Power (MW)'})

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure= {'data': [data],
                'layout':layout}
    ),
    dcc.Graph(
        id='wind',
        figure= {'data': [data_1],
                'layout':layout_1}
    )
])

if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
