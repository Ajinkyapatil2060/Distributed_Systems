from django.shortcuts import render

import threading
from core.models import User, Product, Order
from django.db import IntegrityError

# Input data
users_data = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "David", "email": "david@example.com"},
    {"id": 5, "name": "Eve", "email": "eve@example.com"},
    {"id": 6, "name": "Frank", "email": "frank@example.com"},
    {"id": 7, "name": "Grace", "email": "grace@example.com"},
    {"id": 8, "name": "Alice", "email": "alice@example.com"},
    {"id": 9, "name": "Henry", "email": "henry@example.com"},
    {"id": 10, "name": None, "email": "jane@example.com"},  # Invalid (name is missing)
]
products_data = [
    {"id": 1, "name": "Laptop", "price": 1000.00},
    {"id": 2, "name": "Smartphone", "price": 700.00},
    {"id": 3, "name": "Headphones", "price": 150.00},
    {"id": 4, "name": "Monitor", "price": 300.00},
    {"id": 5, "name": "Keyboard", "price": 50.00},
    {"id": 6, "name": "Mouse", "price": 30.00},
    {"id": 7, "name": "Laptop", "price": 1000.00},
    {"id": 8, "name": "Smartwatch", "price": 250.00},
    {"id": 9, "name": "Gaming Chair", "price": 500.00},
    {"id": 10, "name": "Earbuds", "price": -50.00},  # Invalid (negative price)
]

orders_data = [
    {"id": 1, "user_id": 1, "product_id": 1, "quantity": 2},
    {"id": 2, "user_id": 2, "product_id": 2, "quantity": 1},
    {"id": 3, "user_id": 3, "product_id": 3, "quantity": 5},
    {"id": 4, "user_id": 4, "product_id": 4, "quantity": 1},
    {"id": 5, "user_id": 5, "product_id": 5, "quantity": 3},
    {"id": 6, "user_id": 6, "product_id": 6, "quantity": 4},
    {"id": 7, "user_id": 7, "product_id": 7, "quantity": 2},
    {"id": 8, "user_id": 8, "product_id": 8, "quantity": 0},  # Invalid (zero quantity)
    {"id": 9, "user_id": 9, "product_id": 1, "quantity": -1},  # Invalid (negative quantity)
    {"id": 10, "user_id": 10, "product_id": 11, "quantity": 2},  # Invalid (product_id 11 doesn't exist)
]
# Validation and insertion functions
def insert_users():
    for user in users_data:
        if not user['name'] or not user['email']:
            print(f"Invalid user data: {user}")
            continue
        try:
            User.objects.using('users_db').create(**user)
            print(f"Inserted user: {user}")
        except IntegrityError as e:
            print(f"Error inserting user {user}: {e}")

def insert_products():
    for product in products_data:
        if product['price'] < 0:
            print(f"Invalid product price: {product}")
            continue
        try:
            Product.objects.using('products_db').create(**product)
            print(f"Inserted product: {product}")
        except IntegrityError as e:
            print(f"Error inserting product {product}: {e}")

def insert_orders():
    for order in orders_data:
        if order['quantity'] <= 0:
            print(f"Invalid order quantity: {order}")
            continue
        try:
            Order.objects.using('orders_db').create(**order)
            print(f"Inserted order: {order}")
        except IntegrityError as e:
            print(f"Error inserting order {order}: {e}")

# Simulate concurrent insertion
def run_concurrent_insertions():
    threads = [
        threading.Thread(target=insert_users),
        threading.Thread(target=insert_products),
        threading.Thread(target=insert_orders),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


