import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# 1. SETUP & GENERAL STYLING
# -------------------------------------------------------------------------
# Set a clean grid style and standard figure size
plt.style.use('seaborn-v0_8-whitegrid') 
plt.rcParams['figure.figsize'] = (8, 5)

# Generate dummy data for plotting
x = np.linspace(0, 10, 100)
y_sine = np.sin(x)
y_cosine = np.cos(x)

categories = ['Group A', 'Group B', 'Group C', 'Group D']
values = [15, 30, 45, 10]

# -------------------------------------------------------------------------
# 2. LINE PLOT (Great for trends over time/continuous data)
# -------------------------------------------------------------------------
plt.figure()
plt.plot(x, y_sine, label='Sine Wave', color='blue', linewidth=2, linestyle='-')
plt.plot(x, y_cosine, label='Cosine Wave', color='red', linewidth=2, linestyle='--')

# Customizing Labels, Titles, and Legend
plt.title('Line Plot: Sine and Cosine Waves', fontsize=14, fontweight='bold')
plt.xlabel('X Axis (Time/Index)', fontsize=12)
plt.ylabel('Y Axis (Amplitude)', fontsize=12)
plt.legend(loc='upper right') # Shows labels assigned in plt.plot()
plt.xlim(0, 10)               # Set limits for X-axis
plt.ylim(-1.5, 1.5)           # Set limits for Y-axis

plt.show()

# -------------------------------------------------------------------------
# 3. SCATTER PLOT (Great for showing relationships between two variables)
# -------------------------------------------------------------------------
# Generate some random cluster data
np.random.seed(42)
scatter_x = np.random.rand(50) * 10
scatter_y = scatter_x * 2 + np.random.randn(50) * 3

plt.figure()
# 'c' sets color based on a variable, 'cmap' sets the color palette
plt.scatter(scatter_x, scatter_y, color='purple', s=80, alpha=0.7, edgecolors='black')

plt.title('Scatter Plot: X vs Y Relationship', fontsize=14)
plt.xlabel('Feature X')
plt.ylabel('Target Y')
plt.show()

# -------------------------------------------------------------------------
# 4. BAR PLOT (Great for comparing discrete categories)
# -------------------------------------------------------------------------
plt.figure()
# Creating a vertical bar chart
plt.bar(categories, values, color=['#3498db', '#e74c3c', '#2ecc71', '#f1c40f'], edgecolor='black')

plt.title('Bar Chart: Category Comparisons', fontsize=14)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# -------------------------------------------------------------------------
# 5. HISTOGRAM (Great for viewing the distribution of a single variable)
# -------------------------------------------------------------------------
# Generate 1000 data points from a normal distribution
normal_data = np.random.randn(1000)

plt.figure()
# 'bins' controls the number of intervals/bars
plt.hist(normal_data, bins=30, color='teal', edgecolor='white', alpha=0.8)

plt.title('Histogram: Data Frequency Distribution', fontsize=14)
plt.xlabel('Value Intervals')
plt.ylabel('Frequency Count')
plt.show()

# -------------------------------------------------------------------------
# 6. PIE CHART (Great for part-to-whole compositions)
# -------------------------------------------------------------------------
plt.figure(figsize=(6, 6)) # Make it square for a perfect circle
explode = (0, 0, 0.1, 0)  # slightly "explode" or pop out the 3rd slice (Group C)

plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, 
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'], explode=explode, shadow=True)

plt.title('Pie Chart: Market/Group Share', fontsize=14)
plt.show()

# -------------------------------------------------------------------------
# 7. SUBPLOTS (Grid Layout: Displaying multiple plots together)
# -------------------------------------------------------------------------
# Create a grid of 2 rows and 2 columns
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Top-Left Subplot (Row 0, Col 0)
axes[0, 0].plot(x, y_sine, color='blue')
axes[0, 0].set_title('Sine Wave')

# Top-Right Subplot (Row 0, Col 1)
axes[0, 1].scatter(scatter_x, scatter_y, color='purple')
axes[0, 1].set_title('Scatter Data')

# Bottom-Left Subplot (Row 1, Col 0)
axes[1, 0].bar(categories, values, color='orange')
axes[1, 0].set_title('Category Bars')

# Bottom-Right Subplot (Row 1, Col 1)
axes[1, 1].hist(normal_data, bins=15, color='teal')
axes[1, 1].set_title('Histogram Data')

# Automatically adjust padding between subplots to avoid overlapping text
plt.tight_layout()

# Save the grid plot to your computer
plt.savefig('my_matplotlib_dashboard.png', dpi=300)
plt.show()

print("=== ALL PLOTS GENERATED AND DASHBOARD SAVED ===")