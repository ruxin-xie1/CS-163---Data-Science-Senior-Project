import dash
from dash import html

dash.register_page(__name__, path="/dataset", name="Dataset")

layout = html.Div(
    className="container mt-4",
    children=[
        html.H1("Datasets - Summarize the Dataset"),

        html.P([
            "The dataset, comprising ",
            html.Strong("1,593,026 rows"),
            " and ",
            html.Strong("16 columns"),
            ", focuses on analyzing business closures and trends by leveraging key variables: ",
            html.Strong("NAICS (Number)"),
            ", which categorizes businesses by industry type to identify industries with the highest closure rates; ",
            html.Strong("LOCATION START DATE (Floating Timestamp)"),
            ", indicating when a business began operations to determine its lifespan; ",
            html.Strong("LOCATION END DATE (Floating Timestamp)"),
            ", which identifies when a business ceased operations and serves as the primary target variable for closures; and ",
            html.Strong("LOCATION (Latitude & Longitude)"),
            ", providing geographic coordinates to visualize and analyze spatial trends in closures. These features enable a comprehensive examination of business closures over time, across industries, and by location."
        ]),

        html.H3("Handling Missing Data"),
        html.P([
            "Dropped missing data on column of: ", html.Strong("NAICS, LOCATION"), ". ",
            "Since the area of interest involves NAICS code and location start to end dates, we drop missing records, ",
            "leaving ", html.Strong("624,379 entries remaining"), ". ",
            "We may also drop the data missing coordinates on the location column, leaving ",
            html.Strong("584,508 entries remaining after dropping missing NAICS and LOCATION.")
        ]),

        html.H1("Statistics", style={"marginTop": "40px"}),
        html.P("Calculate measures like mean, median, standard deviation, and correlations:"),

        html.H3("1. Business Lifespan Statistics (Mean, Median, Standard Deviation) in LA"),
        html.P([
            "Business Lifespan Statistics (Mean, Median, Std Dev) show how long businesses last on average, "
            "the typical lifespan, and how much variation exists between businesses. "
            "The average business lifespan is 8.57 years, with a median of 5.96 years, meaning many businesses "
            "close within 6 years. The standard deviation of 8.66 years suggests high variability—some businesses "
            "last much longer while others fail quickly."
        ]),
        html.Img(src="/assets/S1.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"}),

        html.H3("2. Yearly Business Closure Count & 3-Year Moving Average Statistics in LA"),
        html.P([
            "Yearly Business Closure Trends provide insights into whether business closures are increasing or decreasing, "
            "and the 3-Year Moving Average helps smooth short-term fluctuations to highlight long-term trends. "
            "The Yearly Business Closures graph shows spikes in closures in certain years, possibly due to economic downturns "
            "or other external factors. The 3-Year Moving Average (blue line) reveals a smoother trend, showing overall "
            "increases and decreases in business closures over time."
        ]),
        html.Img(src="/assets/S2.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"})
    ]
)
