<a name="readme-top"></a>

<!-- PROJECT TITLE / LOGO -->
<div align="center">
  <!-- Optional logo -->
  <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
    <!-- 🚀 -->
  <!-- <h3 align="center">Business Trends <br> & Market Analysis <br>in Los Angeles</h3> -->



  <h3 align="center">
    <b>Business Trends</b><br> 
    & <b>Market Analysis</b><br>
    in <b>Los Angeles</b>
  </h3>

  <p align="center">
    End-to-end analytics &amp; interactive Dash site for exploring the survival patterns of Los Angeles businesses
    <br />
    <a href="https://github.com/EricSJSU-DataScience/CS163_project"><strong>Explore the repo</strong></a>
    <!-- 
    ·
    <a href="about:blank">Report Bug</a>
    ·
    <a href="about:blank">Request Feature</a> 
    -->
  </p>
</div>

---

<details>
<summary><strong>Table of Contents</strong></summary>

1. [About the Project](#-about-the-project) 
2. [Pipline Overview](#-pipline-overview)
3. [Directory Information](#-directory-information) 
4. [Initial Data Exploration](#-initial-data-exploration) 
5. [Visualization of Business Location](#-visualization-of-business-location) 
6. [Survival Analysis & Graph](#-survival-analysis--graph) 
7. [Machine Learning-Based Data Interpretation](#-machine-learning-based-data-interpretation) 
    - [LSTM Model](#-lstm-model) 
    - [Random Survival Forest Model](#-random-survival-forest-model) 
8. [Environment & Setup](#-environment--setup) 
9. [Website](#-website) 
10. [Contact](#-contact)


</details>




---


## 📑 About the Project

This repository provides data-driven insights into business survival trends in Los Angeles, leveraging municipal government data to estimate closure risks by factor such as industry and location. The project includes a Dash web app for interactive exploration, enabling users to query survival probabilities for specific business types and zoomable map to show same business types in the neighborhoods for location selection.




<p align="right">(<a href="#readme-top">back to top</a>)</p>

---


## 📁 Directory Information

```
.
├── app_multi_page_styled/            # try build w/ custom Bootstrap theme
├── app_single_page_styled/           # Bootstrap theme but single-page Dash
├── appengine/                        # Final version multi-page Dash, deploy to gcloud
├── dataset/                          # Raw & processed data assets (tracked via Git LFS)
├── pic/                              # picture graph plot 
│
├── .gitattributes                    # Track large CSV with Git LFS
├── README.md                         # Project overview, setup & pipeline guide
│
├── dataset_business_city_list.ipynb               # City info in map
├── dataset_business_naics_code.ipynb              # NAICS info for industry in map
├── dataset_business_zipcode_list.ipynb            # Zip info for map
├── dataset_la_business.ipynb                      # Initial data cleaning & feature eng.
├── dataset_la_business_EDA.ipynb                  # Exploratory data analysis
├── dataset_la_business_map.ipynb                  # Geographic map
├── dataset_la_business_ml.ipynb                   # Machine learning LSTM & RSF
├── dataset_la_business_preview.ipynb              # Dataset Preview
├── dataset_la_business_rox.ipynb                  # Ruxin original analysis
├── dataset_la_business_visualization.ipynb        # Survival Analysis
│
└── requirements.txt                 # Python dependencies for notebooks & app

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- data analysis pipline & approach to analyzing idea -->
## 🔃 Pipline Overview

1. Data Collection:
    - Active and closed business records from [Los Angeles Open Data Portal](https://data.lacity.org/Administration-Finance/Listing-of-All-Businesses/r4uk-afju/about_data)
    - [NAICS codes for industry classification](https://www.naics.com/search/#naics) (`dataset_business_naics_code.ipynb`)
    - [City information](https://en.wikipedia.org/wiki/List_of_cities_in_Los_Angeles_County,_California) (`dataset_business_city_list.ipynb`)
    - [Zip code information](https://www.laalmanac.com/communications/cm02_communities.php) (`dataset_business_zipcode_list.ipynb`)

2. Data Preview (`dataset_la_business_preview.ipynb`):
    - inspect missing value
    - parse columns correct data type
    - append info between data source
    - inspect data/record correction

3. Data Cleaning & Filtering

4. Exploratory Analysis:
    - Survival curves (`dataset_la_business_visulization.ipynb`)
    - Geographic map (`dataset_la_business_map.ipynb`)

5. Machine Learning (`dataset_la_business_ml.ipynb`):
    - LSTM for time-series forecasting
    - Random Survival Forests for risk prediction

6. Dashboard Development (`appengine/`):
    - Build interactive visualizations with Plotly/Dash.
    - Deploy on Google App Engine



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- dataset preview & filter -->
## 🔍 Initial Data Exploration

The initial exploration (dataset_la_business_preview.ipynb) assessed raw data quality, focusing on identifying missing values, correcting data types (timestamps, categorical fields), and merging NAICS codes, city, and zip-code data. Exploratory checks ensured data consistency and completeness, preparing the dataset for further cleaning and analysis.

The dataset includes 1.5 millions Los Angeles business records with 16 features, covering identifiers, locations, NAICS codes, and operational periods. Key findings include:

- Temporal Trends: Rapid growth since 1990.

- Data Quality Issues: High missingness in  columns (DBA NAME, MAILING ADDRESS, ignore columns information).

- Date Processing: parsed LOCATION START DATE ; 990k records have end dates.

- Data Append: NAICS codes mapped to industry titles.

Data cleaning removed two third of records lacking essential information (NAICS codes or start dates), resulting in approx 600k usable records for later analytical process.



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- visualization geomap -->
## 🗺️ Visualization of Business Location

Geographic visualization (dataset_la_business_map.ipynb) employed Folium to plot business locations across Los Angeles County based on latitude and longitude, offering an interactive overview of active and closed businesses. Key geospatial insights include:

- Density Hotspots: based on different industry code, map show area businesses density

- City List: additional city list information did **not** append to business dataset well.

- Zip Code: additional zip code list information did **not** append to business dataset well.

- Fitler dataset decision: based on the coordinate range to filter records outside LA area.

Data filtering optimized visualization by focusing on valid geographic coordinates, utilizing the efficient FastMarkerCluster() instead of the slower MarkerCluster(). The interactive maps intuitively inform entrepreneurs and policymakers about strategic business locations and economic trends.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- survial analysis & kaplan-meier curve -->
## 📉 Survival Analysis & Graph

- [Survival Analysis](https://datatab.net/tutorial/survival-analysis)
- [Kaplan Meier Curve](https://datatab.net/tutorial/kaplan-meier-curve)

Survival analysis (dataset_la_business_visualization.ipynb) employed Kaplan-Meier methods to examine business longevity across industries. Survival curves illustrated sector-specific probabilities of businesses remaining operational over time, highlighting notable annual drops in survival rates. Although log-rank tests were applied, their outcomes were less intuitive visually.



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---


<!-- Machine Learning -->
## 📊 Machine Learning-Based Data Interpretation

LSTM was selected primarily driven by its capability to handle sequential data, essential for capturing fluctuations in total number of actived businesses across periods.

Random Survival Forest (RSF) model was selected due to its decision tree, a variance of Random Forest model. The dataset could use start-year, month, NAICS, and district info to feed this model and predict a new business opening in the future.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- Long Short Term Memory -->
### LSTM Model

Long Short-Term Memory (LSTM) model was employed due to its effectiveness in modeling temporal sequences inherent in business data. The dataset, aggregated monthly, allowed the LSTM model to learn and predict business dynamics over time by recognizing sequential dependencies and temporal patterns. 



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- Random Survival Forest -->
### Random Survival Forest Model

A Random Survival Forest (RSF) models business time‑to‑closure while naturally handling censored, still‑open cases. Trained on start year/month, council district, and 2‑digit NAICS sector for ~500 k cleaned records.



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚙️ Environment & Setup

This project is built in Python 3.10, using two main components: Jupyter notebooks (`.ipynb`) for analysis and a Dash/Flask web application (`.py`) to display results. The codebase has minimal dependencies, all listed in `requirements.txt` (Dash, Plotly, pandas, Flask, gunicorn, etc.).

To get started locally, create a new virtual or conda environment and run `pip install -r requirements.txt`. This installs the exact stack required by the notebooks and the WSGI server for the web app. Running `python app.py` launches a local Dash server, enabling real-time iteration on notebooks with immediate updates to the frontend.

For website, the code runs on Google App Engine. The `app.yaml` configuration file sets the runtime to Python 3.10, uses an F2 instance class (memory usage more than 256MB, F1 doesn't work). Deploy updates with termianl command `gcloud app deploy`. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🌐 Website

[Eric's link](https://my-project-cs122-20241114.uw.r.appspot.com/)

[Ruxin's link](https://cs163b.uw.r.appspot.com/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ℹ️ Contact

[Eric's LindedIn](https://www.linkedin.com/in/eric-zhao-data-scientist/)

[Ruxin's LinkedIn](https://www.linkedin.com/in/ruxin-xie-1a76232b3/)



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---


