import dash
from dash import html

dash.register_page(__name__, path="/visualization", name="Visualization")

def alternating_block(image_src, title, description, reverse=False):
    return html.Div(
        className="row mb-5 align-items-center",
        children=[
            html.Div(className="col-md-6", children=[
                html.Img(src=image_src, className="img-fluid rounded shadow", style={"width": "100%", "maxWidth": "600px"})
            ]) if not reverse else
            html.Div(className="col-md-6", children=[
                html.H4(title),
                html.P(description)
            ]),
            html.Div(className="col-md-6", children=[
		html.H4(title),
                html.P(description, className="lead")
            ]) if not reverse else
            html.Div(className="col-md-6", children=[
                html.Img(src=image_src, className="img-fluid rounded shadow", style={"width": "100%", "maxWidth": "600px"})
            ])
        ]
    )

layout = html.Div(
    className="container mt-4",
    children=[
        html.H1("Data Visualization", className="mb-4 text-center"),

        alternating_block(
            "/assets/D1.png",
            "1. Business Closure Trends Histogram",
            "Most businesses close within the first 4 years, highlighting a high early failure rate and a right-skewed distribution.",
            reverse=False
        ),

        alternating_block(
            "/assets/D2.png",
            "2. Closed Businesses by Sector in LOS ANGELES",
            "Retail Trade has the most closures, showing that consumer-facing sectors face the highest failure rates.",
            reverse=True
        ),

        alternating_block(
            "/assets/D3.png",
            "3. Mean vs. Median Business Lifespan by Sector (1980–2024)",
            "The mean lifespan is consistently higher than the median, indicating that outliers extend average longevity.",
            reverse=False
        ),

        alternating_block(
            "/assets/P1.png",
            "4. Distribution of Business Lifespan by Sector (2000–2024)",
            "Violin plots reveal that some industries like real estate have greater variation and longer business survival.",
            reverse=True
        ),

        alternating_block(
            "/assets/dv1.png",
            "5. Net Business Change Per Month in LA (2000–2024)",
            "Major dips align with economic events like the 2008 crisis and COVID-19, showing their business impact.",
            reverse=False
        ),

        alternating_block(
            "/assets/dv2.png",
            "6. Net Change Business by Month (All Years Combined)",
            "January consistently sees business peaks, while December experiences significant closures annually.",
            reverse=True
        )
    ]
)
