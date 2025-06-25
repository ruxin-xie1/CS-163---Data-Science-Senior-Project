import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import pandas as pd
import joblib
import numpy as np
import requests
import matplotlib.pyplot as plt
import io
import base64

from sksurv.ensemble import RandomSurvivalForest

# Register page (for multi-page app)
dash.register_page(__name__, path="/major-findings", name="Major Findings")


url = "https://raw.githubusercontent.com/EricSJSU-DataScience/CS163_project/main/RSF_model/rsf_model.joblib"
response = requests.get(url)
rsf_model = joblib.load(io.BytesIO(response.content))


naics_df = pd.read_csv("https://raw.githubusercontent.com/EricSJSU-DataScience/CS163_project/main/RSF_model/naics_2_clean.csv")
naics_options = [
    {"label": f"{row['Sector_Title']} ({row['Code']})", "value": int(row["Code"])}
    for _, row in naics_df.iterrows()
]

# Layout
layout = html.Div([
    dbc.Container([
        html.H1("Major Findings", className="text-center my-4"),

        html.H2("1. General Static Findings", className="my-4"),

        dbc.Row([
            dbc.Col([
                html.H5("• Identify survival patterns and industry trends using data visualization."),
                html.P("Businesses in sectors like Real Estate show longer survival times, while others like Manufacturing have shorter lifespans, highlighting clear industry-based survival patterns.")
            ]),
            dbc.Col([
                html.H5("• Analyze closure timing regularities across months and years."),
                html.P("Clear seasonal patterns and economic cycles emerge, with spikes in closures around December and sharp dips during crises like 2008 and 2020.")
            ]),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("• Apply Kaplan-Meier survival analysis to estimate survival probability curves."),
                html.P("KM curves reveal steep early drop-offs in survival across most industries, but with significant variation, helping identify risk levels for different business types.")
            ]),
            dbc.Col([
                html.H5("• Develop a Random Survival Forest (RSF) model to predict survival."),
                html.P("RSF models incorporate user input—such as start date, industry, and location—to predict survival rates with high interpretability using historical data.")
            ]),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("• Help new business owners make informed decisions."),
                html.P("These findings serve as decision-support tools for choosing optimal sectors, locations, and starting times based on historical success rates and projections.")
            ]),
        ]),

        html.Hr(),

        # === RSF Interactive Section ===
        html.H2("2. RSF Business Survival Predictor", className="my-4"),

        dbc.Row([
            dbc.Col([
                dbc.Label("Start Year"),
                dcc.Dropdown(
                    id="start-year",
                    options=[{"label": str(y), "value": y} for y in range(2026, 2031)],
                    value=2026
                ),

                dbc.Label("Start Month"),
                dcc.Dropdown(
                    id="start-month",
                    options=[{"label": str(m), "value": m} for m in range(1, 13)],
                    value=1
                ),

                dbc.Label("Council District"),
                dcc.Dropdown(
                    id="council-district",
                    options=[{"label": str(d), "value": d} for d in range(0, 16)],
                    value=0
                ),

                dbc.Label("NAICS Code"),
                dcc.Dropdown(
                    id="naics-code",
                    options=naics_options,
                    value=naics_options[0]["value"] if naics_options else None
                ),

                dbc.Button("Predict Survival", id="predict-btn", color="primary", className="mt-3"),
            ], md=4),

            dbc.Col([
                html.Div(id="prediction-output", className="mt-3"),
                html.Img(id="survival-plot", style={"marginTop": "20px", "width": "100%"})
            ], md=8)
        ])
    ], fluid=True)
])

# === Callbacks ===

@callback(
    [Output("prediction-output", "children"),
     Output("survival-plot", "src")],
    [Input("predict-btn", "n_clicks")],
    [Input("start-year", "value"),
     Input("start-month", "value"),
     Input("council-district", "value"),
     Input("naics-code", "value")]
)
def predict_survival(n_clicks, year, month, district, naics):
    if n_clicks is None or naics is None:
        return "", None

    # Prepare input for model
    input_df = pd.DataFrame([{
        "Start_Year": year,
        "Start_Month": month,
        "Council_District": district,
        "NAICS_Code": int(str(naics)[:2])
    }])

    # Predict survival function
    surv_func = rsf_model.predict_survival_function(input_df, return_array=False)[0]

    # Calculate survival probabilities at specific time points
    time_points = [6, 12, 36]
    prob_text = [
        f"Survival ≥ {t} months: {float(surv_func(t)):.2%}" if t <= surv_func.x[-1]
        else f"{t} months: Beyond model range"
        for t in time_points
    ]

    # Create survival curve plot
    mask = (surv_func.x >= 6) & (surv_func.x <= 60)
    x = surv_func.x[mask]
    y = surv_func.y[mask]

    plt.figure(figsize=(6, 4))
    plt.step(x, y, where="post")
    plt.title("Predicted Survival Curve (6–60 Months)")
    plt.xlabel("Months")
    plt.ylabel("Survival Probability")
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    img_data = base64.b64encode(buf.getbuffer()).decode("utf-8")
    img_src = f"data:image/png;base64,{img_data}"

    return html.Ul([html.Li(p) for p in prob_text]), img_src
