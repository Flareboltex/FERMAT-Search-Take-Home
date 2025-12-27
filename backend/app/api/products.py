from fastapi import APIRouter
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
def get_products():
    return _enriched_products