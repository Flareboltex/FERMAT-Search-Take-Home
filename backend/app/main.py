from fastapi import FastAPI
from app.api.products import router as products_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Product Catalog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}