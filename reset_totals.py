import json
new_totals = {"totalAmounts": [
                {"name": "Apple", "total": 0},
                {"name": "Banana", "total": 0},
                {"name": "Strawberry","total": 0},
                {"name": "Lettuce", "total": 0},
                {"name": "Potato", "total": 0},
                {"name": "Celery", "total": 0},
                {"name": "Carrot", "total": 0},
                {"name": "Orange", "total": 0},
                {"name": "Avocado", "total": 0},
                {"name": "Blueberry", "total": 0}
                ], 
                "totalRevenue": 0.00
}
with open("totals.json", "w") as file:
    json.dump(new_totals, file, indent=1)