import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------------------------
# 1. SET UP STYLE & DATA
# -------------------------------------------------------------------------
# Seaborn comes with built-in themes. 'darkgrid' or 'whitegrid' are favorites.
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Let's create a realistic dataset using Pandas
np.random.seed(42)
days = pd.date_range(start="2026-01-01", periods=100)

# Simulate e-commerce data across two different regions
data_region_A = pd.DataFrame({
    'Date': days,
    'Sales': np.convolve(np.random.normal(500, 50, 100), np.ones(5)/5, mode='same'), # Smooth trend
    'Profit': np.random.randint(10, 100, size=100),
    'Region': 'North Region',
    'Customer_Segment': np.random.choice(['Retail', 'Corporate'], size=100)
})

data_region_B = pd.DataFrame({
    'Date': days,
    'Sales': np.convolve(np.random.normal(400, 45, 100), np.ones(5)/5, mode='same'),
    'Profit': np.random.randint(5, 80, size=100),
    'Region': 'South Region',
    'Customer_Segment': np.random.choice(['Retail', 'Corporate'], size=100)
})

# Combine into a single tidy DataFrame (the format Seaborn loves best)
df = pd.concat([data_region_A, data_region_B], ignore_index=True)

# -------------------------------------------------------------------------
# 2. LINE CHART (With Automatic Faceting/Grouping)
# -------------------------------------------------------------------------
plt.figure()
# Seaborn automatically splits lines and creates legends based on the 'hue' parameter
sns.lineplot(data=df, x='Date', y='Sales', hue='Region', linewidth=2.5)

plt.title('Sales Trends Over Time by Region', fontsize=14, fontweight='bold')
plt.xlabel('Timeline')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------
# 3. VIOLIN PLOT (Showing Data Distribution & Density)
# -------------------------------------------------------------------------
plt.figure()
# 'split=True' lets you directly compare two subgroups side-by-side within one violin
sns.violinplot(data=df, x='Region', y='Profit', hue='Customer_Segment', 
               split=True, inner="quart", palette="muted")

plt.title('Profit Distribution: Region vs Customer Segment', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Profit ($)')
plt.show()

# -------------------------------------------------------------------------
# 4. MATRIX / HEATMAP (Visualizing Correlations)
# -------------------------------------------------------------------------
plt.figure(figsize=(6, 5))

# Generate a small correlation matrix from numerical data
numerical_cols = df[['Sales', 'Profit']]
# Adding an artificial third variable to make the heatmap interesting
numerical_cols = numerical_cols.assign(Discount=np.random.uniform(0.05, 0.3, size=len(numerical_cols)))
corr_matrix = numerical_cols.corr()

# 'annot=True' prints the values inside the squares, 'cmap' changes the color gradient
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt=".2f", square=True, linewidths=.5)

plt.title('Correlation Matrix Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------
# 5. BONUS: THE PAIRPLOT (The Ultimate EDA Visualization)
# -------------------------------------------------------------------------
# One line of Seaborn code creates a grid of pairwise relationships across the dataset
print("Generating Pairplot... (This might take a quick second)")
sns.pairplot(df, hue='Region', palette='husl', corner=True)
plt.show()