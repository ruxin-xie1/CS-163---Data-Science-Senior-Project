import dash
from dash import html

dash.register_page(__name__, path="/objective-goals-datasets", name="Objective, Goals, and Datasets")

layout = html.Div(
    className="container mt-4",
    style={
        'background-color': '#fff8e7', 
        'padding': '20px', 
        'border-radius': '10px', 
        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)'
    },
    children=[
        html.H1("Project Objectives and Dataset", className="mb-4", style={'textAlign': 'center'}),
        
        html.H2("Project Goals", style={'color': '#3a3a3a'}),
        html.Ul([
            html.Li("Identify survival patterns and industry trends using data visualization."),
            html.Li("Analyze closure timing regularities across months and years to detect cyclical risks."),
            html.Li("Apply Kaplan-Meier survival analysis to estimate survival probability curves."),
            html.Li("Develop a Random Survival Forest (RSF) model to predict future business survival chances."),
            html.Li("Help new business owners make informed decisions based on survival predictions."),
        ]),
        
        html.H2("Dataset Overview", className="mt-4", style={'color': '#3a3a3a'}),
        html.P(
            "The dataset includes historical records of business openings and closures within Los Angeles. "
            "Key attributes include industry classification (NAICS code), council district location, business start and end dates, "
            "and other demographic and operational factors."
        ),
        
        html.H2("Broader Impacts", className="mt-4", style={'color': '#3a3a3a'}),
        html.P(
            "The project aims to provide valuable insights for entrepreneurs, city planners, investors, and policymakers. "
            "By understanding survival dynamics, we can forecast economic stability, identify high-risk periods for new ventures, "
            "and improve resource allocation strategies."
        ),
        
        html.H2("Dataset Summary", className="mt-4", style={'color': '#3a3a3a'}),
        html.Ul([
            html.Li("Start Date: Provided for each business."),
            html.Li("End Date: Provided if the business has closed."),
            html.Li("NAICS Codes: Standardized 2-digit industry sector codes."),
            html.Li("Council District: Numeric district identifier (0–15) representing geographical area."),
        ]),
        
        html.H2("Handling Missing Data", className="mt-4", style={'color': '#3a3a3a'}),
        html.P(
	    "After dropping missing data in the columns for NAICS, LOCATION, coordinates, start dates, and end dates, around 500,000 entries remained."
        )
        
      ]
)
