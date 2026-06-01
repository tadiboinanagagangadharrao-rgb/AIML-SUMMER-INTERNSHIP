import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------------------------
# 1. SETUP & DUMMY DATA CREATION
# -------------------------------------------------------------------------
# Set visual styles for cleaner plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Generating a fake dataset for demonstration purposes
np.random.seed(42)
n_samples = 100

data = {
    'Age': np.random.randint(18, 70, size=n_samples),
    'Income': np.random.normal(55000, 15000, size=n_samples).astype(int),
    'Spending_Score': np.random.randint(1, 100, size=n_samples),
    'Membership': np.random.choice(['Standard', 'Premium', 'VIP'], size=n_samples, p=[0.5, 0.3, 0.2]),
}

df = pd.DataFrame(data)

# Injecting some artificial missing values and an outlier for the EDA to catch
df.loc[5:8, 'Income'] = np.nan
df.loc[20, 'Income'] = 250000  # Outlier

# -------------------------------------------------------------------------
# 2. BASIC INSPECTION
# -------------------------------------------------------------------------
print("=== 1. FIRST 5 ROWS ===")
print(df.head(), "\n")

print("=== 2. DATASET INFO ===")
df.info()
print(f"\nDataset Shape: {df.shape}\n")

# -------------------------------------------------------------------------
# 3. DESCRIPTIVE STATISTICS
# -------------------------------------------------------------------------
print("=== 3. NUMERICAL SUMMARY ===")
print(df.describe(), "\n")

print("=== 4. CATEGORICAL SUMMARY ===")
print(df.describe(include=['object']), "\n")

# -------------------------------------------------------------------------
# 4. MISSING VALUES & DUPLICATES
# -------------------------------------------------------------------------
print("=== 5. MISSING VALUES PER COLUMN ===")
print(df.isnull().sum(), "\n")

print(f"=== 6. DUPLICATE ROWS COUNTS ===\nTotal duplicates: {df.duplicated().sum()}\n")

# -------------------------------------------------------------------------
# 5. VISUALIZATIONS (UNIVARIATE & BIVARIATE)
# -------------------------------------------------------------------------
print("...Generating Plots. Close each plot window to proceed to the next one...")

# Plot 1: Distribution of a Numerical Column (Income)
plt.figure()
sns.histplot(df['Income'].dropna(), kde=True, color='blue')
plt.title('Distribution of Income')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()

# Plot 2: Count plot for a Categorical Column (Membership)
plt.figure()
sns.countplot(data=df, x='Membership', order=df['Membership'].value_counts().index, palette='viridis')
plt.title('Distribution of Membership Types')
plt.xlabel('Membership Level')
plt.ylabel('Count')
plt.show()

# Plot 3: Boxplot to Detect Outliers (Income)
plt.figure()
sns.boxplot(x=df['Income'], color='orange')
plt.title('Box Plot for Income (Outlier Detection)')
plt.show()

# Plot 4: Correlation Heatmap
plt.figure()
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Plot 5: Scatter Plot with Category Hue (Age vs Income grouped by Membership)
plt.figure()
sns.scatterplot(data=df, x='Age', y='Income', hue='Membership', size='Spending_Score', sizes=(20, 200))
plt.title('Age vs Income (by Membership & Spending Score)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

print("=== EDA SCRIPT COMPLETED ===")