
# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # convert to pandas DataFrame
    df['species'] = iris.target_names[iris.target]  # add species column
    
    print("✅ Dataset loaded successfully!\n")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Check dataset structure
print("Dataset info:")
print(df.info(), "\n")

# Check for missing values
print("Missing values in dataset:")
print(df.isnull().sum(), "\n")

# Clean dataset (if missing values exist, fill with mean)
df = df.fillna(df.mean(numeric_only=True))

# Task 2: Basic Data Analysis

# Basic statistics
print("Basic statistics:")
print(df.describe(), "\n")

# Group by species and compute mean of numerical columns
grouped = df.groupby("species").mean()
print("Mean values grouped by species:")
print(grouped, "\n")

# Interesting finding
print("Observation: Iris-setosa has the smallest average petal length, while Iris-virginica has the largest.\n")


# Task 3: Data Visualization

# 1. Line chart (showing petal length trend across samples)
plt.figure(figsize=(8,5))
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title("Line Chart: Petal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="Set2")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
plt.figure(figsize=(8,5))
plt.hist(df['sepal length (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram: Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs. petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# Findings

print("""
Findings:
1. Iris-setosa has shorter petals compared to the other species.
2. Iris-virginica has the largest petal lengths and widths overall.
3. Sepal length is positively correlated with petal length.
4. The histogram shows that most sepal lengths fall between 5 and 6.5 cm.
""")