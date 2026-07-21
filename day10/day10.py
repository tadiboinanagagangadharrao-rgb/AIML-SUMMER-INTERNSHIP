import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame({
"OrderID": [1001, 1002, 1003, 1003, 1005, 1006, 1007, 1008],
"Customer": ["asha", "RAVI", "Imran", "Imran", "Sneha", "Karan", "Meena",
"Tara"],
"City": ["Pune", "mumbai", "Pune", "Pune", "Delhi", "Mumbai", "delhi",
"Pune"],
"Category": ["Electronics", "Clothing", "Electronics", "Electronics",
"Grocery", "Electronics", "Clothing", "Grocery"],
"Amount": [25000, np.nan, 18000, 18000, 1200, 999999, 3200, 1500],
"Quantity": [2, 3, 1, 1, 5, 1, -2, 4],
"OrderDate": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02",
"2026-05-03", "2026-05-03", "2026-05-04", "2026-05-05"]
})
print(df.head())
sns.set_theme(style="whitegrid")
cat_rev = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
sns.barplot(x=cat_rev.index, y=cat_rev.values)
plt.title("Total Revenue by Category")
plt.xlabel("Category"); plt.ylabel("Revenue")
plt.show()
sns.set_theme(style="whitegrid")
cat_rev = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
sns.barplot(x=cat_rev.index, y=cat_rev.values)
plt.title("Total Revenue by Category")
plt.xlabel("Category"); plt.ylabel("Revenue")
plt.show()
