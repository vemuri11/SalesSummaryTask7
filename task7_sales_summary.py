import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    # Step 1: Connect to the database
    conn = sqlite3.connect("sales_data.db")
    print("✅ Connected to database successfully.")
    
    # Step 2: Run SQL Query
    query = """
    SELECT 
        product, 
        SUM(quantity) AS total_qty, 
        SUM(quantity * price) AS revenue 
    FROM sales 
    GROUP BY product;
    """
    
    # Step 3: Load result into pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # Step 4: Print results
    print("\n📊 Sales Summary:\n")
    print(df)

    # Step 5: Plotting bar chart
    df.plot(kind='bar', x='product', y='revenue', legend=False)
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("sales_chart.png")
    plt.show()

except sqlite3.Error as e:
    print("❌ SQLite error:", e)

except Exception as e:
    print("❌ Unexpected error:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("🔒 Database connection closed.")