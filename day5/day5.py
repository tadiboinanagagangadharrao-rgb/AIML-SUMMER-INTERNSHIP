import numpy as np
import pandas as pd

# =====================================================================
# 1. CREATE A MESSY DATASET
# =====================================================================
raw_data = {
    "User_ID": [101, 102, 102, 103, 104, 105],
    "Name": ["  john doe ", "Jane Smith", "Jane Smith", "sam brown", "Emily ", "Alex"],
    "Age": ["28", "34", "34", "missing", "45", "-5"],  # Mix of strings, text, and negative age
    "Join_Date": [
        "2023/01/15",
        "2022-05-12",
        "2022-05-12",
        "12-11-2021",
        np.nan,
        "2024-02-10",
    ],
    "Salary": [50000, 75000, 75000, 62000, np.nan, 300000],  # NaN and a massive outlier
    "Active": ["Yes", "no", "no", "YES", "No", "Yes"],  # Inconsistent casing
}

df = pd.DataFrame(raw_data)
print("--- ORIGINAL MESSY DATAFRAME ---")
print(df)
print("\n" + "=" * 50 + "\n")

# =====================================================================
# 2. IDENTIFY MISSING VALUES & DUPLICATES
# =====================================================================
# Check for total missing values per column
print("Missing Value Counts:\n", df.isnull().sum())

# Check for duplicate rows
print("\nNumber of duplicate rows:", df.duplicated().sum())

# =====================================================================
# 3. CLEANING PIPELINE
# =====================================================================

# --- Step A: Remove Duplicates ---
df = df.drop_duplicates(keep="first")

# --- Step B: Clean Text Columns (Strings) ---
# Strip whitespace and normalize to Title Case
df["Name"] = df["Name"].str.strip().str.title()
# Standardize boolean-like text columns to lowercase
df["Active"] = df["Active"].str.strip().str.lower()

# --- Step C: Fix Data Types & Coerce Errors ---
# 'errors="coerce"' turns non-numeric values (like "missing") into NaN
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Handle inconsistent date formats and parse into standard YYYY-MM-DD
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# --- Step D: Handle Missing Values (Imputation) ---
# Fill Age with the column median (safest for skewed data)
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Salary with the column mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# --- Step E: Handle Logical Errors & Outliers ---
# Fix logical errors (e.g., negative Age) by turning them positive
df["Age"] = df["Age"].abs()

# Cap extreme salary outliers using the Interquartile Range (IQR) method
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + (1.5 * IQR)

# Filter out rows where salary is an extreme outlier
df = df[df["Salary"] <= upper_limit]

# =====================================================================
# 4. FINAL CLEAN OUTPUT
# =====================================================================
print("\n" + "=" * 50 + "\n")
print("--- FINAL CLEANED DATAFRAME ---")
print(df)

# Reset index so it's clean and continuous
df = df.reset_index(drop=True)

# Save to a new CSV file
# df.to_csv('cleaned_data.csv', index=False)