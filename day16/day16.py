import numpy as np
import pandas as pd
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Global Significance Level
ALPHA = 0.05

def print_decision(p_value, alpha=ALPHA):
    """Utility function to print hypothesis test decision."""
    print(f"p-value: {p_value:.4f}")
    if p_value < alpha:
        print(f"Decision: Reject H0 (p < {alpha}). There is a statistically significant effect.")
    else:
        print(f"Decision: Fail to Reject H0 (p >= {alpha}). Insufficient evidence for effect.")
    print("-" * 60)


# =====================================================================
# 1. ONE-SAMPLE t-TEST
# Concept: Compare a sample mean against a known target/population mean.
# =====================================================================
print("=== 1. ONE-SAMPLE t-TEST ===")
print("Scenario: Testing if average customer wait time exceeds target of 5 minutes.")
print("H0: Mean wait time = 5.0 mins")
print("H1: Mean wait time != 5.0 mins\n")

# Synthetic wait times (mean ~ 5.4 mins)
wait_times = np.random.normal(loc=5.4, scale=1.2, size=30)
target_mean = 5.0

t_stat, p_val = stats.ttest_1samp(wait_times, popmean=target_mean)
print(f"Sample Mean: {np.mean(wait_times):.2f}")
print(f"t-statistic: {t_stat:.4f}")
print_decision(p_val)


# =====================================================================
# 2. TWO-SAMPLE INDEPENDENT t-TEST
# Concept: Compare means of two completely independent groups.
# =====================================================================
print("=== 2. TWO-SAMPLE INDEPENDENT t-TEST ===")
print("Scenario: Comparing conversion rate between Web Design A and Web Design B.")
print("H0: Mean(Design A) = Mean(Design B)")
print("H1: Mean(Design A) != Mean(Design B)\n")

group_a = np.random.normal(loc=12.5, scale=2.0, size=40)  # Design A
group_b = np.random.normal(loc=14.1, scale=2.1, size=40)  # Design B

t_stat, p_val = stats.ttest_ind(group_a, group_b)
print(f"Group A Mean: {np.mean(group_a):.2f} | Group B Mean: {np.mean(group_b):.2f}")
print(f"t-statistic: {t_stat:.4f}")
print_decision(p_val)


# =====================================================================
# 3. PAIRED SAMPLES t-TEST
# Concept: Compare measurements from the SAME subject before and after.
# =====================================================================
print("=== 3. PAIRED SAMPLES t-TEST ===")
print("Scenario: Weight of participants before and after a 4-week fitness program.")
print("H0: Mean Difference (Before - After) = 0")
print("H1: Mean Difference (Before - After) != 0\n")

weight_before = np.random.normal(loc=80.0, scale=10.0, size=25)
# Weight drops slightly after training
weight_after = weight_before - np.random.normal(loc=1.8, scale=1.0, size=25)

t_stat, p_val = stats.ttest_rel(weight_before, weight_after)
print(f"Avg Weight Before: {np.mean(weight_before):.2f} kg")
print(f"Avg Weight After:  {np.mean(weight_after):.2f} kg")
print(f"t-statistic: {t_stat:.4f}")
print_decision(p_val)


# =====================================================================
# 4. CHI-SQUARE TEST OF INDEPENDENCE
# Concept: Check for a relationship between two categorical variables.
# =====================================================================
print("=== 4. CHI-SQUARE TEST OF INDEPENDENCE ===")
print("Scenario: Testing if Subscription Choice depends on Device Type.")
print("H0: Device Type and Subscription Choice are independent.")
print("H1: Device Type and Subscription Choice are dependent.\n")

# Contingency Table: [Basic, Premium] subscriptions across [Mobile, Desktop]
contingency_table = np.array([
    [120, 50],   # Mobile users [Basic, Premium]
    [60,  80]    # Desktop users [Basic, Premium]
])

chi2_stat, p_val, dof, expected = stats.chi2_contingency(contingency_table)
print(f"Chi-Square Statistic: {chi2_stat:.4f}")
print(f"Degrees of Freedom:   {dof}")
print_decision(p_val)