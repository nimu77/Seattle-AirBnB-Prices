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
        dcc.Markdown(
            """

            ## Process

            This app is able to make prediction based on dataset from [Kaggle]
            (https://www.kaggle.com/shanelev/seattle-airbnb-listings).
            First, the data from [Kaggle]
            (https://www.kaggle.com/shanelev/seattle-airbnb-listings) was placed
            on a pandas dataframe. After, cleaning the data, I divided the dataset
            into train and test set.

            After, dividing the dataset, I wrangled both train and test set, so that
            there was no **zero** values and also rounded the decimal points for latitude
            and longitude to two decimal points.

            For, my final prediction model I used Randomized Search CV with pipeline
            included with **ce.OrdinalEncoder**, **SimpleImputer**, and **RandomForest
            Regressor**. With my final model, I was able to test multiple other process
            to look for feature importances, permutation importance, partial dependence
            plot with one and two features, and also look at the shapely plots to see
            which features played a crucial role in increasing or decreasing the
            price of the AirBnB rentals.

            Here, is the pdp plot with one feature.
            ![](assets/pdp_one.jpg)

            Now, let's look at the pdp plot with two features.  
            ![](assets/pdp_with_two.jpg)

            The most interesting part of this whole project was to look at the shapely
            plot, and how it is able to show us which features affect the target
            variable the most. The graph is very descriptive and shows features that
            decreases or increases the price of the rentals. I narrowed down to one
            observation and then feeded the single observation to shapely to produce this
            graph.
            ![](assets/shapely.jpg)


            """
        ),
    ],
)

layout = dbc.Row([column1])
