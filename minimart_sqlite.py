import sqlite3
# This creates a new SQLite database file
conn = sqlite3.connect("minimart.db")
cursor = conn.cursor() # Create a cursor object to execute SQL commands
 #Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

print("✅ Tables created successfully!")

#INSERT DATA
# Clear old data (for re-runs)
cursor.execute("DELETE FROM customers")
cursor.execute("DELETE FROM products")
cursor.execute("DELETE FROM orders")

# Insert customers
customers = [("Ruth",), ("Rose",), ("Chaxxy",), ("Dre",)]
cursor.executemany("INSERT INTO customers (name) VALUES (?)", customers)

# Insert products
products = [("Milk", 60.0), ("Bread", 70.0), ("Eggs", 90.0), ("Juice", 200.0)]
cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

# Insert orders (customer_id, product_id, quantity)
orders = [
    (1, 1, 2),  # Ruth buys 2 Milk
    (2, 2, 3),  # Rose buys 3 Bread
    (1, 3, 1),  # Ruth buys 1 Eggs
    (4, 4, 5),  # Dre buys 5 Juice
    (3, 1, 1)   # Chaxxy buys 1 Milk
]
cursor.executemany("INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)", orders) # Insert multiple records

conn.commit() # Commit changes to the database
print("✅ Sample data inserted successfully!")

#  Run SQL Queries

# Retrieve all orders made by a specific customer (Ruth)
print("\n--- Orders by Ruth ---")
cursor.execute("""
SELECT customers.name, products.name, orders.quantity
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN products ON orders.product_id = products.id
WHERE customers.name = 'Ruth'
""")
for row in cursor.fetchall(): # Fetch and print all matching records
    print(row)

# Get total number of orders
cursor.execute("SELECT COUNT(*) FROM orders") #the actual number of orders
total_orders = cursor.fetchone()[0]
print(f"\nTotal number of orders: {total_orders}")

#Calculate total revenue generated
cursor.execute("""
SELECT SUM(products.price * orders.quantity)
FROM orders
JOIN products ON orders.product_id = products.id
""")
total_revenue = cursor.fetchone()[0]
print(f"Total revenue: KES {total_revenue}")

# Show order details  through INNER JOIN
print("\n--- All Order Details (INNER JOIN) ---")
cursor.execute("""
SELECT customers.name, products.name, products.price, orders.quantity
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN products ON orders.product_id = products.id
""")
for row in cursor.fetchall():
    print(row)

# Show all products and any related order via LEFT JOIN
print("\n--- All Products and Related Orders (LEFT JOIN) ---")
cursor.execute("""
SELECT products.name, orders.quantity
FROM products
LEFT JOIN orders ON products.id = orders.product_id
""")
for row in cursor.fetchall():
    print(row)


#Close connection

conn.close() # Close the database connection
print("\n Database connection closed successfully.")


