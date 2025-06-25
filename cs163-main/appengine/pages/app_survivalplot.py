import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State, no_update
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# ---------------------
# Step 1. Data Loading
# ---------------------
time_start = time.time()
# business_filtered.csv
url = "https://media.githubusercontent.com/media/EricSJSU-DataScience/CS163_project/refs/heads/main/dataset/business_filtered.csv"
url_1980 = "https://raw.githubusercontent.com/EricSJSU-DataScience/CS163_project/refs/heads/main/dataset/business_filtered_1980after.csv"
url_2000 = "https://raw.githubusercontent.com/EricSJSU-DataScience/CS163_project/refs/heads/main/dataset/business_filtered_2000after.csv"

df = pd.read_csv(url_1980, usecols=["NAICS", "is_open", "duration"])
df["NAICS-2"] = df["NAICS"].map(lambda n: int(n / 10000))
# NAICS info csv
naics_file = "https://raw.githubusercontent.com/EricSJSU-DataScience/CS163_project/refs/heads/main/dataset/naics_2_clean.csv"
df_naics = pd.read_csv(naics_file)
code_sector_dict = df_naics.set_index("Code")["Sector_Title"].to_dict()
df["NAICS-2_Title"] = df["NAICS-2"].map(code_sector_dict)
time_end = time.time()
print(f"survivalplot\tdata Loading completed!\tTime: {(time_end - time_start): .1f} second")


# ---------------------
# Function Definitions
# ---------------------
def plot_kaplan_meier_by_industries(df, industries, max_time=240, y_lower=0.4):
    """
    Computes and returns a Plotly figure with Kaplan-Meier survival curves for multiple industries.

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame that must include:
         - 'is_open': dataset modify to boolean dtype recently
         - 'duration': the duration (in months) of each business.
         - 'NAICS-2_Title': the industry classification.
    industries : list
        List of industry names to filter on.
    max_time : int, optional
        Maximum time (in months) to display on the x-axis (default is 600).

    Returns:
    --------
    fig : plotly.graph_objects.Figure
        Figure containing Kaplan-Meier survival curves.
    """
    time_start = time.time()
    fig = go.Figure()

    # Loop over each industry in the provided list.
    for industry in industries:
        # Filter for closed businesses in the given industry.
        # original idea may wrong, survival analysis should keep both.
        if pd.isna(industry):
            df_ind = df[(df["NAICS-2_Title"].isna())].copy()
            industry_label = "NaN"
        else:
            df_ind = df[(df["NAICS-2_Title"] == industry)].copy()
            industry_label = industry

        # Skip if no data is available for this industry.
        if df_ind.empty:
            continue

        # Round the duration values.
        df_ind["duration_rounded"] = df_ind["duration"].round(1)

        # Count the number of closures (events) at each unique rounded duration.
        # event_counts = df_ind["duration_rounded"].value_counts().sort_index()
        event_counts = df_ind[df_ind["is_open"] == False]["duration_rounded"].value_counts().sort_index()
        unique_times = event_counts.index

        # Compute the number at risk just before each event time.
        n_at_risk = [(df_ind["duration_rounded"] >= t).sum() for t in unique_times]

        # Compute the Kaplan-Meier survival probabilities.
        survival_probs = []
        cum_survival = 1.0
        for t, d, n in zip(unique_times, event_counts, n_at_risk):
            cum_survival *= 1 - d / n
            survival_probs.append(cum_survival)

        # Add a step-like trace for the current industry.
        fig.add_trace(
            go.Scatter(
                x=list(unique_times),
                y=survival_probs,
                mode="lines",
                line_shape="hv",  # horizontal-vertical step plot
                name=str(industry_label),
                text=[
                    f"Industry: {industry_label}<br>Duration: {t} months<br>Survival: {prob:.2f}"
                    for t, prob in zip(unique_times, survival_probs)
                ],
                hoverinfo="text",
            )
        )

    # Define x-axis ticks (every 12 months).
    xticks = list(np.arange(0, max_time + 12, 12))
    # y_lower = 0.2
    
    # Update the layout.
    fig.update_layout(
        title="Kaplan-Meier Survival Curves by Industry",
        xaxis_title="Duration (Months)",
        yaxis_title="Survival Probability",
        xaxis=dict(
            range=[0, max_time], tickmode="array", tickvals=xticks, tickangle=-45
        ),
        yaxis=dict(
            range=[y_lower, 1], 
            tickmode="linear", 
            dtick=0.05, 
            ticks="outside",
            ticklabelposition="outside",
            # ticklabelindex=10
        ),
        legend=dict(
            title="Industry", font=dict(size=10), xanchor="right", yanchor="top"
        ),
        width=1000,
        height=600,
    )
    time_end = time.time()
    print(f'survivalplot\tFunction survival curve: {(time_end - time_start): .1f} second')

    return fig


# ---------------------
# Industry List for Filtering
# ---------------------
industry_list = [
    "Retail Trade",
    "Arts, Entertainment, and Recreation",
]
# Create checklist options from the industry list.
# there is null value, add if statement to filter out null value
industry_options = [
    {"label": industry, "value": industry} 
    for industry in df['NAICS-2_Title'].unique() if pd.notnull(industry)
]


# ---------------------
# Define the layout for the Survival Plot component
# ---------------------
def get_survival_plot_component():
    return html.Div([
        html.H3("Kaplan-Meier Survival Analysis Dashboard"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Button(
                        "Select Industries",
                        id="open-collapse-survival",
                        color="primary",
                        className="mb-2",
                    ),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col(
                                        html.Div("Pick one or more industries:"),
                                        width="auto"
                                    ),
                                    dbc.Col(
                                        # Clear Button 
                                        dbc.Button(
                                            "Clear",
                                            id="clear-button-survival",
                                            color="secondary",
                                            style={
                                                "height": "20px",
                                                "width": "60px",
                                                "fontSize": "10px",
                                                "padding": "0px 4px"
                                            },
                                            className="mt-2"
                                        ),
                                        width="auto"
                                    )
                                ], justify="start", align="center"),
                                dcc.Checklist(
                                    id="industry-checklist",
                                    options=industry_options,
                                    value=industry_list,  # Default selection
                                    labelStyle={"display": "block"},
                                ),
                            ])
                        ),
                        id="collapse-checklist-survival",
                        is_open=False,
                        style={
                            "position": "absolute",
                            "top": "60px", 
                            "left": "0",
                            "zIndex": "999",
                            "width": "400px"
                        },
                    ),
                ], style={"position": "relative", "display": "inline-block"}),
            ], width="auto"),
            dbc.Col([
                html.Div([
                    html.Label("Max Duration (Months):"),
                    dcc.Slider(
                        id="max-time-slider",
                        min=60,
                        max=360,
                        step=12,
                        value=240,
                        marks={i: str(i) for i in range(0, 1201, 60)},
                        tooltip={"placement": "bottom", "always_visible": True},
                    ),
                ], style={"margin": "20px 0"}),
            ], width="auto"),
            dbc.Col([
                html.Div([
                    html.Label("Survival lower bound:"),
                    dcc.Slider(
                        id="y-lower-slider",
                        min=0.2,
                        max=0.9,
                        step=0.05,
                        value=0.4,    # default
                        marks={i: f"{i:.2f}" for i in np.arange(0, 1, 0.2)},
                        tooltip={"placement": "bottom", "always_visible": True},
                    ),
                ], style={"margin": "20px 0"}),
            ], width="auto"),
            dbc.Col([
                dbc.Button(
                    "Apply",
                    id="apply-button-survival",
                    color="primary",
                    style={
                        "height": "36px",
                        "width": "100px",
                        "fontSize": "10px",
                        "padding": "2px 4px",
                    },
                    className="mt-2 ml-2",
                ),
            ], width="auto"),

        ], justify="center", align="center"),
        dcc.Graph(
            id="survival-graph", 
            figure={},
            style={"width": "100%", "height": "auto", "display": "block"}, 
            config={"responsive": True}
        ),
        html.Hr(),
    ])

# ---------------------
# App Callbacks
# ---------------------
@callback(
    Output("collapse-checklist-survival", "is_open"),
    Input("open-collapse-survival", "n_clicks"),
    State("collapse-checklist-survival", "is_open"),
)
def toggle_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


@callback(
    Output("industry-checklist", "value"), 
    Input("clear-button-survival", "n_clicks")
)
def clear_all(n_clicks):
    if n_clicks:
        return []
    return no_update


@callback(
    Output("survival-graph", "figure"),
    Input("apply-button-survival", "n_clicks"),
    State("industry-checklist", "value"),
    State("max-time-slider", "value"),
    State("y-lower-slider", "value"),
)
def update_survival_plot(n_clicks, selected_industries, max_time, y_lower):
    # If no button click yet, show survival curves for default industries.
    if n_clicks is None:
        return plot_kaplan_meier_by_industries(df, industry_list, max_time)
    if not selected_industries:
        # If no industries are selected, return an empty figure with a message.
        return {"data": [], "layout": {"title": "Please select at least one industry."}}
    return plot_kaplan_meier_by_industries(df, selected_industries, max_time, y_lower)


# ---------------------
# Export the survival_plot
# ---------------------
survival_plot = get_survival_plot_component()
