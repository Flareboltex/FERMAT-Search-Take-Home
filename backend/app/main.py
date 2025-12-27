from fastapi import FastAPI
from app.api.products import router as products_router

app = FastAPI(title="Product Catalog API")

app.include_router(products_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}