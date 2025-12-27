from typing import Dict, List


def calculate_product_popularity(orders: List[dict]) -> Dict[str, int]:
    # Returns a mapping of productId to total quantity purchased

    popularity: Dict[str, int] = {}

    for order in orders:
        for item in order.get("items", []):
            product_id = item["productId"]
            quantity = item.get("quantity", 1)

            popularity[product_id] = popularity.get(product_id, 0) + quantity

    return popularity

