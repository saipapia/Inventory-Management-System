from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None  # Auto-incremented in DB
    name: str
    category: str
    price: float = Field(gt=0, description="Price must be greater than 0")
    stock: int = Field(ge=0, description="Stock must be 0 or more")

class ProductUpdate(BaseModel):
    price: Optional[float] = Field(default=None, gt=0, description="Price must be greater than 0")
    stock: Optional[int] = Field(default=None, ge=0, description="Stock must be 0 or more")

    class Config:
        validate_assignment = True  # ✅ Ensures validation during updates
