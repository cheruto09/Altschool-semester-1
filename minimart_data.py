
# Use of lists of dictionaries to simulate tables (like SQL tables).

# Product list: each product has an ID, name, and price (as a string for now)
products = [

    {"product_id": 1, "name": "Milk", "price": "60"},
    {"product_id": 2, "name": "Bread", "price": "70"},
    {"product_id": 3, "name": "Eggs", "price": "90"},
    {"product_id": 4, "name": "Juice", "price": "200"},
    
]

# Customer list: each has an ID and name
customers = [
    {"customer_id": 1, "name": "Ruth"},
    {"customer_id": 2, "name": "Rose"},
    {"customer_id": 3, "name": "Chaxxy"},
    {"customer_id": 4, "name": "Dre"}
]

# Orders list: joins customer_id and product_id with quantity ordered
orders = [
    {"order_id": 1, "customer_id": 1, "product_id": 1, "quantity": 2},
    {"order_id": 2, "customer_id": 2, "product_id": 2, "quantity": 3},
    {"order_id": 1, "customer_id": 1, "product_id": 3, "quantity": 1},
    {"order_id": 3, "customer_id": 4, "product_id": 4, "quantity": 5},
    {"order_id": 4, "customer_id": 3, "product_id": 1, "quantity": 1}
]


#PRICE CONVERSION AND DISCOUNT APPLICATION
# Convert product prices from string → float 
# Then apply a 10% discount if the price is above 100
for product in products:
    product["price"] = float(product["price"])  # convert string to float
    if product["price"] > 100:
        product["price"] *= 0.9  # apply 10% discount

print("Updated product prices after discount:")
for product in products:
    print(product)  # prints each product’s details after discount


# IDENTIFY CUSTOMERS WITH LARGE ORDERS 
# logical conditions (if, and, or) to find customers with >3 total items ordered
print("\n  Customers with large orders:")
for customer in customers:
    # Calculate total quantity ordered by each customer
    total_quantity = sum(order["quantity"] for order in orders if order["customer_id"] == customer["customer_id"])
    if total_quantity > 3:  # if they ordered more than 3 items
        print(f"{customer['name']} ordered {total_quantity} items (large order!)")


#  GENERATE SUMMARY REPORT 
#  Total products sold
# Most popular product
# Revenue per customer

# Total number of products sold
total_sold = sum(order["quantity"] for order in orders)

# Determine the most popular product (highest total quantity)
product_sales = {}
for order in orders:
    pid = order["product_id"]
    product_sales[pid] = product_sales.get(pid, 0) + order["quantity"]

most_popular_id = max(product_sales, key=product_sales.get)
most_popular_name = next(p["name"] for p in products if p["product_id"] == most_popular_id)

#Calculate total revenue per customer
revenue_per_customer = {}
for order in orders:
    product = next(p for p in products if p["product_id"] == order["product_id"])
    customer = next(c for c in customers if c["customer_id"] == order["customer_id"])
    revenue = order["quantity"] * product["price"]
    revenue_per_customer[customer["name"]] = revenue_per_customer.get(customer["name"], 0) + revenue

# Final report dictionary to summarize all key metrics
report = {
    "Total Products Sold": total_sold,
    "Most Popular Product": most_popular_name,
    "Revenue Per Customer": revenue_per_customer
}

# Print report results
print("\n  Summary Report:")
for key, value in report.items():
    print(f"{key}: {value}")
