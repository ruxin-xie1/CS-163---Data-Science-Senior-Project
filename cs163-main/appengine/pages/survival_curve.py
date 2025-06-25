import dash
from dash import html
import dash_bootstrap_components as dbc
from pages.app_survivalplot import survival_plot


dash.register_page(__name__, 
                   path="/survival", 
                   name="Analysis-KM Survival Curve", 
                   order=4)
layout = html.Div(
    className="container mt-4",
    style={
        'backgroundColor': 'rgba(180, 167, 214, 0.5)',
        'padding': '50px',
        'minHeight': '100vh'
    },
    children=[
        html.H1("Kaplan-Meier Survival Curve Analysis"),
        html.P("This page visualizes business survival over time by industry using Kaplan-Meier survival curves."),
        
        
        # Formula as image (fallback)
        # html.H3("Kaplan-Meier Estimator Formula:"),
        # html.Img(
        #     src="https://latex.codecogs.com/svg.latex?S(t)%20%3D%20%5Cprod_%7Bi%3At_i%20%5Cleq%20t%7D%20%5Cleft(1%20-%20%5Cfrac%7Bd_i%7D%7Bn_i%7D%5Cright)",
        #     className="mx-auto d-block",
        #     style={'margin': '24px 0'},
        # ),
        # html.H6("Where:"),
        # html.Ul([
        #     html.Li("tᵢ = Time when at least one event occurred"),
        #     html.Li("dᵢ = Number of events (business closures)"),
        #     html.Li("nᵢ = Number of businesses at risk"),
        # ]),
        html.Details([
            html.Summary("Kaplan–Meier Estimator Formula:", style={"cursor": "pointer", "fontSize": "1.25rem"}),
            html.Div([
                html.Img(
                    src=(
                        "https://latex.codecogs.com/svg.latex?"
                        "S(t)%20%3D%20%5Cprod_%7Bi%3At_i%20%5Cleq%20t%7D"
                        "%20%5Cleft(1%20-%20%5Cfrac%7Bd_i%7D%7Bn_i%7D%5Cright)"
                    ),
                    className="mx-auto d-block",
                    style={'margin': '16px 0'}
                ),
                html.H6("Where:"),
                html.Ul([
                    html.Li("tᵢ = Time when at least one event occurred"),
                    html.Li("dᵢ = Number of events (business closures)"),
                    html.Li("nᵢ = Number of businesses at risk"),
                ]),
            ], style={"padding": "0 1rem"})
        ], open=False, style={"border": "1px solid #ddd", "borderRadius": "4px"}),

        # explanation
        html.H4("Purpose"),
        html.P("Visualize LA business survival by industry with Kaplan–Meier curves to pinpoint resilient sectors, expose systemic risks, and guide site selection, policy, and investment by revealing saturated and underserved markets."),
        html.Div(
            dbc.Row([

                # # instruction
                dbc.Col(
                    html.Div([
                        html.H5("Instructions"),
                        html.Ul([
                            html.Li([
                                "Click ", 
                                html.Strong("SELECT INDUSTRIES"),
                                "."
                            ]),
                            html.Li("Check one or more industries in the pop-up."),
                            html.Li([
                                "Adjust the ",
                                html.Strong("Max Duration"),
                                " slider (60–360 months) to focus on a specific timeframe."
                            ]),
                            html.Li([
                                "Adjust the ",
                                html.Strong("Probability Range"),
                                " slider to narrow the survival probability displayed."
                            ]),
                            html.Li([
                                "Click ",
                                html.Strong("APPLY"),
                                " to compare survival curves."
                            ]),
                        ]),
                    ])
                ),

                # # interpretation
                dbc.Col(
                    html.Div([
                        html.H5("How to Interpret Results"),
                        html.Ul([
                            html.Li([
                                html.Strong("Higher curves"),
                                " indicate industries with ",
                                html.Strong("resilient business models"),
                                ", ",
                                html.Strong("lower closure risks"),
                                ", and greater ",
                                html.Strong("investor appeal"),
                                "."
                            ]),
                            html.Li([
                                html.Strong("Lower curves"),
                                " signal ",
                                html.Strong("higher vulnerability"),
                                " due to ",
                                html.Strong("market saturation"),
                                ", or ",
                                html.Strong("operational challenges"),
                                # ", ",
                                # html.Strong("cyclical downturns"),
                                "."
                            ]),
                        ]),
                    ])
                ),
                
            ])
        ),

        # # from app_survivalplot.py
        survival_plot,


        html.Div([

            html.H5("Unique Observation"),
            html.Ul([
                html.Li([
                    html.Strong("Pattern:"),
                    " Sudden declines at 12, 24, 36 months suggest systemic pressures (e.g., lease renewals, annual compliance deadlines)", 
                ]),

                html.Li([
                    html.Strong("Implications:"),

                    html.Ul([
                        html.Li([
                            html.Strong("Businesses:"),
                            " Negotiate flexible leases; budget for annual fees.", 
                        ]),
                        html.Li([
                            html.Strong("Policymakers:"),
                            " Stagger compliance deadlines or offer grace periods.", 
                        ]),
                        html.Li([
                            html.Strong("Investors:"),
                            " Factor seasonal risks into portfolios."
                        ]),
                        html.Li([
                            html.Strong("Societal:"),
                            " Stabilize local economies by reducing synchronized closures."
                        ]),
                    ]),

                ]),  
            ]),
        ]),

        

    ],
)
