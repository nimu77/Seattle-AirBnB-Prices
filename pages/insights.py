# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.H2("Insights"),
        dcc.Markdown(
            """
            Considering the turmoil that we are facing right now, this market is
            very unpredictable in current condition. Nevertheless, I wanted to
            do some research on AirBnb market. Short-term rentals has
            grown exponentially over the years. To meet the demands and to create
            a fresh new approach in the market, AirBnb was founded back in 2008. I
            narrowed down my research to just one city and only for the year 2018.
            Seattle is a famous city, it is mostly known for its lush evergreen forests,
            but thats not all, it is also famous for its coffee, culture, sports, tech
            industry and for general outdoor lifestyle. So, what I am trying to say
            is Seattle attracts people from any background.

            For this predictive model, I retrieved the dataset from [Kaggle]
            (https://www.kaggle.com/shanelev/seattle-airbnb-listings). The motive of
            this app is to predict rental price for AirBnB in Seattle. Given that,
            the dataset was from 2018, all future predictions based on this dataset
            should account for inflation and exclude market extremities like we are
            facing right now with COVID-19.





            """
        ),
        html.Img(src='assets/airbnb.jpg', className='img-airbnb', style={'width':'80%'}),
        html.Br(),
        html.Div([
			html.Br(),
			html.P(
			"""
			The next two graphs are called partial dependence plots.
			The line represents change in prediction based on
			adjusting the feature's value. In the graph below, predictions
			are either positively or negatively affected by changing
			your guitar brand from say, a Peavey to a Gibson.
			"""),
			html.Img(src='assets/brand_pdp.png', className='img-fluid')
		]),
		html.Br(),
		html.Div([
			dcc.Markdown(
			"""
			In the chart below, you can see how an exclusive change in
			the country of manufacture drives price prediction up or
			down from a baseline.
			"""),
			html.Img(src='assets/country_pdp.png', className='img-fluid')
		])
    ],
)

layout = dbc.Row([column1])
