import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline

df = pd.read_csv("CarPriceData.csv",header=0)
df.head()

df.info()
df.describe()
df.isnull().sum()

#Null count and percentage

null_counts = df.isnull().sum()

null_percent = (null_counts / len(df)) * 100

print(pd.concat([null_counts, null_percent], axis=1, keys=['Null Count', 'Percentage']))


#Drop columns with high null %

threshold = 40  # Drop if more than 40% null

df = df.loc[:, (null_percent < threshold)]


#Drop rows with too many NaNs (e.g., > 50% missing)

row_null_percent = (df.isnull().sum(axis=1) / df.shape[1]) * 100

df = df.loc[row_null_percent < 50]


#Drop unwanted columns

df.drop(['car_ID'], axis=1, inplace=True)

#Split CarName

df['carCompany'] = df['CarName'].apply(lambda x: x.split(' ')[0].lower())

df.drop(['CarName'], axis=1, inplace=True)



# Fix spelling issues in carCompany

df['carCompany'] = df['carCompany'].replace({

    'vw': 'volkswagen', 'vokswagen': 'volkswagen', 'maxda': 'mazda',

    'porcshce': 'porsche', 'toyouta': 'toyota', 'nissan':'nissan', 'Nissan':'nissan'

})



# Create dummy variables

df = pd.get_dummies(df, drop_first=True)



#Create derived feature - car_stability

df['car_stability'] = df['wheelbase'] / df['carlength']



#Drop highly correlated variables

df.drop(['carwidth', 'curbweight', 'carlength', 'wheelbase', 'highwaympg', 'car_stability'], axis=1, inplace=True)

#Visualization

# Pairplot and heatmap

sns.pairplot(df[['price', 'enginesize', 'horsepower', 'citympg']])

plt.show()

# Calculate correlation matrix
corr_matrix = df.corr()

# Get top 10 features most correlated with 'price' (excluding 'price' itself)
top_corr = corr_matrix['price'].abs().sort_values(ascending=False)[1:11]
top_features = top_corr.index.tolist()

# Create a focused correlation matrix
focused_corr = df[top_features + ['price']].corr()

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(
focused_corr,
annot=True,
fmt=".2f",
cmap='coolwarm',
vmin=-1,
vmax=1,
square=True,
linewidths=0.5,
cbar_kws={"shrink": 0.8}
)

plt.title("Top 10 Features Most Correlated with Car Price", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

#Histograms and Bar Charts

df.hist(bins=20, figsize=(20, 15))

plt.tight_layout()

plt.show()



#Final Insights Placeholder

# You can use describe(), groupby(), or visual analysis to derive business insights

print(df.describe())   
