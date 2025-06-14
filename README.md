This project performs a comprehensive exploratory data analysis (EDA) on a car pricing dataset to uncover key insights and factors that influence car prices. The analysis includes data cleaning, feature engineering, visualization, and correlation studies to aid in understanding pricing trends in the automobile industry.

#Features of the Project

Handles missing data with thresholds for rows and columns
Extracts and cleans brand names from car names
Fixes typos in categorical data
Creates dummy variables for categorical features
Engineers new feature car_stability
Removes multicollinearity by dropping highly correlated features
Visualizes distributions, pairwise relationships,  and correlations

#Technologies Used :
Python,Pandas,NumPy,Seaborn,Matplotlib

#Dataset
The dataset used is CarPriceData.csv, which contains specifications of various car models and their prices.

#Data Preprocessing
Null value analysis and handling:
Dropped columns with >40% missing data
Removed rows with >50% missing values
Removed irrelevant or redundant columns (car_ID, CarName)
Created carCompany by splitting CarName and corrected misspellings
One-hot encoding for categorical variables

#Feature Engineering
car_stability: Derived as wheelbase / carlength to assess vehicle balance
Removed highly correlated features to reduce noise and multicollinearity

#Visualizations
Pairplots for initial inspection of relationships between key numeric features and price
Heatmap to show the top 10 most correlated features with price
Histograms for understanding the distribution of all numerical variables



