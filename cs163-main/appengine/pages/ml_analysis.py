import dash
from dash import html

dash.register_page(__name__, path="/ml", name="ML Analysis")

def alternating_layout(entries):
    children = []
    for i, (title, img_path, description) in enumerate(entries):
        is_even = i % 2 == 0
        row = html.Div(className="row align-items-center my-4", children=[
            html.Div(className="col-md-6", children=[
                html.H4(title),
                html.P(description)
            ]) if is_even else html.Div(className="col-md-6", children=[
                html.Img(src=img_path, className="img-fluid", style={"max-width": "100%"})
            ]),
            html.Div(className="col-md-6", children=[
                html.Img(src=img_path, className="img-fluid", style={"max-width": "100%"})
            ]) if is_even else html.Div(className="col-md-6", children=[
                html.H4(title),
                html.P(description)
            ])
        ])
        children.append(row)
    return children

layout = html.Div(className="container mt-4", children=[
    html.H1("Machine Learning Analysis"),
    html.H2("Long Short Term Memory (LSTM)"),
    *alternating_layout([
        ("ML1 – Model Architecture", "/assets/ml1.png", 
         "The LSTM model consists of stacked LSTM layers followed by dense and dropout layers, trained on sequential business number data over time."),
        ("ML2 – Business Number Prediction (Test)", "/assets/ml2.png", 
         "The test results show that the LSTM model accurately tracks actual business trends from 2000 to 2024, with a high correlation between predicted and actual values."),
        ("ML3 – Future Forecasting", "/assets/ml3.png", 
         "The model forecasts business numbers for 2025 to 2027, continuing the growth trend and capturing seasonal variations based on past patterns."),
    ]),
    html.H2("Random Survival Forest (RSF)"),
    *alternating_layout([
        ("MLA – Model Parameters", "/assets/mla.png", 
         "The RSF model is configured with 6 trees, depth of 5, and uses 'Council District' and 'NAICS Code' to estimate survival probability of businesses over time."),
        ("MLB – Predicted Survival Curve", "/assets/mlb.png", 
         "For a business starting in 2026 in Council District 3 and NAICS Code 53, the survival probability declines from 50% to below 20% within 60 months."),
        ("MLC – Model Performance (C-index)", "/assets/mlc.png", 
         "The model achieves a Concordance Index of 0.7574, indicating strong predictive power and consistent ranking of business survival times.")
    ])
])
