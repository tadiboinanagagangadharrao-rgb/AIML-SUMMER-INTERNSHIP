import sqlite3
import pandas as pd

# Create an in-memory database for this exercise
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
print("Database connection established.")
cursor.execute("""
CREATE TABLE Customers (
    CustomerID   INTEGER PRIMARY KEY,
    CustomerName TEXT,
    City         TEXT,
    Segment      TEXT
)
""")

cursor.execute("""
CREATE TABLE Products (
    ProductID   TEXT PRIMARY KEY,
    ProductName TEXT,
    Category    TEXT,
    Price       INTEGER
)
""")

cursor.execute("""
CREATE TABLE Orders (
    OrderID     INTEGER PRIMARY KEY,
    CustomerID  INTEGER,
    ProductID   TEXT,
    Quantity    INTEGER,
    OrderAmount INTEGER,
    OrderDate   TEXT
)
""")
print("Tables created.")
customers = [
    (101, "Rajesh", "Hyderabad", "Premium"),
    (102, "Priya", "Bengaluru", "Regular"),
    (103, "Aman", "Mumbai", "Premium"),
    (104, "Sneha", "Delhi", "Regular"),
    (105, "Karan", "Hyderabad", "Premium")
]
products = [
    ("P1", "Laptop", "Electronics", 60000),
    ("P2", "Phone", "Electronics", 30000),
    ("P3", "Mouse", "Accessories", 1200)
]
orders = [
    (5001, 101, "P1", 1, 60000, "2026-05-01"),
    (5002, 102, "P2", 2, 60000, "2026-05-02"),
    (5003, 101, "P3", 3, 3600, "2026-05-03"),
    (5004, 103, "P1", 1, 60000, "2026-05-05"),
    (5005, 104, "P2", 1, 30000, "2026-05-07"),
    (5006, 101, "P2", 1, 30000, "2026-05-09")
]

cursor.executemany("INSERT INTO Customers VALUES (?,?,?,?)", customers)
cursor.executemany("INSERT INTO Products VALUES (?,?,?,?)", products)
cursor.executemany("INSERT INTO Orders VALUES (?,?,?,?,?,?)", orders)
conn.commit()
print("Sample data inserted.")
query = """
SELECT c.CustomerName, o.OrderAmount
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
"""
print(pd.read_sql(query, conn))
query = "SELECT COUNT(*) AS Orders, SUM(OrderAmount) AS Revenue, AVG(OrderAmount) AS AvgValue FROM Orders"
print(pd.read_sql(query, conn))
query = """
SELECT CustomerID, SUM(OrderAmount) AS TotalSpent
FROM Orders
GROUP BY CustomerID
ORDER BY TotalSpent DESC
"""
print(pd.read_sql(query, conn))
query = """
SELECT CustomerID, SUM(OrderAmount) AS TotalSpent
FROM Orders
GROUP BY CustomerID
HAVING SUM(OrderAmount) > 50000
"""
print(pd.read_sql(query, conn))
query = """
SELECT c.CustomerName, c.City, SUM(o.OrderAmount) AS TotalSpent
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName, c.City
HAVING SUM(o.OrderAmount) > 50000
ORDER BY TotalSpent DESC
"""
report = pd.read_sql(query, conn)
print(report)
conn.close()
print("Connection closed.")



