# DataAnalytics-carpriceanalysis

Project Objectives
*Clean and preprocess used car data for analysis.
*Identify strong predictors of car price.
*Visualize trends and correlations among variables.
*Engineer meaningful features to boost model performance.


#Technologies Used
 Python
 Pandas, NumPy for data handling
 Seaborn, Matplotlib for EDA & visualization
  
#Exploratory Data Analysis
- Null values assessed and handled systematically
- Strong correlations found:
  - `highwaympg` vs `citympg` (0.97)
  - `carlength`, `carwidth`, `curbweight` vs `wheelbase` (>0.79)
- Redundant variables dropped to avoid multicollinearity
- Features engineered:
  - `carCompany` extracted from `CarName`
  - `car_stability` derived and later dropped due to high correlation

 #Tools used: `pairplot`, `heatmap`, histograms, and bar charts.

#Data Preparation
Null Handling: Columns with high null % were dropped.

#Feature Engineering
Extracted `carCompany` and corrected spelling inconsistencies.
Created dummy variables for categorical columns.

#Dimensionality Reduction
Removed highly correlated features to prevent overfitting.



