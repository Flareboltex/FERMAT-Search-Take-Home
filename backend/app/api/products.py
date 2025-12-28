from fastapi import APIRouter, Query
from typing import List, Optional
from app.utils.data_loader import load_products, load_orders
from app.services.popularity_service import calculate_product_popularity
from app.services.product_service import attach_popularity_to_products

router = APIRouter()

# Load data at startup
_products = load_products(sample=True)
_orders = load_orders(sample=True)

_popularity_map = calculate_product_popularity(_orders)
_enriched_products = attach_popularity_to_products(_products, _popularity_map)

@router.get("/products")
def get_products(
    q: Optional[str] = Query(None, description="Search term"),
    category: Optional[str] = Query(None),
    brand: Optional[str] = Query(None),
    minPrice: Optional[float] = Query(None),
    maxPrice: Optional[float] = Query(None),
    sort: Optional[str] = Query(None, description="Sort by: price_asc, price_desc, rating, popularity")
) -> List[dict]:

    filtered = _enriched_products

    # 1️⃣ Search
    if q:
        q_lower = q.lower()
        filtered = [
            p for p in filtered
            if q_lower in p["name"].lower() or q_lower in p["description"].lower()
        ]

    # 2️⃣ Filter by category
    if category:
        filtered = [p for p in filtered if p["category"].lower() == category.lower()]

    # 3️⃣ Filter by brand
    if brand:
        filtered = [p for p in filtered if p["brand"].lower() == brand.lower()]

    # 4️⃣ Filter by price range
    if minPrice is not None:
        filtered = [p for p in filtered if p["price"] >= minPrice]
    if maxPrice is not None:
        filtered = [p for p in filtered if p["price"] <= maxPrice]

    # 5️⃣ Sorting
    if sort:
        reverse = False
        key_func = None

        if sort == "price_asc":
            key_func = lambda p: p["price"]
        elif sort == "price_desc":
            key_func = lambda p: p["price"]
            reverse = True
        elif sort == "rating":
            key_func = lambda p: p["rating"]
            reverse = True
        elif sort == "popularity":
            key_func = lambda p: p["popularity"]
            reverse = True

        if key_func:
            filtered.sort(key=key_func, reverse=reverse)

    return filtered