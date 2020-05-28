# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Imports from this application
from app import app

pipeline = load('assets/random_pipeline.joblib')
print('pipeline loaded')
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),

        dcc.Slider(
            id='slider1',
            min=-0,
            max=100,
            step=0.5,
            value=0,
            marks={0: '0',
                   20: '20',
                   40: '40',
                   60: '60',
                   80: '80',
                   100: '100'}
        ),

        # dcc.Markdown('', id='out1')
    ],
    md=6,
)

column2 = dbc.Col(
    [
    daq.Gauge(
        id='my-daq-gauge',
        min=0,
        max=100,
        value=50
        )
    ]
)


layout = dbc.Row([column1, column2])

@app.callback(
    # Output(component_id='out1', component_property='children'),
    Output(component_id='my-daq-gauge', component_property='value'),
    [Input(component_id='slider1', component_property='value')]
)
def update_output_div(input_value):
    return input_value
