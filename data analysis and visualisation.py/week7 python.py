#task 1
import seaborn as sns
import pandas as pd

# Load the Iris dataset from seaborn
df = sns.load_dataset('iris')

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Explore the structure of the dataset (data types and missing values)
print("\nDataset structure and data types:")
print(df.info())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# If there are missing values (though the Iris dataset usually doesn't have missing values), fill or drop them
# For this dataset, we'll just ensure there are no missing values for completeness
df = df.dropna()  # Alternatively, you could use df.fillna() to fill missing values if needed

#task 2
import pandas as pd
import seaborn as sns

# Load the dataset
df = sns.load_dataset('iris')  # or pd.read_csv('path_to_your_file.csv')

# Check the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Basic statistics of the numerical columns
basic_stats = df.describe()

# Output the statistics
print("\nBasic Statistics:")
print(basic_stats)

# task 3
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset('iris')

# Line chart - showing the count of each species
df['species'].value_counts().plot(kind='bar')
plt.title('Species Count')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# Scatter plot - Sepal length vs Petal length
plt.scatter(df['sepal_length'], df['petal_length'])
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()
