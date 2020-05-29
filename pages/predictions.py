# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
import numpy as np

# Imports from this application
from app import app

pipeline = load('assets/random_pipeline.joblib')
print('pipeline loaded')
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Choose your features', className='mb-5'),
        dcc.Markdown('#### Bedrooms'),
        dcc.Slider(
            id='bedrooms',
            min=1,
            max=10,
            step=0.5,
            value=1,
            marks={n: str(n) for n in range(1,10)},
            className='mb-5',
        ),
        dcc.Markdown('#### Address'),
        dcc.Dropdown(
            id='address',
            options = [
                {'label': 'Seattle', 'value': '2'},
                {'label': 'Bellevue', 'value': '3'},
                {'label': 'Kirkland', 'value': '1'},
                {'label': 'Redmond', 'value': '4'},
                {'label': 'Newcastle', 'value': '6'},
                {'label': 'Mercer Island', 'value': '6'},
                {'label': 'Renton', 'value': '5'},
                {'label': 'Other', 'value': '8'},
            ],
            value = '2',
            className='mb-5',
        ),
        dcc.Markdown('#### Room Type'),
        dcc.Dropdown(
            id='room_type',
            options = [
                {'label': 'Entire Home/Apt', 'value': '1'},
                {'label': 'Private Room', 'value': '2'},
                {'label': 'Shared Room', 'value': '3'},
            ],
            value = 1,
            className='mb-5',
        ),
        dcc.Markdown('#### Overall Satisfaction'),
        dcc.Slider(
            id='overall_satisfaction',
            min=1,
            max=5,
            step=0.1,
            value=1,
            marks={1: '1',
                   2: '2',
                   3: '3',
                   4: '4',
                   5: '5'},
            className='mb-5',
        ),
        dcc.Markdown('#### Accommodates'),
        dcc.Slider(
            id='accommodates',
            min=1,
            max=24,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,24, 2)},
            className='mb-5',
        ),
    ],
    md=6,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## ', className='mb-5'),
        dcc.Markdown('#### Bathrooms'),
        dcc.Slider(
            id='bathrooms',
            min=1,
            max=8,
            step=0.5,
            value=1,
            marks={1: '1',
                   2: '2',
                   3: '3',
                   4: '4',
                   5: '5',
                   6: '6',
                   7: '7',
                   8: '8'},
            className='mb-5',
        ),
        dcc.Markdown('#### Reviews'),
        dcc.Input(
            id='reviews',
            type='number',
            placeholder='Enter here...',
            value=0,
            className='mb-5',

        # dcc.Slider(
        #     id='reviews',
        #     min=0,
        #     max=500,
        #     step=1,
        #     value=1,
        #     marks = {0: '0',
        #              50: '50',
        #              100: '100',
        #              150: '150',
        #              200: '200',
        #              250: '250',
        #              300: '300',
        #              350: '350',
        #              400: '400',
        #              450: '450',
        #              500: '500'},
        #     className='mb-5',
        ),
        dcc.Markdown('#### Latitude'),
        # html.Label('Latitude Range from 47.508 to 47.723'),
        # dcc.Input(
        #     id='reviews',
        #     placeholder='Enter a value...',
        #     value=47.508,
        #     className='mb-5',
        dcc.Slider(
            id='latitude',
            min=47.51,
            max=47.723,
            step=0.01,
            value=47.72,
            marks={n: format(n) for n in np.arange(47.51, 47.72, 0.05).round(decimals=2)},
            vertical=False,
            className='mb-5',
        ),
        dcc.Markdown('#### Longitude'),
        dcc.Slider(
            id='longitude',
            min=-122.42,
            max=-122.11,
            step=0.01,
            value=-122.42,
            marks={n: format(n) for n in np.arange(-122.42, -122.11, 0.05).round(decimals=2)},
            vertical=False,
            className='mb-5',
        ),
    ],
    md=6
)




# column2 = dbc.Col(
#     [
#         dcc.Markdown('#### Bathrooms'),
#         dcc.Slider(
#             id='bathrooms',
#             min=1,
#             max=8,
#             step=1,
#             value=1,
#             marks={1: '1',
#                    2: '2',
#                    3: '3',
#                    4: '4',
#                    5: '5',
#                    6: '6',
#                    7: '7',
#                    8: '8'},
#             className='mb-5',
#         ),
#         dcc.Markdown('#### Reviews'),
#         dcc.Slider(
#             id='reviews',
#             min=0,
#             max=500,
#             step=1,
#             value=1,
#             marks = {0: '0',
#                      50: '50',
#                      100: '100',
#                      150: '150',
#                      200: '200',
#                      250: '250',
#                      300: '300',
#                      350: '350',
#                      400: '400',
#                      450: '450',
#                      500: '500'},
#             className='mb-5',
#         ),
#         dcc.Markdown('#### Room Type'),
#         dcc.Dropdown(
#             id='room_type',
#             options = [
#                 {'label': 'Entire Home/Apt', 'value': '1'},
#                 {'label': 'Private Room', 'value': '2'},
#                 {'label': 'Shared Room', 'value': '3'},
#             ],
#             value = 'Entire Home/Apt',
#             className='mb-5',
#         ),
#         dcc.Markdown('#### Latitude'),
#         dcc.Slider(
#             id='latitude',
#             min=47.624349,
#             max=47.722770,
#             step=0.0000001,
#             value=47.624349,
#             marks={n: format(n) for n in np.arange(47.624349, 47.722771, .0000001)},
#             className='mb-5',
#         ),
#         dcc.Markdown('#### Accommodates'),
#         dcc.Slider(
#             id='accommodates',
#             min=1,
#             max=24,
#             step=0.1,
#             value=1,
#             marks={1: '1',
#                    2: '2',
#                    3: '3',
#                    4: '4',
#                    5: '5'},
#             className='mb-5',
#         ),
#     ],
#     md=6,
# )
#
column3 = dbc.Col(
    [
        html.H2('You might find a room for...', className='mb-5'),
        html.Div(id='prediction-content', className='lead')

    ]
)
#
#

# layout = dbc.Row([column1, column2, column3])
#
@app.callback(
    Output('prediction-content', 'children'),
    [Input('reviews', 'value'), Input('overall_satisfaction', 'value'),
    Input('accommodates', 'value'),Input('bedrooms', 'value'),
    Input('bathrooms', 'value'),Input('latitude', 'value'), Input('longitude', 'value'),
    Input('room_type', 'value'), Input('address', 'value')],
)
def predict(reviews, overall_satisfaction, accommodates, bedrooms,
            bathrooms, latitude, longitude, room_type, address):
    df = pd.DataFrame(
        columns=['reviews', 'overall_satisfaction', 'accommodates', 'bedrooms',
                'bathrooms', 'latitude', 'longitude', 'room_type', 'address'],
        data=[[reviews, overall_satisfaction, accommodates, bedrooms,
               bathrooms, latitude, longitude, room_type, address]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'${y_pred:.0f} per night'
# @app.callback(
#     # Output(component_id='out1', component_property='children'),
#     Output(component_id='my-daq-gauge', component_property='value'),
#     [Input(component_id='slider1', component_property='value')]
# )
# def update_output_div(input_value):
#     return input_value
layout = dbc.Row([column1, column2, column3])
