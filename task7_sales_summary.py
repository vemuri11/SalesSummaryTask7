import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")

# Run SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
"""

# Load into pandas
df = pd.read_sql_query(query, conn)

# Print result
print("\n📊 Sales Summary:\n")
print(df)

# Plot
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()

# Save and show plot
plt.savefig("sales_chart.png")
plt.show()

# Close DB connection
conn.close()