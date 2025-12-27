from typing import List, Dict

def attach_popularity_to_products(
    products: List[dict],
    popularity_map: Dict[str, int]
) -> List[dict]:
    enriched_products = []

    for product in products:
        product_copy = product.copy()
        product_id = product["id"]

        product_copy["popularity"] = popularity_map.get(product_id, 0)
        enriched_products.append(product_copy)

    return enriched_products