import pandas as pd

# All lists must have the exact same length (6 items each)
df = pd.DataFrame({
    "Region": ["North", "South", "North", "East", "West", "South"],
    "Product": ["A", "B", "A", "C", "B", "A"],
    "Sales": [200, 350, 180, 500, 220, 310],  # Added comma here
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 55000, 40000, 90000, 60000, 52000]
})

print("--- Original DataFrame ---")
print(df)

print("\n--- Filtering (Sales > 200) ---")
print(df[df["Sales"] > 200])

print("\n--- Sorting by Sales ---")
print(df.sort_values("Sales"))

print("\n--- Total salary by dept ---")
print(df.groupby("Department")["Salary"].sum())

print("\n--- Average salary by dept ---")
print(df.groupby("Department")["Salary"].mean())

print("\n--- Employee count by dept ---")
print(df.groupby("Department")["Salary"].count())