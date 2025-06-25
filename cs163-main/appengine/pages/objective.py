import dash
from dash import html

dash.register_page(__name__, path="/objective", name="Objective")

layout = html.Div(
    className="container mt-4",
    children=[
        html.H2("Project Summary", style={'color': 'black'}),
        html.P(
            "This project aims to develop a data-driven business advisory tool to help new business "
            "owners make informed decisions about starting and sustaining their ventures. Using large-scale "
            "datasets from Los Angeles city records, it will analyze trends in active and closed businesses, "
            "applying machine learning and statistical analysis to provide actionable insights. The final "
            "product will be an interactive web-based application where users can input key business details "
            "such as industry, location, and startup size. The system will then generate personalized "
            "recommendations, including estimated startup costs (covering labor, materials, and rent), the "
            "probability of business closure over one, three, and seven years, and strategic advice for "
            "sustainability.",
            className="lead",
            style={'color': '#333'}
        ),

        html.H2("Broader Impacts", style={'color': 'black', 'marginTop': '40px'}),
        html.P(
            "This project will provide valuable insights for multiple stakeholders, including new business owners, "
            "investors, policymakers, city planners, and economic researchers. New business owners will benefit "
            "from actionable insights that help them make informed decisions about selecting sustainable locations "
            "and industries. Investors and policymakers can use the findings to guide investment strategies and "
            "urban development initiatives by identifying areas of economic growth and market saturation. City "
            "planners will be able to assess which regions are oversaturated or underserved, allowing for targeted "
            "economic development and infrastructure planning. Additionally, economic researchers will find value "
            "in the analysis, as it contributes to studies on business survival trends and broader economic patterns, "
            "offering a data-driven perspective on the factors influencing business success and failure.",
            className="lead",
            style={'color': '#333'}
        )
    ]
)
