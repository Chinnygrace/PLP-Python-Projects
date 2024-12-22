import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load the dataset
try:
    df = pd.read_csv('dataset.csv')
    print("Dataset loaded successfully.")
    print("First 5 rows of the dataset:")
    print(df.head())
except FileNotFoundError:
    print("Error: CSV file not found. Please ensure the file is in the same folder as this script.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Show data types
print("\nData Types:")
print(df.dtypes)

# Show missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Option 1: Drop rows with missing values
# df_cleaned = df.dropna()

# Option 2: Fill missing values with the mean for numerical columns
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())

# Drop rows where non-numerical columns still have missing values
df_cleaned = df.dropna()

print("\nAfter Cleaning:")
print(df_cleaned.isnull().sum())

# Task 2: Basic statistics
print("\nBasic Statistics:")
print(df_cleaned.describe())

# Group by USERID and compute the mean of AMOUNTINFO
grouped_data = df_cleaned.groupby('USERID')['AMOUNTINFO'].mean()

# Display the group-wise mean
print("\nGroup-wise Mean (USERID vs AMOUNTINFO):")
print(grouped_data)

# Insights or Patterns
print("\nObservations:")
print("The smallest transaction amount is 0.50, while the largest is 30,999.")
print("This range suggests the presence of outliers or extreme values.")


# Task 3

# Load the dataset
df = pd.read_csv('dataset.csv')

# Handle missing values (if not already done)
df['AMOUNTINFO'] = df['AMOUNTINFO'].fillna(df['AMOUNTINFO'].mean())

# Convert ORDERDATE to datetime for time-series analysis
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# 1. Line Chart: Trends Over Time
plt.figure(figsize=(10, 6))
df_grouped_by_date = df.groupby('ORDERDATE')['AMOUNTINFO'].sum()
plt.plot(df_grouped_by_date.index, df_grouped_by_date.values, marker='o', color='blue')
plt.title('Transaction Amount Trend Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Transaction Amount', fontsize=12)
plt.grid()
plt.show()

# 2. Bar Chart: Average Amount Per USERID
plt.figure(figsize=(12, 6))
df_grouped_by_user = df.groupby('USERID')['AMOUNTINFO'].mean().head(10)  # Top 10 users for clarity
sns.barplot(x=df_grouped_by_user.index, y=df_grouped_by_user.values, palette='viridis')
plt.title('Average Transaction Amount by Top 10 USERIDs', fontsize=16)
plt.xlabel('USERID', fontsize=12)
plt.ylabel('Average Transaction Amount', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# 3. Histogram: Distribution of Transaction Amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['AMOUNTINFO'], bins=30, kde=True, color='purple')
plt.title('Distribution of Transaction Amounts', fontsize=16)
plt.xlabel('Transaction Amount', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

# 4. Scatter Plot: Relationship Between USERID and AMOUNTINFO
plt.figure(figsize=(10, 6))
sns.scatterplot(x='USERID', y='AMOUNTINFO', data=df, alpha=0.5, edgecolor=None)
plt.title('Scatter Plot: USERID vs Transaction Amount', fontsize=16)
plt.xlabel('USERID', fontsize=12)
plt.ylabel('Transaction Amount', fontsize=12)
plt.show()
