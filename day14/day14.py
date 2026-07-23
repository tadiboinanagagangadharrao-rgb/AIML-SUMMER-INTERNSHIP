import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Initialize in-memory database
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# --- Schema ---
cur.executescript(
    """
CREATE TABLE Customers (
    CustomerID   INTEGER PRIMARY KEY,
    CustomerName TEXT, City TEXT, State TEXT, Segment TEXT, SignupDate TEXT
);
CREATE TABLE Products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT, Category TEXT, Price INTEGER, Cost INTEGER
);
CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    CustomerID INTEGER, OrderDate TEXT, Status TEXT
);
CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY,
    OrderID TEXT, ProductID TEXT, Quantity INTEGER, UnitPrice INTEGER
);
CREATE TABLE Payments (
    PaymentID TEXT PRIMARY KEY,
    OrderID TEXT, PaymentMode TEXT, PaidAmount INTEGER, PaymentDate TEXT
);
"""
)

# --- Data Insertion ---
customers = [
    (1, "Asha Reddy", "Hyderabad", "Telangana", "Premium", "2024-02-10"),
    (2, "Ravi Kumar", "Mumbai", "Maharashtra", "Regular", "2024-05-15"),
    (3, "Imran Khan", "Pune", "Maharashtra", "Premium", "2023-11-20"),
    (4, "Divya Rao", "Delhi", "Delhi", "Regular", "2025-01-05"),
    (5, "Karan Mehta", "Hyderabad", "Telangana", "Premium", "2024-08-30"),
    (6, "Sneha Iyer", "Bengaluru", "Karnataka", "Regular", "2024-03-12"),
    (7, "Vikram Singh", "Delhi", "Delhi", "Premium", "2025-03-01"),
    (8, "Meena Nair", "Bengaluru", "Karnataka", "Regular", "2024-09-25"),
]
products = [
    ("P1", "Laptop Pro", "Electronics", 80000, 62000),
    ("P2", "Smartphone X", "Electronics", 45000, 34000),
    ("P3", "Wireless Mouse", "Accessories", 1500, 800),
    ("P4", "Mechanical Keyboard", "Accessories", 4000, 2500),
    ("P5", "Noise Headphones", "Audio", 12000, 8000),
    ("P6", "Smartwatch", "Wearables", 20000, 14000),
]
orders = [
    ("O-1001", 1, "2026-01-12", "Completed"),
    ("O-1002", 2, "2026-01-20", "Completed"),
    ("O-1003", 3, "2026-02-05", "Completed"),
    ("O-1004", 1, "2026-02-18", "Completed"),
    ("O-1005", 4, "2026-03-02", "Completed"),
    ("O-1006", 5, "2026-03-15", "Completed"),
    ("O-1007", 3, "2026-04-10", "Completed"),
    ("O-1008", 6, "2026-04-22", "Cancelled"),
    ("O-1009", 1, "2026-05-08", "Completed"),
    ("O-1010", 7, "2026-05-19", "Completed"),
    ("O-1011", 2, "2026-06-03", "Completed"),
    ("O-1012", 5, "2026-06-14", "Completed"),
]
order_items = [
    (1, "O-1001", "P1", 1, 80000),
    (2, "O-1001", "P3", 1, 1500),
    (3, "O-1002", "P2", 1, 45000),
    (4, "O-1003", "P1", 1, 80000),
    (5, "O-1003", "P5", 1, 12000),
    (6, "O-1004", "P6", 1, 20000),
    (7, "O-1005", "P2", 1, 45000),
    (8, "O-1005", "P4", 1, 4000),
    (9, "O-1006", "P1", 1, 80000),
    (10, "O-1007", "P5", 2, 12000),
    (11, "O-1008", "P3", 1, 1500),
    (12, "O-1009", "P2", 1, 45000),
    (13, "O-1009", "P3", 2, 1500),
    (14, "O-1010", "P1", 1, 80000),
    (15, "O-1010", "P6", 1, 20000),
    (16, "O-1011", "P5", 1, 12000),
    (17, "O-1011", "P4", 1, 4000),
    (18, "O-1012", "P6", 2, 20000),
]
payments = [
    ("PAY-1", "O-1001", "Card", 81500, "2026-01-12"),
    ("PAY-2", "O-1002", "UPI", 45000, "2026-01-20"),
    ("PAY-3", "O-1003", "Card", 92000, "2026-02-05"),
    ("PAY-4", "O-1004", "UPI", 20000, "2026-02-18"),
    ("PAY-5", "O-1005", "Card", 49000, "2026-03-02"),
    ("PAY-6", "O-1006", "NetBanking", 80000, "2026-03-15"),
    ("PAY-7", "O-1007", "UPI", 24000, "2026-04-10"),
    ("PAY-8", "O-1009", "Card", 48000, "2026-05-08"),
    ("PAY-9", "O-1010", "UPI", 95000, "2026-05-19"),
    ("PAY-10", "O-1011", "Card", 16000, "2026-06-03"),
]

cur.executemany("INSERT INTO Customers VALUES (?,?,?,?,?,?)", customers)
cur.executemany("INSERT INTO Products VALUES (?,?,?,?,?)", products)
cur.executemany("INSERT INTO Orders VALUES (?,?,?,?)", orders)
cur.executemany("INSERT INTO OrderItems VALUES (?,?,?,?,?)", order_items)
cur.executemany("INSERT INTO Payments VALUES (?,?,?,?,?)", payments)
conn.commit()
print("Database created and populated successfully.\n")


def run(sql):
    return pd.read_sql(sql, conn)


try:
    # --- Baseline KPIs ---
    print("--- Baseline KPIs ---")
    kpi_df = run("""
    SELECT 
        COUNT(DISTINCT o.OrderID) AS CompletedOrders,
        COUNT(DISTINCT o.CustomerID) AS ActiveCustomers,
        SUM(oi.Quantity * oi.UnitPrice) AS TotalRevenue
    FROM Orders o 
    JOIN OrderItems oi ON o.OrderID = oi.OrderID
    WHERE o.Status = 'Completed';
    """)
    print(kpi_df.to_string(index=False))
    print("\n" + "=" * 40 + "\n")

    # --- Profit by Category ---
    print("--- Profit by Category ---")
    profit_df = run("""
    SELECT 
        p.Category,
        SUM(oi.Quantity * oi.UnitPrice) AS Revenue,
        SUM(oi.Quantity * (oi.UnitPrice - p.Cost)) AS Profit
    FROM Orders o
    JOIN OrderItems oi ON o.OrderID = oi.OrderID
    JOIN Products p ON oi.ProductID = p.ProductID
    WHERE o.Status = 'Completed'
    GROUP BY p.Category 
    ORDER BY Profit DESC;
    """)
    print(profit_df.to_string(index=False))

    # --- Visualization ---
    cat = run("""
    SELECT 
        p.Category, 
        SUM(oi.Quantity * oi.UnitPrice) AS Revenue
    FROM Orders o
    JOIN OrderItems oi ON o.OrderID = oi.OrderID
    JOIN Products p ON oi.ProductID = p.ProductID
    WHERE o.Status = 'Completed'
    GROUP BY p.Category 
    ORDER BY Revenue DESC;
    """)

    plt.figure(figsize=(8, 5))
    ax = sns.barplot(data=cat, x="Category", y="Revenue", palette="Blues_r")
    plt.title("Revenue by Category", fontsize=14, fontweight="bold")
    plt.xlabel("Category", fontsize=11)
    plt.ylabel("Revenue (₹)", fontsize=11)
    plt.ticklabel_format(style="plain", axis="y")

    # Adding values on top of bars
    for p in ax.patches:
        ax.annotate(
            f"₹{int(p.get_height()):,}",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 5),
            textcoords="offset points",
        )

    plt.tight_layout()
    plt.show()

finally:
    conn.close()
    print("Analysis complete; database connection safely closed.")