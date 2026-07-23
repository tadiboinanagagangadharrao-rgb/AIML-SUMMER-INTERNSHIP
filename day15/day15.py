import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# -------------------------------------------------------------------
# 1. GENERATE SYNTHETIC DATASET
# -------------------------------------------------------------------
np.random.seed(42)  # For reproducibility

n = 100
df = pd.DataFrame({
    'Group': np.random.choice(['A', 'B'], size=n),
    'Age': np.random.randint(22, 60, size=n),
    'Score_Pre': np.random.normal(loc=70, scale=10, size=n),
    # Group B gets a slight bump in post-scores to simulate an effect
    'Score_Post': np.random.normal(loc=72, scale=12, size=n)
})
df.loc[df['Group'] == 'B', 'Score_Post'] += 5

print("=== SAMPLE DATASET ===")
print(df.head(), "\n")

# -------------------------------------------------------------------
# 2. DESCRIPTIVE STATISTICS
# -------------------------------------------------------------------
print("--- Measures of Central Tendency & Dispersion ---")
age_mean = df['Age'].mean()
age_median = df['Age'].median()
age_std = df['Age'].std()
age_iqr = stats.iqr(df['Age'])

print(f"Mean Age:         {age_mean:.2f}")
print(f"Median Age:       {age_median:.2f}")
print(f"Std Deviation:    {age_std:.2f}")
print(f"Interquartile Range (IQR): {age_iqr:.2f}\n")

print("--- Summary by Group ---")
group_summary = df.groupby('Group')[['Score_Pre', 'Score_Post']].agg(['mean', 'std', 'median'])
print(group_summary, "\n")

# -------------------------------------------------------------------
# 3. NORMALITY TESTING (Shapiro-Wilk Test)
# -------------------------------------------------------------------
# Null Hypothesis (H0): Data is normally distributed
print("--- Normality Check (Score_Post) ---")
stat, p_val = stats.shapiro(df['Score_Post'])
print(f"Shapiro-Wilk W-statistic: {stat:.4f}, p-value: {p_val:.4f}")
if p_val > 0.05:
    print("Result: Data appears to be normally distributed (Fail to reject H0)\n")
else:
    print("Result: Data deviates significantly from normal distribution (Reject H0)\n")

# -------------------------------------------------------------------
# 4. HYPOTHESIS TESTING (Two-Sample Independent t-test)
# -------------------------------------------------------------------
# Testing if Group A and Group B have significantly different Score_Post averages
# Null Hypothesis (H0): Mean(Group A) == Mean(Group B)
group_a_scores = df[df['Group'] == 'A']['Score_Post']
group_b_scores = df[df['Group'] == 'B']['Score_Post']

t_stat, p_value_ttest = stats.ttest_ind(group_a_scores, group_b_scores)

print("--- Independent Two-Sample t-Test (Group A vs Group B) ---")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value:     {p_value_ttest:.4f}")

if p_value_ttest < 0.05:
    print("Result: Statistically significant difference between groups (Reject H0)\n")
else:
    print("Result: No statistically significant difference detected (Fail to reject H0)\n")

# -------------------------------------------------------------------
# 5. CORRELATION ANALYSIS (Pearson vs Spearman)
# -------------------------------------------------------------------
pearson_corr, p_pearson = stats.pearsonr(df['Score_Pre'], df['Score_Post'])
spearman_corr, p_spearman = stats.spearmanr(df['Score_Pre'], df['Score_Post'])

print("--- Correlation Analysis (Score_Pre vs Score_Post) ---")
print(f"Pearson Correlation:  {pearson_corr:.4f} (p = {p_pearson:.4f})")
print(f"Spearman Correlation: {spearman_corr:.4f} (p = {p_spearman:.4f})\n")

# -------------------------------------------------------------------
# 6. VISUALIZATIONS
# -------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Boxplot comparing Post-Scores by Group
sns.boxplot(ax=axes[0], data=df, x='Group', y='Score_Post', palette='Set2')
axes[0].set_title('Post-Scores by Group')
axes[0].set_ylabel('Score')

# Plot 2: Scatter plot with regression line for Pre vs Post scores
sns.regplot(ax=axes[1], data=df, x='Score_Pre', y='Score_Post', color='teal')
axes[1].set_title('Pre-Score vs Post-Score Correlation')
axes[1].set_xlabel('Pre-Score')
axes[1].set_ylabel('Post-Score')

plt.tight_layout()
plt.show()