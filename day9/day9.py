import sqlite3
import pandas as pd


# 1. CONNECT TO THE SQLite DATABASE
# This creates a local database file named 'company.db' automatically
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
print("[INFO] Connected successfully to 'company.db' relational database.")

# 2. CREATE THE CUSTOMERS TABLE AND INSERT DATA
# Cleaning old tables to avoid conflicts
cursor.execute("DROP TABLE IF EXISTS customers")

# Generating the relational schema
cursor.execute("""
CREATE TABLE customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT,
    City TEXT,
    Age INTEGER
)
""")

# Sample Data records matching the training module syllabus
customer_records = [
    (101, "Rakesh", "Hyderabad", 28),
    (102, "Priyanka", "Bengaluru", 34),
    (103, "Amani", "Mumbai", 22),
    (104, "Snehitha", "Delhi", 41),
    (105, "Karan", "Hyderabad", 30)
]

# Loading rows into the relational framework
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customer_records)
conn.commit()
print("[INFO] Relational 'customers' table created and populated successfully.\n")

# =====================================================================
# HANDS-ON SQL QUERIES EXECUTIONS VIA PANDAS
# =====================================================================

print("-" * 60)
print("TASK 1: Retrieve All Records (SELECT *)")
print("-" * 60)
query_all = "SELECT * FROM customers;"
df_all = pd.read_sql(query_all, conn)
print(df_all)
print()

print("-" * 60)
print("TASK 2: Retrieve Specific Columns (Name, City)")
print("-" * 60)
query_columns = "SELECT Name, City FROM customers;"
df_columns = pd.read_sql(query_columns, conn)
print(df_columns)
print()

print("-" * 60)
print("TASK 3: Apply Filter (WHERE City = 'Hyderabad')")
print("-" * 60)
query_filter = "SELECT Name, Age FROM customers WHERE City = 'Hyderabad';"
df_filter = pd.read_sql(query_filter, conn)
print(df_filter)
print()

print("-" * 60)
print("TASK 4: Use Logical Operators (City = 'Hyderabad' AND Age > 28)")
print("-" * 60)
query_logical = "SELECT * FROM customers WHERE City = 'Hyderabad' AND Age > 28;"
df_logical = pd.read_sql(query_logical, conn)
print(df_logical)
print()

print("-" * 60)
print("TASK 5: Sort Data (ORDER BY Age DESC)")
print("-" * 60)
query_sort = "SELECT Name, Age FROM customers ORDER BY Age DESC;"
df_sort = pd.read_sql(query_sort, conn)
print(df_sort)
print()

print("-" * 60)
print("TASK 6: Combined Analytical Pattern (SELECT -> WHERE -> ORDER BY)")
print("-" * 60)
query_combined = """
SELECT Name, City, Age
FROM customers
WHERE Age > 25
ORDER BY Age DESC;
"""
df_combined = pd.read_sql(query_combined, conn)
print(df_combined)
print()

# 3. ENVIRONMENT CLEANUP
conn.close()
print("=" * 60)
print("[INFO] Database connection safely disconnected. Task Complete!")
print("=" * 60)