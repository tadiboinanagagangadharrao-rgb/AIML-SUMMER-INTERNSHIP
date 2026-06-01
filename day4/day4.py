import numpy as np
import pandas as pd

# =====================================================================
# 1. CREATE / LOAD DATA
# =====================================================================
# Creating a dummy dataset to demonstrate all operations
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": [" Alice ", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [28, 34, np.nan, 45, 28, 34],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "IT"],
    "Salary": [50000, 75000, 80000, 120000, np.nan, 75000],
    "Join_Date": ["2021-01-15", "2020-05-12", "2022-09-01", "2018-11-20", "2023-02-10", "2020-05-12"],
}
df = pd.DataFrame(data)

# (Alternative Load: df = pd.read_csv('file.csv'))

# =====================================================================
# 2. INSPECT THE DATA
# =====================================================================
print("--- FIRST 2 ROWS ---")
print(df.head(2))

print("\n--- DATA INFO & MISSING VALUES ---")
df.info()
print("\nMissing values per column:\n", df.isnull().sum())

# =====================================================================
# 3. CLEANING DATA
# =====================================================================
# Clean up string whitespace
df["Name"] = df["Name"].str.strip()

# Handle Missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())  # Fill Age with median
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())  # Fill Salary with mean

# Convert Join_Date column to actual datetime object
df["Join_Date"] = pd.to_datetime(df["Join_Date"])

# Remove exact duplicates (Row 6 is a duplicate of Row 2 in reality, except for ID)
# Let's drop duplicates based on specific columns
df = df.drop_duplicates(subset=["Name", "Age", "Department"], keep="first")

# =====================================================================
# 4. SELECTING & FILTERING
# =====================================================================
# Filter: IT employees making more than 70,000
it_high_earners = df[(df["Department"] == "IT") & (df["Salary"] > 70000)]

# Select specific columns using .loc
subset = df.loc[df["Age"] > 30, ["Name", "Salary"]]

# =====================================================================
# 5. MANIPULATING & CREATING COLUMNS
# =====================================================================
# Add a flag for high salary using a lambda function
df["Is_High_Earner"] = df["Salary"].apply(lambda x: "Yes" if x >= 80000 else "No")

# Extract year from the datetime column
df["Join_Year"] = df["Join_Date"].dt.year

# Rename a column
df = df.rename(columns={"Salary": "Annual_Salary"})

# =====================================================================
# 6. AGGREGATING & GROUPING
# =====================================================================
print("\n--- VALUE COUNTS (DEPARTMENTS) ---")
print(df["Department"].value_counts())

print("\n--- GROUP BY SUMMARY ---")
# Get total salary and average age per department
summary = df.groupby("Department").agg({"Annual_Salary": "sum", "Age": "mean"})
print(summary)

# =====================================================================
# 7. EXPORT DATA
# =====================================================================
# df.to_csv('cleaned_employees.csv', index=False)
print("\n--- FINAL CLEANED DATAFRAME ---")
print(df)