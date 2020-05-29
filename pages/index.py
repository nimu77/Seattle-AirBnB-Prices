# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import matplotlib.pyplot as plt

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## How about AirBnB?

            People love to travel. We all talk about how we want travel all around the world.

            The sad truth about travelling is that it is expensive. People want to do as much as they can in short amount of time, because this will save them tons of money.

            Major cities are a big attraction for tourist. Like I said before, travelling comes with a hefty price and in major cities it is only going to be more heftier.

            This app covers Seattle region and based on your interest of where you want to stay in Seattle, it helps you predict what is the average price you should pay around that area.

            I hope this app will help travellers all around the world who wants to visit Seattle in getting the best value for their money.

            """
        ),
        dcc.Link(dbc.Button("Let's Begin!!!", color='primary'), href='/predictions')
    ],
    md=6,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='assets/airbnb.jpg', className='img-airbnb', style={'width':'120%'})
        # dcc.Graph(figure=fig),
    ],
    md=6
)

layout = dbc.Row([column1, column2])
