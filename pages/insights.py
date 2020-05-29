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

            The baseline for predicting AirBnB rentals was $106.77, with a mean
            absolute error of $49.46 on average. To improve the baseline, I first introduced linear
            regression. Linear regression improved the mean absolute error to $34.30 on average.
            This was a really good jump from $49 to $34, even though it is the most simple
            model.
            """
        ),
        html.Img(src='assets/linear_rel.jpg', className='linear',
                 style={'width':'70%', 'height':'30%'}),
        html.Br(),
        html.Div([
			html.Br(),
			html.P(
			"""
            After, fitting Linear Regression, I fitted other regression models like
            ridge, decision tree, random forest, and randomized search cv. Out of all these
            models randomized cv was able to produce the best result without overfitting
            the model and also giving the best mean absolute error on average. The mean
            absolute error dropped down to $31.42.

            I was also able to look at the feature importances of each feature towards the
            target which is price. The graph below shows the feature importances of each
            feature.
			"""
            ),
        ]),
		html.Img(src='assets/f_importance.jpg', className='feature_imp'),
		html.Br(),
		html.Div([
			html.Br(),
            html.P(
			"""
            Also, to see the best possible ways to find how important the feature really is
            I tried Permuatation Importance. Permutation Importance shuffles one feature
            at a time, keeping other features constant to see how important each feature
            is if the value is not constant. Here, is the Permutation Importance for each
            feature.
			"""
            ),
        ]),
        html.Img(src='assets/permutation.jpg', className='permutation'),
	]
)

layout = dbc.Row([column1])
