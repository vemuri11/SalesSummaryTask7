import sqlite3

try:
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    # Insert data
    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", [
        ('Apples', 10, 2.5),
        ('Oranges', 5, 3.0),
        ('Bananas', 7, 1.8),
        ('Apples', 4, 2.5),
        ('Oranges', 3, 3.0),
    ])

    conn.commit()
    print("✅ Database created and data inserted successfully.")

except sqlite3.Error as e:
    print("❌ SQLite error:", e)

except Exception as e:
    print("❌ Unexpected error:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("🔒 Database connection closed.")