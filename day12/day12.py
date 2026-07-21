import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Set display options for clear terminal output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# ==========================================
# 1. SETUP: Create Sample Dataset
# ==========================================
raw_data = {
    'CustomerID': [101, 102, 103, 104, 105],
    'SignupDate': ['2025-01-15', '2025-06-20', '2025-11-05', '2026-02-10', '2026-05-01'],
    'Age': [23, 45, 18, 35, 52],
    'Income': [35000, 120000, 15000, 85000, 250000],  # Highly skewed numerical data
    'AccountType': ['Basic', 'Premium', 'Basic', 'Standard', 'Premium'], # Ordinal/Nominal
    'DeviceType': ['Mobile', 'Desktop', 'Mobile', 'Mobile', 'Desktop'],  # Nominal
    'MonthlySpend': [120.5, 450.0, 50.0, 310.2, 890.0]
}

df = pd.DataFrame(raw_data)
print("=== 1. Raw Dataset ===")
print(df)
print("\n" + "="*60 + "\n")

# ==========================================
# 2. FEATURE CREATION (Engineering New Columns)
# ==========================================

# A. Date-Time Features (Extracting temporal components)
df['SignupDate'] = pd.to_datetime(df['SignupDate'])
df['SignupYear'] = df['SignupDate'].dt.year
df['SignupMonth'] = df['SignupDate'].dt.month
df['SignupDayOfWeek'] = df['SignupDate'].dt.day_name()

# B. Interaction Features (Combining existing variables)
# Ratio of monthly spend relative to total income
df['SpendToIncomeRatio'] = df['MonthlySpend'] / (df['Income'] / 12)

# C. Binning / Discretization (Converting continuous to categorical)
# Segmenting Age into age brackets
age_bins = [0, 25, 40, 65]
age_labels = ['Young', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

print("=== 2. Dataset After Feature Creation ===")
print(df[['CustomerID', 'SignupDayOfWeek', 'SpendToIncomeRatio', 'AgeGroup']])
print("\n" + "="*60 + "\n")

# ==========================================
# 3. DATA TRANSFORMATION (Scaling & Encoding)
# ==========================================

# A. Log Transformation (Handling Skewed Distributions)
# Mitigates heavy right-skew in financial features (e.g., Income)
df['Log_Income'] = np.log1p(df['Income'])

# B. Ordinal Encoding (Mapping ordered categories to integers)
account_mapping = {'Basic': 1, 'Standard': 2, 'Premium': 3}
df['AccountType_Encoded'] = df['AccountType'].map(account_mapping)

# C. One-Hot Encoding (Converting nominal categories into binary flags)
df_encoded = pd.get_dummies(df, columns=['DeviceType'], prefix='Device', drop_first=False)

# D. Feature Scaling (Standardization / Z-score Normalization)
scaler = StandardScaler()
df_encoded[['Scaled_Spend', 'Scaled_Log_Income']] = scaler.fit_transform(
    df_encoded[['MonthlySpend', 'Log_Income']]
)

print("=== 3. Final Transformed Dataset ===")
selected_columns = [
    'CustomerID', 'Log_Income', 'Scaled_Log_Income', 
    'AccountType_Encoded', 'Device_Desktop', 'Device_Mobile', 'Scaled_Spend'
]
print(df_encoded[selected_columns])