import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
import time
from dash import no_update




# ---------------------
# Step 1. Data Loading
# ---------------------
time_start = time.time()
url = 'https://raw.githubusercontent.com/EricSJSU-DataScience/CS163_project/refs/heads/main/dataset/business_subset.csv'
df_preworked = pd.read_csv(url, dtype={"NAICS": "Int64"})
time_end = time.time()
print(f'geomap\t\tdata Loading completed!\tTime: {(time_end - time_start): .1f} second')

# ---------------------
# dictionary of NAICS 2-digits information
# ---------------------
code_sector_dict = {11: 'Agriculture, Forestry, Fishing and Hunting',
                    21: 'Mining',
                    22: 'Utilities',
                    23: 'Construction',
                    31: 'Manufacturing',
                    32: 'Manufacturing',
                    33: 'Manufacturing',
                    42: 'Wholesale Trade',
                    44: 'Retail Trade',
                    45: 'Retail Trade',
                    48: 'Transportation and Warehousing',
                    49: 'Transportation and Warehousing',
                    51: 'Information',
                    52: 'Finance and Insurance',
                    53: 'Real Estate Rental and Leasing',
                    54: 'Professional, Scientific, and Technical Services',
                    55: 'Management of Companies and Enterprises',
                    56: 'Administrative and Support and Waste… Services',
                    61: 'Educational Services',
                    62: 'Health Care and Social Assistance',
                    71: 'Arts, Entertainment, and Recreation',
                    72: 'Accommodation and Food Services',
                    81: 'Other Services (except Public Administration)',
                    92: 'Public Administration'}

# ---------------------
# Compute Zip Counts for Filter Dropdown
# ---------------------
naics_counts = df_preworked['NAICS-2'].value_counts().to_dict()
naics_options = [
    {"label": f"{code} - {code_sector_dict.get(code, 'Unknown')} ({naics_counts.get(code, 0)})", "value": code}
    for code in sorted(naics_counts.keys())
]
# default_sectors = sorted(naics_counts.keys())
default_sectors = [44, 45]

# ---------------------
# Function to Build Folium Map for a Given NAICS Sector Code
# ---------------------
def create_map_naics(selected_sector):
    st = time.time()
    # Filter businesses based on the selected NAICS-2 sector codes
    df_filtered = df_preworked[df_preworked['NAICS-2'].isin(selected_sector)].copy()
    map_center = [34.05525, -118.23737]
    # scrollWheelZoom=True -> Map can zoom by middle wheel
    business_map = folium.Map(location=map_center, zoom_start=10, scrollWheelZoom=False)
    points = df_filtered[['latitude', 'longitude']].values.tolist()
    FastMarkerCluster(points).add_to(business_map)
    et = time.time()
    print(f'geomap\t\tFunction create_map: {(et - st): 0.1f} seconds')
    return business_map._repr_html_()

# ---------------------
# Define the layout for the map component
# ---------------------
def get_map_component():
    return html.Div([
        # html.H3("Business Map Dashboard"),
        html.H4("Purpose"),
        html.P("Provide a location-based view of existing businesses by industry across Los Angeles to help new investors and business owners assess the competition and identify underserved areas before choosing a location."),
        html.Div(
            dbc.Row([

                # # instruction
                dbc.Col(
                    html.Div([
                        html.H5("Instructions"),
                        html.Ul([
                            html.Li([
                                "Click ", 
                                html.Strong("SELECT NAICS SECTORS"),
                                "."
                            ]),
                            html.Li("Check one or more industries in the pop-up."),
                            html.Li([
                                "Click ",
                                html.Strong("APPLY"),
                                " to redraw the map."
                            ]),
                        ]),
                    ])
                ),

                # # interpretation
                dbc.Col(
                    html.Div([
                        html.H5("How to Interpret"),
                        html.Ul([
                            html.Li([
                                html.Strong("Denser"),
                                " orange circles indicate ", 
                                html.Strong("more businesses"),
                                " in the area.",
                            ]),
                            html.Li([
                                "Zoom ", 
                                html.Strong("in/out"),
                                " to see neighborhood densities.",
                            ]),
                            html.Li([
                                "A higher density may lead to ",
                                html.Strong("saturation"),
                                ", while fewer circles may present ",
                                html.Strong("opportunities"),
                                " (consider local factors like zoning or demand)."
                            ]),
                        ]),
                    ])
                ),
                
            ])
        ),


        dbc.Row([
            dbc.Col([
                html.Div([
                    # Button for industry selection
                    dbc.Button(
                        "Select NAICS Sectors",
                        id="open-collapse",
                        color="primary",
                        style={
                        "height": "36px",
                        "width": "150px",
                        "fontSize": "10px",
                        "padding": "2px 4px",
                        },
                        # className="mb-2",
                        className="mt-2 ml-2",
                    ),

                    # Collapse Option for industry selection
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col(
                                        html.Div("Pick one or more NAICS Sectors:"),
                                        width="auto"
                                    ),
                                    dbc.Col(
                                        # Clear Button
                                        dbc.Button(
                                            "Clear",
                                            id="clear-button",
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
                                    id="sector-checklist",
                                    options=naics_options,
                                    value=[44, 45],  # Default selection
                                    labelStyle={"display": "block"},
                                ),
                            ])
                        ),
                        id="collapse-checklist",
                        is_open=False,
                        style={
                            "position": "absolute",
                            "top": "60px", 
                            "left": "-50px",
                            "zIndex": "999",
                            "width": "550px"
                        },
                    ),
                ], style={"position": "relative", "display": "inline-block"}),
            ], width="auto"),

            # Button Apply selection
            dbc.Col([
                dbc.Button(
                    "Apply",
                    id="apply-button",
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
        # html.Div("Map View:", style={"marginTop": 20}),
        html.Iframe(id="map", style={"width": "100%", "height": "600px", "border": "none"})
    ])


# ---------------------
# Callback to update the map
# ---------------------

# Callback to toggle the collapsible container
@callback(
    Output("collapse-checklist", "is_open"),
    Input("open-collapse", "n_clicks"),
    State("collapse-checklist", "is_open")
)
def toggle_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# Callback to clear selections
@callback(
    Output("sector-checklist", "value"),
    Input("clear-button", "n_clicks")
)
def clear_all(n_clicks):
    if n_clicks:
        return []
    return no_update

# Callback to apply selections
@callback(
    Output("map", "srcDoc"),
    Input("apply-button", "n_clicks"),
    State("sector-checklist", "value")
)
def update_map(n_clicks, selected_sectors):
    # On initial load, display the map based on the default sectors.
    if n_clicks is None:
        return create_map_naics(default_sectors)
    if not selected_sectors:
        return "<h4>Please select at least one NAICS sector.</h4>"
    return create_map_naics(selected_sectors)

# Export the map_layout
map_layout = get_map_component()