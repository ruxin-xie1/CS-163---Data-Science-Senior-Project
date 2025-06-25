import dash
from dash import html

dash.register_page(__name__, path="/about", name="About")

layout = html.Div(
    children=[
        html.Section(
            id="contact",
            className="contact-section bg-black",
            children=html.Div(
                className="container",
                children=html.Div(
                    className="row justify-content-center",
                    children=[
                        html.Div(
                            className="col-md-8 mb-3 mb-md-0",
                            children=html.Div(
                                className="card py-4 h-100",
                                children=html.Div(
                                    className="card-body text-center",
                                    children=[
                                        html.I(className="fas fa-map-marked-alt text-primary mb-2"),
                                        html.H4("E-mail Address", className="text-uppercase m-0", style={"color": "black"}),
                                        html.H6("Ruxin Xie: ruxin.xie01@sjsu.edu", className="m-0", style={"color": "black"}),
                                        html.H6("Eric Zhao: eric.zhao@sjsu.edu", className="m-0", style={"color": "black"})
                                    ]
                                )
                            )
                        )
                    ]
                )
            )
        ),
        html.Footer(
            className="bg-black small text-center text-white-50 mt-5",
            children=html.Div(
                className="container",
                children="SJSU CS163"
            )
        )
    ]
)
