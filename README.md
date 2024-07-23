# Data Analysis of the Sold Houses Los Angeles 2024 From Zillow

This is our final project of the Data Science Course at University of Tehran in spring 2024. In this project, we took all the steps of a data science project from data collection to data visualization and modeling.

## [Phase 0: Choosing the Subject and Dataset](./Phase0/)

In this phase, we decided to work on the data of sold houses in Los Angeles in 2024. We decided that we collect the data by ourselves from [Zillow](https://www.zillow.com/) which is a real estate and rental marketplace.

## [Phase 1: Data Collection and Analysis](./Phase1/)

This phase consists of the following steps:

### 1. Collecting the data from Zillow

Data scraping was done in two steps:
1. First, we scraped the links of the houses that were sold in Los Angeles in 2024.
2. Then, we scraped the data of each house from the links we collected in the first step.

We used `Selenium`, `requests` and `BeautifulSoup` libraries in Python for scraping the data.

### 2. Preprocessing and cleaning the data

In this step, We checked the data for missing values and outliers and used different methods to handle them.

### 3. Visualizing The Distribution of the Data

We visualized the distribution of all numerical features in the dataset and using this insight we removed some outliers and did some feature engineering.

### 4. Analyzing the Top 10s

We found the top 10 and bottom 10 of some features in the dataset and found more insights about the data.

### 5. Correlation Analysis

We calculated the correlation between the features and visualized it using a heatmap which helped us to find the relationships between the features.

### 6. Statistical Tests

We did some statistical tests to check whether some assumptions about the data are true or not. We used the `t-test` and `chi-square test` for this purpose.

## [Phase 2: Modeling](./Phase2/)

In this phase, we used the data to build a model that can predict the price of a house based on its features.

This phase consists of the following steps:

### 1. Preprocessing the Data 

In this step, we prepared the data for modeling. We converted the categorical features to numerical using different methods and also we scaled the data.

### 2. Dimensionality Reduction

We used PCA to reduce the dimension of the data so that we also test how well the model performs on the reduced data.

### 3. Choosing the Metrics

In this step, we searched about the most appropriate metrics for this task and in the end we chose various metrics but the most important one was `MAPE` which stands for Median Absolute Percentage Error.

### 4. Training the Models

We used different Machine Learning models to predict the price of the houses. We used `Linear Regression`, `Decision Tree Regressor`, `SVR`, `KNN` and we also used `Neural Networks` for this task. In the end we compared the models based on the metrics we chose in the previous step.

### 5. Conclusion

In the end, we concluded that the best model for this task was `SVR` and `Neural Networks`. Using `SVR` we reached 9% `MAPE`. and we also checked the importance of the features in predicting the price of the houses.

## [Data](./data/)

This directory contains all variations of the data that we collected and used in this project.

