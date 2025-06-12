import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", [
    ('Apples', 10, 2.5),
    ('Oranges', 5, 3.0),
    ('Bananas', 7, 1.8),
    ('Apples', 4, 2.5),
    ('Oranges', 3, 3.0),
])

conn.commit()
conn.close()

print("✅ Database created and sample data inserted.")