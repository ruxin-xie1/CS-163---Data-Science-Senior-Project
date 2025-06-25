import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="Welcome")

layout = html.Div(
    style={
        'position': 'relative',
        'backgroundImage': 'url("/assets/w1.webp")',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center',
        'minHeight': '100vh',
        'padding': '50px',
        'color': 'white',
        'overflow': 'hidden'
    },
    children=[
        html.Div(style={
            'position': 'absolute',
            'top': 0,
            'left': 0,
            'width': '100%',
            'height': '100%',
            'backgroundColor': 'rgba(0,0,0,0.7)',
            'zIndex': 0
        }),

        dbc.Container([
            html.Div([
                html.H1("Welcome to Business Survival Analysis", style={
                    'textAlign': 'center', 'fontSize': '48px', 'marginBottom': '30px'}),
                html.P(
                    "Explore business trends, survival probabilities, and machine learning predictions "
                    "based on real business closure data in Los Angeles.",
                    style={'textAlign': 'center', 'fontSize': '24px', 'marginBottom': '40px'}
                ),
                html.Hr(style={'borderColor': 'white'}),
                html.Div([
                    html.H4("Our project helps entrepreneurs, investors, and policymakers by offering:"),
                    html.Ul([
                        html.Li("Insights into historical business trends", style={'fontSize': '20px'}),
                        html.Li("Data-driven survival rate estimations", style={'fontSize': '20px'}),
                        html.Li("Predictive tools for new businesses based on industry and location", style={'fontSize': '20px'}),
                    ])
                ], style={'maxWidth': '800px', 'margin': 'auto', 'marginTop': '40px'})
            ], style={'position': 'relative', 'zIndex': 1})
        ], fluid=True),

        html.Div(style={
            'position': 'relative',
            'zIndex': 1,
            'backgroundColor': '#fdfdfd',
            'color': '#222',
            'padding': '60px 40px'
        }, children=[
            html.H2("Some Interesting Findings", style={'textAlign': 'center', 'marginBottom': '40px'}),

            # Row 1
            dbc.Row([
                dbc.Col([
                    html.H4("1. Distribution of Business Lifespan by Sector"),
                    html.P("Some sectors show significant difference of lifespan: Agriculture and Real Estate have different distributions and outliers.")
                ], md=6),
                dbc.Col(html.Img(src="/assets/P1.png", style={'width': '100%'}), md=6)
            ], style={'marginBottom': '40px'}),

            # Row 2
            dbc.Row([
                dbc.Col(html.Img(src="/assets/dv1.png", style={'width': '100%'}), md=6),
                dbc.Col([
                    html.H4("2. Net Business Change Per Month in LA"),
                    html.P("Major drops during financial crises and pandemic periods. Earlier years were more stable.")
                ], md=6)
            ], style={'marginBottom': '40px'}),

            # Row 3
            dbc.Row([
                dbc.Col([
                    html.H4("3. Net Change Business by Month"),
                    html.P("Seasonal trends show gains in January and steep declines in December.")
                ], md=6),
                dbc.Col(html.Img(src="/assets/dv2.png", style={'width': '100%'}), md=6)
            ])
        ])
    ]
)
