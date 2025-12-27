import json
from pathlib import Path
from typing import List, Dict, Any


BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "data"


def load_json(filename: str) -> List[Dict[str, Any]]:
    file_path = DATA_DIR / filename
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_products(sample: bool = True):
    filename = "sample-products.json" if sample else "products.json"
    return load_json(filename)


def load_orders(sample: bool = True):
    filename = "sample-orders.json" if sample else "orders.json"
    return load_json(filename)
