import dash
from dash import html
from pages.app_geomap import map_layout


dash.register_page(__name__, 
                   path="/map", 
                   name="Analysis-Map Dashboard", 
                   order=3)

layout = html.Div(
    className="container mt-4",
	style={
        # 'backgroundColor': '#b9e1db',
        'backgroundColor': 'rgba(185, 225, 219, 0.5)',
        'padding': '50px',
        'minHeight': '100vh'
    },
    children=[
        html.H1("Business Map Dashboard"),
        # html.P("This interactive dashboard shows the geographic distribution of business across Los Angeles."),
        map_layout
    ]
)
