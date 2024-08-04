# Strategic_Aid_Allocation
Repo containing files for Clustering model "Help Organization Strategic Aid Allocation"
**Problem Statement**
HELP International is an international humanitarian NGO dedicated to fighting poverty and providing essential services and relief during disasters and natural calamities. The organization has raised $10 million to allocate strategically to countries in dire need. The goal is to identify and prioritize these countries using socio-economic and health factors that determine overall development and need for aid.

The specific objectives of this project include:

Strategic Resource Allocation: Maximizing the impact of available funds by identifying countries that require immediate assistance due to economic instability, high child mortality rates, low life expectancy, and other socio-economic challenges.

Data-Driven Decision Making: Utilizing data science techniques to provide objective and precise insights into countries' needs, ensuring resources are directed where they can make the most significant impact.

Targeted Interventions: Tailoring aid efforts to address specific challenges faced by different regions, enhancing the effectiveness and efficiency of aid delivery.

The goal is to categorize countries into different clusters based on their socio-economic and health profiles, enabling HELP International to prioritize aid allocation to those most in need.

**Steps Taken to Solve the Problem
**1. Exploratory Data Analysis (EDA)****
The exploratory data analysis phase involved understanding the dataset's structure, distribution, and relationships between variables. The following steps were conducted:

Univariate Analysis
Histogram and Box Plots: Visualized the distribution of each variable to understand the skewness, spread, and potential outliers. This helped identify variables that required transformation or treatment for outliers.

Outlier Analysis: Identified outliers using box plots and histograms. However, removing outliers was deemed inappropriate because outliers could represent significant economic events or crises affecting a country's socio-economic condition during a particular year.

**Winsorization**: Instead of removing outliers, winsorization was applied to cap extreme values. This approach retained the data's integrity while reducing the impact of extreme values.

**Bivariate Analysis**
Correlation Matrix: Analyzed the pairwise correlations between variables to identify significant relationships. Strong correlations were found between variables such as exports and imports, total fertility rate and life expectancy, and more.

**2. Hypothesis Testing**
Hypothesis testing was conducted to validate relationships between key socio-economic variables. Here are the detailed hypothesis tests performed:

1. Hypothesis Testing: Increased Health Spending Leads to Higher Life Expectancy
Hypothesis: Countries with higher health spending (% of GDP) have higher life expectancy.

Method: Conducted a t-test comparing life expectancy between high and low health-spending countries.


2. Hypothesis Testing: Correlation Between Total Fertility and Income
Hypothesis: There is a significant correlation between total fertility rates and income levels.

Method: Performed Pearson correlation analysis and a t-test on income levels between high and low fertility countries.

3. Hypothesis Testing: Income Levels and Child Mortality
Hypothesis: Higher income levels are associated with lower child mortality rates.

Method: Analyzed the correlation between income and child mortality rates.

4. Hypothesis Testing: Inflation and GDP per Capita
Hypothesis: Higher inflation rates are associated with lower GDP per capita, indicating economic instability.

Method: Conducted correlation analysis and t-tests between inflation rates and GDP per capita.


**3. Machine Learning Modeling**
The primary objective was to cluster countries based on socio-economic and health indicators to prioritize aid allocation. The following steps were taken:

Feature Engineering
New Features: Created features such as the child well-being index, real income, life expectancy improvement potential, economic dependence ratio, and more.

Binary Encoding: Applied binary encoding to the 'Country' feature to avoid the curse of dimensionality and preserve uniqueness without introducing ordinal relationships.

Dimensionality Reduction with PCA
Principal Component Analysis (PCA): Reduced the dataset to 14 features from 26 to retain maximum explained variance. This step helped in visualizing clusters and improved model performance.
Clustering with K-Means
Elbow Method: Used the Elbow method to determine the optimal number of clusters, resulting in three clusters.

Model Training: Applied the K-Means algorithm to segment countries into three clusters, each representing different aid priorities.

Silhouette Score: The target metric for evaluating clustering performance was the silhouette score. A silhouette score of 0.18 was achieved, indicating the model's effectiveness in clustering countries based on socio-economic indicators.

**4. Deployment**
The deployment phase involved creating an API using Flask to allow stakeholders to interact with the model and obtain predictions:

Steps for Deployment
Flask API Configuration: Developed a Python script (app.py) with Flask configurations, incorporating all transformations performed during data preprocessing and feature engineering.

Pickle Files: Saved the trained model, scalers, and PCA components as pickle files to ensure consistent transformations and predictions for new data points.

API Endpoints: Created endpoints to accept country data and return the predicted cluster, indicating the priority for aid allocation.

Mapping and Consistency: Ensured that all encoding, scaling, and PCA transformations applied in the Jupyter notebook were replicated in the Flask application, maintaining consistency between development and production environments.

**Why This Approach Was Chosen**
This approach was chosen due to its ability to provide a systematic, data-driven method for identifying countries in dire need of aid. By leveraging socio-economic and health data, the model can effectively cluster countries into priority groups, allowing HELP International to allocate resources where they can make the most significant impact.

Comprehensive Analysis: The combination of EDA, hypothesis testing, and feature engineering provided a thorough understanding of the data and relationships between key indicators.

Robust Clustering: K-Means clustering, combined with PCA for dimensionality reduction
