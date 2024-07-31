import numpy as np
import pandas as pd
from scipy import stats

# Load the CSV file into a DataFrame
df = pd.read_csv("C:/Users/shiro/Downloads/01.Data Cleaning and Preprocessing.csv")

# Display information about the DataFrame
print(df.info())

# Display the type of the DataFrame
print(type(df))

# Display the first few rows of the DataFrame
print(df.head())

# Display the last few rows of the DataFrame
print(df.tail())

# Display summary statistics of the DataFrame
print(df.describe())

# Display the shape of the DataFrame
print(df.shape)

# Display null values in the DataFrame
print(df.isnull())

# Sum of null values for each column
print(df.isnull().sum())

# Total number of null values
print(df.isnull().sum().sum())

# Display not null values in the DataFrame
print(df.notnull())

# Drop rows with any null values
df_cleaned = df.dropna()
print(df_cleaned.head())

# Fill null values with 0
df_filled = df.fillna(value=0)
print(df_filled.head())

# Fill null values with the previous value (forward fill)
df_ffill = df.fillna(method="ffill")
print(df_ffill.head())

# Fill null values with the next value (backward fill)
df_bfill = df.fillna(method="bfill")
print(df_bfill.head())

# Display the column names
print(df.columns)

# Drop duplicate rows
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates.head())

# Filter data where 'BlowFlow' column values are greater than 16
filtered_data = df[df["BlowFlow"] > 16]
print(filtered_data.head())

# Sort data by 'ChipRate' column in ascending order
sorted_data = df.sort_values(by='ChipRate', ascending=True)
print(sorted_data.head())

# Group data by 'ChipMass-4 ' column and sum the values
grouped_data = df.groupby('ChipMass-4 ').sum()
print(grouped_data.head())


