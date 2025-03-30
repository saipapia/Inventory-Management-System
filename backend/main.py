from fastapi import FastAPI
from backend.routes import products

app = FastAPI()

# Register routers
app.include_router(products.router, prefix="/api", tags=["Products"])
