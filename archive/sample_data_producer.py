import json
from datetime import date
from main import Product

# Sample products
products = [
    Product("Apple", 1, 0.99, 5),
    Product("Banana", 2, 0.25, 10),
    Product("Strawberry", 3, 1.10, 5),
    Product("Lettuce", 4, 0.35, 10),
    Product("Potato", 5, 1.50, 5),
    Product("Celery", 6, 2.80, 10),
    Product("Carrot", 7, 0.20, 5),
    Product("Orange", 8, 0.40, 8),
    Product("Avocado", 9, 1.25, 1),
    Product("Blueberry", 10, 0.10, 3)
]

log = {
    "transaction_date": "2/4/2024",
    "transaction_time": "12:31:00",
    "transaction_total": 1.99,
    "items_sold": [
        {"name": "Apple",
        "sku": 1,
        "price": 0.99,
        "qty_sold": 1},
        {"name": "Banana",
        "sku": 2,
        "price": 0.25,
        "qty_sold": 4}
    ]
}

log_file = "log.json"
with open(log_file, "w") as file:
    json.dump(log, file, indent=1)
